"""Restore one newly downloaded C bundle over the byte-bound existing B bundle.

No project code or checkout, only new bare Git objects/ref. Originals untouched.
The B bundle was previously remote-restored; it is not downloaded again here.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile

HERE = Path('/Users/elinhaggstrom/nortropic-backups-20260910/github-history-transfer-20260912.HYawFS')
BASE = Path('/Users/elinhaggstrom/nortropic-backups-20260910/full-20260910T103342Z')
SOURCE = Path('/Users/elinhaggstrom/nortropic-repos/work/test-author-h039-asset-local-8095d947-20260912')
B = '8095d947c83202e2b87801531d9f7cb1457c8719'
C = '7be3a5ab20b2079b146984915935a2ed6714c286'
TREE = 'f4de53628896dc48233d999c6c45f9f9bc43899a'
base_bundle = BASE / 'bundles/v316-h039-continuity-product-8095d94.bundle'
delta_bundle = HERE / 'h039-contract-C-7be3a5ab-incremental.download.bundle'
source_bundle = BASE / 'bundles/h039-contract-C-7be3a5ab-incremental.bundle'
def sha(p):
    with p.open('rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()
assert sha(base_bundle) == '5cc302c9e867a8a74a43317150dd3a3b956207ba1c43a099fe6da512badd2279'
assert sha(delta_bundle) == sha(source_bundle) == '084bd35fdb07c891efc8b3a7c656d01311c65b144dec1d8837f5bee538a2b2b3'
env = dict(PATH='/usr/bin:/bin', LANG='C', LC_ALL='C', GIT_CONFIG_NOSYSTEM='1',
           GIT_CONFIG_GLOBAL='/dev/null', GIT_OPTIONAL_LOCKS='0', GIT_NO_LAZY_FETCH='1')
root = Path(tempfile.mkdtemp(prefix='nortropic-h039-C-bundle-restore-', dir='/private/tmp'))
os.chmod(root, 0o700)
commands = []
def git(where, *args):
    argv = ['/usr/bin/git', '-C', str(where), *args]
    r = subprocess.run(argv, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    commands.append(dict(argv=argv, exit=r.returncode,
                         stdout_sha256=hashlib.sha256(r.stdout).hexdigest(),
                         stderr_sha256=hashlib.sha256(r.stderr).hexdigest()))
    assert r.returncode == 0, (args, r.returncode)
    return r.stdout
git(root, 'init', '--bare', '--template=')
git(root, 'bundle', 'unbundle', str(base_bundle))
git(root, 'cat-file', '-e', B + '^{commit}')
git(root, 'bundle', 'verify', str(delta_bundle))
assert git(root, 'bundle', 'list-heads', str(delta_bundle)).decode().splitlines() == [C + ' refs/heads/nortropic/loop-h039-asset-local-20260912']
git(root, 'bundle', 'unbundle', str(delta_bundle))
git(root, 'update-ref', 'refs/heads/restored-C', C, '0' * 40)
git(root, 'symbolic-ref', 'HEAD', 'refs/heads/restored-C')
assert git(root, 'rev-parse', 'HEAD').strip().decode() == C
raw_commit = git(root, 'cat-file', 'commit', C)
assert raw_commit == git(SOURCE, 'cat-file', 'commit', C)
assert [line for line in raw_commit.splitlines() if line.startswith(b'parent ')] == [b'parent ' + B.encode()]
assert raw_commit.splitlines()[0] == b'tree ' + TREE.encode()
tree = git(root, 'ls-tree', '-rz', '--full-tree', C)
assert tree == git(SOURCE, 'ls-tree', '-rz', '--full-tree', C)
rows = []
for line in tree.split(b'\0')[:-1]:
    header, name = line.split(b'\t', 1)
    mode, kind, oid = header.split()
    assert kind == b'blob' and mode in (b'100644', b'100755')
    raw = git(root, 'cat-file', 'blob', oid.decode())
    assert raw == git(SOURCE, 'cat-file', 'blob', oid.decode())
    assert hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest().encode() == oid
    rows.append(dict(path=name.decode(), mode=mode.decode(), oid=oid.decode(),
                     sha256=hashlib.sha256(raw).hexdigest(), bytes=len(raw)))
assert len(rows) == 144
git(root, 'fsck', '--full')
assert sha(delta_bundle) == sha(source_bundle) == '084bd35fdb07c891efc8b3a7c656d01311c65b144dec1d8837f5bee538a2b2b3'
record = dict(status='REMOTE_C_INCREMENTAL_BUNDLE_RESTORED_OVER_VERIFIED_LOCAL_B_BUNDLE',
              restored=str(root), candidate=C, parent=B, tree=TREE,
              source_bundle_sha256=sha(source_bundle), base_bundle_sha256=sha(base_bundle),
              base_redownloaded_this_run=False, full_new_remote_base_delta_restore=False,
              original_admin_state_restored=False, project_code_executed=False,
              runtime_credit=False, paths=rows, commands=commands)
output = HERE / 'h039-C-7be3a5ab-bundle-restore.json'
with output.open('x') as f:
    json.dump(record, f, indent=2)
    f.write('\n')
    f.flush()
    os.fsync(f.fileno())
print(json.dumps(dict(restored=str(root), candidate=C, tree=TREE,
                      paths=len(rows), commands=len(commands), receipt=str(output))))
