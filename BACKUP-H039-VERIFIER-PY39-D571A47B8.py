"""Backup only: new verifier py39 D delta; restore in a fresh bare repository. No project execution."""
import ast,hashlib,json,os,re,signal,stat,subprocess,sys,tempfile
from pathlib import Path
HERE=Path('/Users/elinhaggstrom/nortropic-backups-20260910/github-history-transfer-20260912.HYawFS')
BASE=Path('/Users/elinhaggstrom/nortropic-backups-20260910/full-20260910T103342Z')
SOURCE=Path('/Users/elinhaggstrom/nortropic-repos/work/test-author-h039-verifier-py39-C83f75968-20260912')
C='571a47b8f5fbf1718125742718d2f5908d49e95c'
P='83f75968b9892ae98a6a879178c407d2a6fd935e'
TREE='10d70b1b77601b72b07c633510cb12f5ac657b02'
REF='refs/heads/nortropic/loop-h039-verifier-py39-local-20260912'
BUNDLE=BASE/'bundles/h039-verifier-py39-D-571a47b8-incremental.bundle'
DOWNLOAD=HERE/'h039-verifier-py39-D-571a47b8-incremental.download.bundle'
INSPECTION=HERE/'h039-verifier-py39-D-571a47b8-bundle-inspection.json'
RESTORE=HERE/'h039-verifier-py39-D-571a47b8-bundle-restore.json'
GIT='/Library/Developer/CommandLineTools/usr/bin/git'
ENV={'PATH':'/usr/bin:/bin','LANG':'C','LC_ALL':'C','GIT_CONFIG_NOSYSTEM':'1','GIT_CONFIG_GLOBAL':'/dev/null','GIT_OPTIONAL_LOCKS':'0','GIT_NO_LAZY_FETCH':'1','GIT_ALLOW_PROTOCOL':'file'}
commands=[];cancelled=None
def sha(raw):return hashlib.sha256(raw).hexdigest()
def latch(signum,frame):
 global cancelled
 if cancelled is None:cancelled=signum
def check():
 if cancelled is not None:raise ValueError('CANCELLED_PRESERVE_NO_RETRY',cancelled)
def git(root,*args):
 check()
 argv=[GIT,'--no-pager','--no-replace-objects','-c','core.hooksPath=/dev/null',*args]
 row={'argv':argv,'cwd':str(root),'pid':None,'exit':None,'status':'SPAWN_NOT_RETURNED'};commands.append(row)
 child=subprocess.Popen(argv,cwd=root,env=ENV,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=subprocess.PIPE,start_new_session=True)
 row.update(pid=child.pid,status='OWNED_COMMAND_STARTED')
 try:
  out,err=child.communicate(timeout=60)
  row.update(exit=child.returncode,status='DIRECT_CHILD_TERMINAL',stdout_sha256=sha(out),stderr_sha256=sha(err))
  check()
 except BaseException as exc:
  if row['status']!='DIRECT_CHILD_TERMINAL':row['status']='UNRESOLVED_PRESERVED_NO_RETRY'
  row['error']=type(exc).__name__;print(json.dumps({'commands':commands}),file=sys.stderr,flush=True);raise
 assert child.returncode==0 and len(out)<8388608,row
 return out
def save(path,value):
 check()
 with path.open('x') as f:json.dump(value,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
assert sys.argv[1:] in (['prepare'],['restore'])
assert sha(Path(GIT).read_bytes())=='be4afb2b003904725826250de9fb76567bbacf82323457b5a1ec26706b66bcae'
assert sha(Path(sys.executable).read_bytes())=='94be2db6796807c796419e7adbc45cbff3e71966c107c2adcbf931cf70393941'
disk=os.statvfs('/private/tmp');assert disk.f_bavail*disk.f_frsize>=21474836480+67108864
previous={s:signal.getsignal(s) for s in (signal.SIGINT,signal.SIGTERM)}
for s in previous:signal.signal(s,latch)
if sys.argv[1]=='prepare':
 assert not os.path.lexists(BUNDLE) and not os.path.lexists(INSPECTION)
 assert git(SOURCE,'rev-parse','HEAD').strip().decode()==C
 assert git(SOURCE,'show','-s','--format=%P%n%T',C).decode().splitlines()==[P,TREE]
 assert git(SOURCE,'status','--porcelain=v1','--untracked-files=all')==b''
 patterns_tree=ast.parse(Path('/Users/elinhaggstrom/nortropic-backups-20260910/github-transfer-20260912.dVjQlj/inspect_first_batch.py').read_bytes())
 patterns=ast.literal_eval(next(n.value for n in patterns_tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PATTERNS' for t in n.targets)))
 rows=[];findings=[]
 for line in git(SOURCE,'rev-list','--objects',C,'^'+P).splitlines():
  oid=line.split(b' ',1)[0].decode();kind=git(SOURCE,'cat-file','-t',oid).strip().decode()
  raw=git(SOURCE,'cat-file',kind,oid)
  assert hashlib.sha1(kind.encode()+b' '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==oid
  rows.append({'oid':oid,'kind':kind,'bytes':len(raw),'sha256':sha(raw)})
  for name,pat in patterns.items():
   for m in re.finditer(pat,raw):findings.append({'oid':oid,'kind':name,'offset':m.start()})
 assert not findings,findings
 git(SOURCE,'bundle','create',str(BUNDLE),REF,'^'+P)
 assert git(SOURCE,'bundle','list-heads',str(BUNDLE)).decode().splitlines()==[C+' '+REF]
 git(SOURCE,'bundle','verify',str(BUNDLE))
 assert git(SOURCE,'status','--porcelain=v1','--untracked-files=all')==b''
 save(INSPECTION,{'status':'LOCAL_NEW_OBJECTS_INSPECTED_NOT_UPLOADED','candidate':C,'parent':P,'tree':TREE,'bundle_sha256':sha(BUNDLE.read_bytes()),'bundle_bytes':BUNDLE.stat().st_size,'new_objects':rows,'findings':findings,'scan_scope':'All new decompressed Git objects; bounded patterns not proof of absence','commands':commands,'runtime_credit':False})
 result={'inspection':str(INSPECTION),'bundle_sha256':sha(BUNDLE.read_bytes()),'objects':len(rows),'bytes':BUNDLE.stat().st_size}
else:
 m=json.loads(INSPECTION.read_bytes());assert not m['findings'] and sha(DOWNLOAD.read_bytes())==sha(BUNDLE.read_bytes())==m['bundle_sha256'] and not RESTORE.exists()
 bundles=[
 (BASE/'bundles/v316-h039-continuity-product-8095d94.bundle','5cc302c9e867a8a74a43317150dd3a3b956207ba1c43a099fe6da512badd2279'),
 (HERE/'h039-contract-C-7be3a5ab-incremental.download.bundle','084bd35fdb07c891efc8b3a7c656d01311c65b144dec1d8837f5bee538a2b2b3'),
 (HERE/'h039-product-P-005366dd-incremental.download.bundle','f6f7e95b97d49f1d1c12cc1559d46f0727d870d9d785d0509c978af68a3cf30a'),
 (HERE/'h039-verifier-C-83f75968-incremental.download.bundle','81cabd9181d7341a1c53c25d6739a73042523de3ee9d10ef081905c78d19e6e9'),
 (DOWNLOAD,m['bundle_sha256'])]
 for path,h in bundles:assert sha(path.read_bytes())==h
 check();root=Path(tempfile.mkdtemp(prefix='nortropic-h039-verifier-py39-D-restore-',dir='/private/tmp'))
 git(root,'init','--bare','--template=')
 for path,h in bundles:git(root,'bundle','unbundle',str(path))
 assert git(root,'bundle','list-heads',str(DOWNLOAD)).decode().splitlines()==[C+' '+REF]
 git(root,'update-ref','refs/heads/restored-verifier-py39-D',C,'0'*40)
 git(root,'symbolic-ref','HEAD','refs/heads/restored-verifier-py39-D')
 commit=git(root,'cat-file','commit',C);assert commit==git(SOURCE,'cat-file','commit',C)
 assert commit.splitlines()[0]==b'tree '+TREE.encode() and [x for x in commit.splitlines() if x.startswith(b'parent ')]==[b'parent '+P.encode()]
 listing=git(root,'ls-tree','-rz','--full-tree',C);assert listing==git(SOURCE,'ls-tree','-rz','--full-tree',C)
 rows=[]
 for line in listing.split(b'\0')[:-1]:
  header,name=line.split(b'\t',1);mode,kind,oid=header.split();assert kind==b'blob' and mode in (b'100644',b'100755')
  raw=git(root,'cat-file','blob',oid.decode());assert raw==git(SOURCE,'cat-file','blob',oid.decode())
  assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest().encode()==oid
  rows.append({'path':name.decode(),'mode':mode.decode(),'oid':oid.decode(),'sha256':sha(raw),'bytes':len(raw)})
 assert len(rows)==144
 git(root,'fsck','--full')
 for path,h in bundles:assert sha(path.read_bytes())==h
 save(RESTORE,{'status':'DOWNLOADED_VERIFIER_PY39_D_RESTORED_OVER_PREVIOUSLY_VERIFIED_LOCAL_B_C_P_C83_BUNDLES','restored':str(root),'candidate':C,'parent':P,'tree':TREE,'bundle_sha256':m['bundle_sha256'],'bundles':[{'path':str(p),'sha256':h} for p,h in bundles],'base_redownloaded':False,'full_new_remote_base_delta_restore':False,'original_admin_state_restored':False,'project_code_executed':False,'runtime_credit':False,'paths':rows,'commands':commands})
 result={'restored':str(root),'paths':len(rows),'commands':len(commands),'receipt':str(RESTORE)}
for s,h in previous.items():signal.signal(s,h)
check()
print(json.dumps(result))
