"""Replay only the pinned YM.Branch.Pick local import closure in an output workspace.

Usage: python3 replay_branch.py UPSTREAM LEAN_BINARY PACKAGE_DIRECTORY OUTPUT_DIRECTORY
All generated source copies, object files and raw logs go to OUTPUT_DIRECTORY.
An unsuccessful compilation is recorded and stops the replay; source is never patched.
"""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

upstream, lean, packages, output = map(lambda x: Path(x).resolve(), sys.argv[1:])
assert upstream != output and upstream not in output.parents
pin = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=upstream, text=True).strip()
if pin != '3456e5e75cf8d4cd558955a5c7638fba2d68f464':
    raise SystemExit('Unexpected upstream revision')
seen, ordered, external = set(), [], set()


def visit(name):
    if name in seen:
        return
    seen.add(name)
    source = upstream/(name.replace('.', '/')+'.lean')
    for line in source.read_text().splitlines():
        if line.startswith('import '):
            for dep in line.split()[1:]:
                if dep.startswith('YM.'):
                    visit(dep)
                else:
                    external.add(dep)
    ordered.append(name)


visit('YM.Branch.Pick')
source_root, lib, logs = (output/x for x in ('src', 'lib', 'logs'))
for p in (source_root, lib, logs):
    p.mkdir(parents=True, exist_ok=True)
manifest = {}
for name in ordered:
    rel = Path(name.replace('.', '/')+'.lean')
    dest = source_root/rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(upstream/rel, dest)
    manifest[str(rel)] = hashlib.sha256(dest.read_bytes()).hexdigest()
extra = 'YM/Next/FOUNDATIONS/Primary.lean'
manifest[extra] = hashlib.sha256((upstream/extra).read_bytes()).hexdigest()
probe = source_root/'BranchProbe.lean'
probe.write_text('import YM.Branch.Pick\n'+'\n'.join(
    '#print axioms '+name for name in ['YM.Branch.Pairs.compare_energy',
    'YM.Branch.Pairs.closeness', 'YM.Branch.align', 'YM.RG.frame_unique',
    'YM.RG.predictor_unique', 'YM.Axial.eligible', 'YM.Axial.viable'])+'\n')
env = os.environ.copy()
env['LEAN_PATH'] = os.pathsep.join([str(lib)]+[str(p/'.lake/build/lib/lean')
    for p in sorted(packages.iterdir()) if (p/'.lake/build/lib/lean').is_dir()])
env['TMPDIR'] = str(output/'tmp')
Path(env['TMPDIR']).mkdir(exist_ok=True)
report = {'upstream_commit': pin, 'lean_version': subprocess.check_output([str(lean),'--version'],text=True).strip(),
          'local_import_closure_count': len(ordered), 'external_imports': sorted(external),
          'source_sha256': manifest, 'source_changed': False, 'runs': [],
          'branch_replay_complete': False, 'full_upstream_replay': False,
          'foundation_kernel_consumer_compiled': False}
for name in ordered+['BranchProbe']:
    rel = Path(name.replace('.', '/'))
    obj = lib/rel.with_suffix('.olean')
    obj.parent.mkdir(parents=True, exist_ok=True)
    log = logs/(name+'.log')
    cmd = [str(lean), '--trust=0', '-j1', '-DmaxHeartbeats=0', '-DmaxRecDepth=4096',
           '-R', str(source_root), '-o', str(obj), str(source_root/rel.with_suffix('.lean'))]
    start = time.monotonic()
    try:
        with log.open('w') as f:
            run = subprocess.run(cmd, cwd=source_root, env=env, stdout=f, stderr=subprocess.STDOUT, timeout=120)
        code = run.returncode
    except subprocess.TimeoutExpired:
        code = 'timeout_120_seconds'
    report['runs'].append({'module': name, 'exit_code': code, 'elapsed_seconds': round(time.monotonic()-start,3),
                           'log_sha256': hashlib.sha256(log.read_bytes()).hexdigest()})
    print(name, code, flush=True)
    (output/'replay-report.json').write_text(json.dumps(report,indent=2)+'\n')
    if code != 0:
        print(log.read_text()[-5000:], flush=True)
        break
else:
    report['branch_replay_complete'] = True
    (output/'replay-report.json').write_text(json.dumps(report,indent=2)+'\n')
print('branch_replay_complete:', report['branch_replay_complete'], flush=True)
