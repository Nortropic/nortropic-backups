"""Fixed 97-file P construction/failure checkpoint, no code execution.
BSD tar keeps source-relative hierarchy to avoid duplicate result/stdout basenames.
Only selected regular single-link files; no directories, links or secret custody.
"""
import ast,base64,datetime,decimal,hashlib,json,os,re,stat,subprocess,sys,tarfile,tempfile
from pathlib import Path
HERE=Path('/Users/elinhaggstrom/nortropic-backups-20260910/github-history-transfer-20260912.HYawFS')
BASE=Path('/Users/elinhaggstrom/nortropic-backups-20260910/full-20260910T103342Z')
LIST=HERE/'h039-P-005366dd-evidence-selection.json'
ARCHIVE=BASE/'external/h039-P-005366dd-construction-and-first-final-20260912.tar.gz'
MANIFEST=HERE/'h039-P-005366dd-evidence-inspection.json'
DOWNLOAD=HERE/'h039-P-005366dd-construction-and-first-final-20260912.download.tar.gz'
RECEIPT=HERE/'h039-P-005366dd-evidence-restore.json'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def identity(p):
 s=p.lstat();assert stat.S_ISREG(s.st_mode) and s.st_nlink==1 and s.st_uid==os.geteuid() and not s.st_flags
 return [s.st_dev,s.st_ino,s.st_mode,s.st_uid,s.st_gid,s.st_nlink,s.st_size,s.st_mtime_ns,s.st_ctime_ns]
def save(p,obj):
 with p.open('x') as f:json.dump(obj,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
def attrs(p):
 names=subprocess.check_output(['/usr/bin/xattr',str(p)],text=True).splitlines()
 assert set(names)<={'com.apple.provenance'}
 return {n:base64.b64encode(bytes.fromhex(subprocess.check_output(['/usr/bin/xattr','-px',n,str(p)],text=True))).decode() for n in names}
assert sys.argv[1:] in (['prepare'],['verify'])
disk=os.statvfs('/private/tmp');assert disk.f_bavail*disk.f_frsize>=21474836480+33554432
if sys.argv[1]=='prepare':
 assert sha(LIST)=='ac40ff15bee08e2391026b43a8c9c128de129a05eab147da0a768038f1f41297'
 items=json.loads(LIST.read_bytes());assert items['count']==96
 selected={Path(x['path']):x['sha256'] for x in items['rows']};selected[LIST]=sha(LIST);assert len(selected)==97
 before={p:identity(p) for p in selected}
 for p,h in selected.items():assert p.resolve()==p and sha(p)==h and p.stat().st_size<8*1024**2
 expected={str(p.relative_to('/')):p for p in selected};assert len(expected)==97
 sidecars={str(Path(n).with_name('._'+Path(n).name)) for n in expected}
 assert not ARCHIVE.exists() and not MANIFEST.exists()
 cmd=['/usr/bin/tar','-czf',str(ARCHIVE),'-C','/',*expected]
 r=subprocess.run(cmd,capture_output=True,timeout=60);assert r.returncode==0 and not r.stdout and not r.stderr
 tree=ast.parse(Path('/Users/elinhaggstrom/nortropic-backups-20260910/github-transfer-20260912.dVjQlj/inspect_first_batch.py').read_bytes())
 patterns=ast.literal_eval(next(n.value for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PATTERNS' for t in n.targets)))
 rows=[];findings=[]
 with tarfile.open(ARCHIVE,'r:gz') as tar:
  members=tar.getmembers();names=[m.name for m in members];assert len(names)==len(set(names)) and set(expected)<=set(names)<=set(expected)|sidecars
  for m in members:
   assert m.isfile() and not m.name.startswith('/') and all(x not in ('','.','..') for x in m.name.split('/')) and m.size<8*1024**2 and not m.mode&0o7000
   raw=tar.extractfile(m).read();assert len(raw)==m.size
   assert set(m.pax_headers)<={'mtime','LIBARCHIVE.xattr.com.apple.provenance','SCHILY.xattr.com.apple.provenance'}
   if m.name in sidecars:assert raw[:4]==bytes.fromhex('00051607') and b'com.apple.provenance\0' in raw
   else:assert sha(expected[m.name])==hashlib.sha256(raw).hexdigest()==selected[expected[m.name]]
   for label,pattern in patterns.items():
    for hit in re.finditer(pattern,raw):findings.append(dict(path=m.name,kind=label,offset=hit.start()))
   row=dict(path=m.name,sha256=hashlib.sha256(raw).hexdigest(),bytes=m.size,mode=m.mode,uid=m.uid,gid=m.gid,pax=m.pax_headers)
   if m.name in expected:
    p=expected[m.name];row.update(source=str(p),source_identity=list(map(str,before[p])),xattrs=attrs(p))
    assert (m.size,m.mode,m.uid,m.gid)==(before[p][6],stat.S_IMODE(before[p][2]),before[p][3],before[p][4])
    assert int(decimal.Decimal(m.pax_headers['mtime'])*10**9)==before[p][7]
   rows.append(row)
 for p,h in selected.items():assert sha(p)==h and identity(p)==before[p]
 save(MANIFEST,dict(status='LOCAL_INSPECTED_NOT_UPLOADED',archive_sha256=sha(ARCHIVE),archive_bytes=ARCHIVE.stat().st_size,files=rows,findings=findings,logical_files=97,source_unchanged=True,command=cmd,exit=0,scope='Exact P construction methods/reviews, two raw construction lanes and first failed final captures/snapshots; not full final fixture/admin/continuity or later corrected replica work',runtime_credit=False))
 print(json.dumps(dict(files=len(rows),logical_files=97,bytes=ARCHIVE.stat().st_size,sha256=sha(ARCHIVE),findings=findings)))
else:
 m=json.loads(MANIFEST.read_bytes());assert not m['findings'] and sha(DOWNLOAD)==m['archive_sha256']==sha(ARCHIVE) and not RECEIPT.exists()
 target=Path(tempfile.mkdtemp(prefix='nortropic-h039-P-evidence-restore-',dir='/private/tmp'))
 r=subprocess.run(['/usr/bin/tar','-xzf',str(DOWNLOAD),'-C',str(target)],capture_output=True,timeout=60);assert r.returncode==0 and not r.stdout and not r.stderr
 rows=[x for x in m['files'] if 'source' in x];assert len(rows)==97
 expected={x['path'] for x in rows}
 actual=set()
 for parent,dirs,files in os.walk(target,followlinks=False):
  for n in dirs:assert stat.S_ISDIR((Path(parent)/n).lstat().st_mode)
  for n in files:actual.add(str((Path(parent)/n).relative_to(target)))
 assert actual==expected
 for row in rows:
  p=target/row['path'];s=p.lstat();assert p.resolve()==p and stat.S_ISREG(s.st_mode) and s.st_uid==row['uid']==os.geteuid() and s.st_nlink==1
  if s.st_gid!=row['gid']:os.chown(p,-1,row['gid'],follow_symlinks=False)
  s=p.lstat();assert (s.st_size,stat.S_IMODE(s.st_mode),s.st_uid,s.st_gid,s.st_mtime_ns)==(row['bytes'],row['mode'],row['uid'],row['gid'],int(decimal.Decimal(row['pax']['mtime'])*10**9))
  assert sha(p)==row['sha256'] and attrs(p)==row['xattrs'] and list(map(str,[s.st_dev,s.st_ino]))!=row['source_identity'][:2]
 save(RECEIPT,dict(time_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='DOWNLOADED_97_P_EVIDENCE_FILES_RESTORED_VERIFIED',inspection_sha256=sha(MANIFEST),archive_sha256=m['archive_sha256'],archive_bytes=m['archive_bytes'],restored=str(target),logical_files=97,checked=['file_membership','bytes','size','mode','uid','gid','mtime_ns','xattrs','single_link_independent_inode'],directory_metadata_restored=False,original_inode_recreated=False,project_code_executed=False,runtime_credit=False,full_final_fixture_restored=False))
 print('97 actual downloaded selected files restored, no code execution')
