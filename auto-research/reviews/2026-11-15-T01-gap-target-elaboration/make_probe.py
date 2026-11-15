"""Build Checks.lean from the two target files, unchanged, plus ChecksTail.lean.

Usage (from the repository root):
    python auto-research/reviews/2026-11-15-T01-gap-target-elaboration/make_probe.py OUT.lean
"""
import pathlib
import sys

here = pathlib.Path(__file__).resolve().parent
root = here.parents[2]
sources = [
    root / "research/mass-gap-20261111/MassGapTarget.lean",
    root / "auto-research/reviews/2026-11-12-T01-gap-target-specification/SpecVariants.lean",
]
parts = ["import ChallengeSpec\n"]
for src in sources:
    lines = src.read_text(encoding="utf-8").splitlines(keepends=True)
    assert lines[0].strip() == "import ChallengeSpec", src
    parts.append(f"\n-- ===== verbatim body of {src.relative_to(root).as_posix()} =====\n")
    parts.extend(lines[1:])
parts.append("\n-- ===== ChecksTail.lean =====\n")
parts.append((here / "ChecksTail.lean").read_text(encoding="utf-8"))
pathlib.Path(sys.argv[1]).write_text("".join(parts), encoding="utf-8", newline="\n")
