"""Run the elaboration checks and write logs plus verification.json here.

Usage: python run_checks.py UPSTREAM_DIR
UPSTREAM_DIR is a checkout of yang-mills-group/OpenAI-YM-20261028 at
3456e5e75cf8d4cd558955a5c7638fba2d68f464 on which `lake exe cache get` and
`lake build WilsonPublic` have already succeeded.
"""
import datetime, hashlib, json, pathlib, subprocess, sys, tempfile

here = pathlib.Path(__file__).resolve().parent
root = here.parents[2]
up = pathlib.Path(sys.argv[1]).resolve()
targets = {
    "MassGapTarget": root / "research/mass-gap-20261111/MassGapTarget.lean",
    "SpecVariants": root / "auto-research/reviews/2026-11-12-T01-gap-target-specification/SpecVariants.lean",
}
tmp = pathlib.Path(tempfile.mkdtemp())
probe = tmp / "Checks.lean"
subprocess.run([sys.executable, "-I", str(here / "make_probe.py"), str(probe)], check=True)
text = probe.read_text(encoding="utf-8")
control = tmp / "ControlReversed.lean"
bad = text.replace("(hle : m' ≤ m)", "(hle : m ≤ m')")
assert bad != text
control.write_text(bad, encoding="utf-8", newline="\n")

def sha(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()

def lean(path):
    r = subprocess.run(["lake", "env", "lean", "--trust=0", str(path)], cwd=up,
                       capture_output=True, text=True, encoding="utf-8")
    return r.returncode, (r.stdout + r.stderr).replace(str(tmp), "<tmp>").replace(str(root), "<repo>")

b = subprocess.run(["lake", "build", "WilsonPublic"], cwd=up, capture_output=True, text=True, encoding="utf-8")
(here / "WilsonPublic-build.log").write_text(b.stdout + b.stderr, encoding="utf-8", newline="\n")
runs = []
for name, path in [*targets.items(), ("Checks", probe), ("ControlReversed", control)]:
    code, out = lean(path)
    (here / f"{name}.log").write_text(out, encoding="utf-8", newline="\n")
    runs.append({"file": name, "command": ["lake", "env", "lean", "--trust=0", name + ".lean"],
                 "exit_code": code, "expected_exit_code": 1 if name == "ControlReversed" else 0,
                 "input_sha256": sha(path), "log": f"{name}.log"})

ver = subprocess.run(["lake", "env", "lean", "--version"], cwd=up, capture_output=True, text=True).stdout.strip()
manifest = json.loads((up / "lake-manifest.json").read_text(encoding="utf-8"))
receipt = {
    "date": datetime.date.today().isoformat(),
    "evidence": "Lean elaboration with --trust=0 by a contributor who did not write the targets; AI-assisted; no subject-expert review",
    "upstream": "yang-mills-group/OpenAI-YM-20261028",
    "upstream_commit": subprocess.run(["git", "rev-parse", "HEAD"], cwd=up, capture_output=True, text=True).stdout.strip(),
    "lean_version": ver,
    "dependency_revisions": {p["name"]: p["rev"] for p in manifest["packages"]},
    "prerequisite_note": "`lake exe cache get` was run beforehand (exit 0, log not kept); the build below is rerun by this script",
    "prerequisite_command": ["lake", "build", "WilsonPublic"],
    "prerequisite_exit_code": b.returncode,
    "prerequisite_log": "WilsonPublic-build.log",
    "probe_generator": "make_probe.py (verbatim target bodies + ChecksTail.lean)",
    "checks_tail_sha256": sha(here / "ChecksTail.lean"),
    "runs": runs,
    "all_as_expected": b.returncode == 0 and all(r["exit_code"] == r["expected_exit_code"] for r in runs),
}
(here / "verification.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps({r["file"]: r["exit_code"] for r in runs}), receipt["all_as_expected"])
