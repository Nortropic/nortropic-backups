"""Restore newly downloaded P objects over already remote-verified local B/C bundles.
No checkout, archived code execution, old source mutation or qualification credit.
"""
import hashlib,json,os,subprocess,tempfile
from pathlib import Path
HERE=Path('/Users/elinhaggstrom/nortropic-backups-20260910/github-history-transfer-20260912.HYawFS')
BASE=Path('/Users/elinhaggstrom/nortropic-backups-20260910/full-20260910T103342Z')
SOURCE=Path('/Users/elinhaggstrom/nortropic-repos/work/builder-h039-asset-local-7be3a5ab-20260912')
B='8095d947c83202e2b87801531d9f7cb1457c8719'
C='7be3a5ab20b2079b146984915935a2ed6714c286'
P='005366dd5e3a9a74d8140c9dd0c0175aea268294'
TREE='a548cb8876346eb505906fb3feaa7b8d33ec43aa'
bundles=[
(BASE/'bundles/v316-h039-continuity-product-8095d94.bundle','5cc302c9e867a8a74a43317150dd3a3b956207ba1c43a099fe6da512badd2279'),
(HERE/'h039-contract-C-7be3a5ab-incremental.download.bundle','084bd35fdb07c891efc8b3a7c656d01311c65b144dec1d8837f5bee538a2b2b3'),
(HERE/'h039-product-P-005366dd-incremental.download.bundle','f6f7e95b97d49f1d1c12cc1559d46f0727d870d9d785d0509c978af68a3cf30a')]
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
for p,h in bundles:assert sha(p)==h
assert sha(BASE/'bundles/h039-product-P-005366dd-incremental.bundle')==bundles[-1][1]
output=HERE/'h039-P-005366dd-bundle-restore.json'
assert not output.exists()
env=dict(PATH='/usr/bin:/bin',LANG='C',LC_ALL='C',GIT_CONFIG_NOSYSTEM='1',GIT_CONFIG_GLOBAL='/dev/null',GIT_OPTIONAL_LOCKS='0',GIT_NO_LAZY_FETCH='1')
git_path='/Library/Developer/CommandLineTools/usr/bin/git'
assert sha(Path(git_path))=='be4afb2b003904725826250de9fb76567bbacf82323457b5a1ec26706b66bcae'
root=Path(tempfile.mkdtemp(prefix='nortropic-h039-P-bundle-restore-',dir='/private/tmp'))
commands=[]
def git(where,*args):
 argv=[git_path,'-C',str(where),*args]
 r=subprocess.run(argv,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=120)
 commands.append(dict(argv=argv,exit=r.returncode,stdout_sha256=hashlib.sha256(r.stdout).hexdigest(),stderr_sha256=hashlib.sha256(r.stderr).hexdigest()))
 assert r.returncode==0,(args,r.returncode)
 return r.stdout
git(root,'init','--bare','--template=')
git(root,'bundle','unbundle',str(bundles[0][0]))
git(root,'cat-file','-e',B+'^{commit}')
for p,h in bundles[1:]:
 git(root,'bundle','verify',str(p));git(root,'bundle','unbundle',str(p))
assert git(root,'bundle','list-heads',str(bundles[2][0])).decode().splitlines()==[P+' refs/heads/nortropic/loop-h039-asset-product-local-20260912']
git(root,'update-ref','refs/heads/restored-P',P,'0'*40)
git(root,'symbolic-ref','HEAD','refs/heads/restored-P')
assert git(root,'rev-parse','HEAD').decode().strip()==P
for commit,parent in [(C,B),(P,C)]:
 raw=git(root,'cat-file','commit',commit)
 assert raw==git(SOURCE,'cat-file','commit',commit)
 assert [x for x in raw.splitlines() if x.startswith(b'parent ')]==[b'parent '+parent.encode()]
assert raw.splitlines()[0]==b'tree '+TREE.encode()
tree=git(root,'ls-tree','-rz','--full-tree',P)
assert tree==git(SOURCE,'ls-tree','-rz','--full-tree',P)
rows=[]
for line in tree.split(b'\0')[:-1]:
 header,name=line.split(b'\t',1);mode,kind,oid=header.split()
 assert kind==b'blob' and mode in (b'100644',b'100755')
 raw=git(root,'cat-file','blob',oid.decode())
 assert raw==git(SOURCE,'cat-file','blob',oid.decode())
 assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest().encode()==oid
 rows.append(dict(path=name.decode(),mode=mode.decode(),oid=oid.decode(),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw)))
assert len(rows)==144
git(root,'fsck','--full')
for p,h in bundles:assert sha(p)==h
record=dict(status='REMOTE_P_INCREMENTAL_BUNDLE_RESTORED_OVER_VERIFIED_LOCAL_B_C_BUNDLES',restored=str(root),candidate=P,parent=C,tree=TREE,release_id=387676316,asset_id=559802438,asset_sha256=bundles[-1][1],bundles=[dict(path=str(p),sha256=h) for p,h in bundles],base_and_contract_redownloaded_this_run=False,full_new_remote_base_delta_restore=False,original_admin_state_restored=False,project_code_executed=False,runtime_credit=False,qualification_credit=False,paths=rows,commands=commands)
with output.open('x') as f:
 json.dump(record,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps(dict(restored=str(root),candidate=P,paths=len(rows),commands=len(commands),receipt=str(output))))
