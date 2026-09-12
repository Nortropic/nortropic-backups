"""Bounded incremental backup of fixed C, R4, review and continuity files; no project execution."""
import ast,base64,datetime,decimal,hashlib,json,os,re,stat,subprocess,sys,tarfile,tempfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
EVID=Path('/private/tmp/nortropic-v313-contract.Fq5ueV')
REV=Path('/Users/elinhaggstrom/nortropic/evidence/v316-h039-continuity-review-20260912')
BASE=Path('/Users/elinhaggstrom/nortropic-backups-20260910/full-20260910T103342Z')
ARCHIVE=BASE/'external/h039-contract-C-7be3a5ab-20260912.tar.gz'
MANIFEST=HERE/'h039-C-7be3a5ab-backup-inspection.json'
DOWNLOAD=HERE/'h039-contract-C-7be3a5ab-20260912.download.tar.gz'

def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def identity(p):
 s=p.lstat();assert stat.S_ISREG(s.st_mode) and s.st_nlink==1 and s.st_uid==os.geteuid() and not s.st_flags
 return [s.st_dev,s.st_ino,s.st_mode,s.st_uid,s.st_gid,s.st_nlink,s.st_size,s.st_mtime_ns,s.st_ctime_ns]
def save(path,obj):
 with path.open('x') as f:json.dump(obj,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
def attrs(p):
 names=subprocess.check_output(['/usr/bin/xattr',str(p)],text=True).splitlines()
 assert set(names)<= {'com.apple.provenance'}
 return {n:base64.b64encode(bytes.fromhex(subprocess.check_output(['/usr/bin/xattr','-px',n,str(p)],text=True))).decode() for n in names}

mode=sys.argv[1];assert mode in ('prepare','verify')
if mode=='prepare':
 listing=HERE/'h039-C-7be3a5ab-backup-selection.sha256'
 assert sha(listing)=='c5d24c45e255a41bfcc4aadc017e7ff63b930d029139e5d6b3ab3ce3241fc824'
 selected={Path(line.split('  ',1)[1]):line.split('  ',1)[0] for line in listing.read_text().splitlines()}
 selected[listing]=sha(listing)
 assert len(selected)==55 and len({p.name for p in selected})==55
 before={p:identity(p) for p in selected}
 for p,digest in selected.items():assert p.parent in (EVID,REV,HERE,Path('/private/tmp/h039-asset-measure-lifecycle-bw_y6e7e'),Path('/private/tmp/h039-contract-absence-f736rd5u'),Path('/Users/elinhaggstrom/nortropic')) and p.resolve()==p and sha(p)==digest and p.stat().st_size<8*1024**2
 assert not ARCHIVE.exists()
 cmd=['/usr/bin/tar','-czf',str(ARCHIVE)]
 for p in selected:cmd+=['-C',str(p.parent),p.name]
 r=subprocess.run(cmd,capture_output=True);assert r.returncode==0 and not r.stdout and not r.stderr
 old=Path('/Users/elinhaggstrom/nortropic-backups-20260910/github-transfer-20260912.dVjQlj/inspect_first_batch.py')
 tree=ast.parse(old.read_bytes());patterns=ast.literal_eval(next(n.value for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PATTERNS' for t in n.targets)))
 rows=[];findings=[];expected={p.name:p for p in selected}
 with tarfile.open(ARCHIVE,'r:gz') as tar:
  members=tar.getmembers();names=[m.name for m in members]
  assert len(names)==len(set(names)) and set(expected)<=set(names)<=set(expected)|{'._'+n for n in expected}
  for m in members:
   assert m.isfile() and '/' not in m.name and m.name not in ('.','..') and m.size<8*1024**2 and not m.mode&0o7000
   raw=tar.extractfile(m).read();assert len(raw)==m.size
   assert set(m.pax_headers)<={'mtime','LIBARCHIVE.xattr.com.apple.provenance','SCHILY.xattr.com.apple.provenance'}
   if m.name.startswith('._'):
    assert raw[:4]==bytes.fromhex('00051607') and b'com.apple.provenance\0' in raw
   else:
    raw.decode('utf8');assert b'\0' not in raw and hashlib.sha256(raw).hexdigest()==selected[expected[m.name]]
   for label,pattern in patterns.items():
    for hit in re.finditer(pattern,raw):findings.append(dict(path=m.name,kind=label,line=raw[:hit.start()].count(b'\n')+1))
   row=dict(path=m.name,sha256=hashlib.sha256(raw).hexdigest(),bytes=m.size,mode=m.mode,uid=m.uid,gid=m.gid,pax=m.pax_headers,mtime=m.mtime)
   if m.name in expected:
    p=expected[m.name];row.update(source=str(p),source_identity=before[p],xattrs=attrs(p))
    assert (m.size,m.mode,m.uid,m.gid)==(before[p][6],stat.S_IMODE(before[p][2]),before[p][3],before[p][4])
    assert int(decimal.Decimal(m.pax_headers['mtime'])*10**9)==before[p][7]
   rows.append(row)
 for p,h in selected.items():assert sha(p)==h and identity(p)==before[p]
 save(MANIFEST,dict(source=str(ARCHIVE),archive_sha256=sha(ARCHIVE),archive_bytes=ARCHIVE.stat().st_size,files=rows,findings=findings,source_unchanged=True,command=cmd,exit=0,
  scope='55 exact selected C held sources, R1-R4 methods, R4/C execution records, reviews, source snapshots and continuity files; not a full worktree/admin backup or later edits',
  prior_subject_dependency='H039-PHASE-RESTORE-RECEIPT.json preserves prior 775b/748b tranche; v316-h039-continuity-product-8095d94.bundle preserves B; separate C incremental Git bundle required for C graph',
  status='LOCAL_INSPECTED_NOT_UPLOADED',runtime_credit=False))
 print(json.dumps(dict(files=len(rows),logical_files=55,bytes=ARCHIVE.stat().st_size,sha256=sha(ARCHIVE),findings=findings)))
else:
 m=json.loads(MANIFEST.read_bytes());assert not m['findings'] and sha(DOWNLOAD)==m['archive_sha256']==sha(ARCHIVE)
 target=Path(tempfile.mkdtemp(prefix='nortropic-h039-C-restore-',dir='/private/tmp'))
 r=subprocess.run(['/usr/bin/tar','-xzf',str(DOWNLOAD),'-C',str(target)],capture_output=True);assert r.returncode==0 and not r.stdout and not r.stderr
 rows=[x for x in m['files'] if 'source' in x];assert {p.name for p in target.iterdir()}=={x['path'] for x in rows}
 for row in rows:
  p=target/row['path'];s=p.lstat();assert stat.S_ISREG(s.st_mode) and s.st_uid==row['uid']==os.geteuid() and s.st_nlink==1
  if s.st_gid!=row['gid']:os.chown(p,-1,row['gid'],follow_symlinks=False)
  s=p.lstat();assert (s.st_size,stat.S_IMODE(s.st_mode),s.st_uid,s.st_gid,s.st_mtime_ns)==(row['bytes'],row['mode'],row['uid'],row['gid'],int(decimal.Decimal(row['pax']['mtime'])*10**9))
  assert sha(p)==row['sha256'] and attrs(p)==row['xattrs']
  assert [s.st_dev,s.st_ino]!=row['source_identity'][:2]
 save(HERE/'h039-C-7be3a5ab-backup-restore.json',dict(time_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='DOWNLOADED_FILES_RESTORED_VERIFIED',inspection_sha256=sha(MANIFEST),archive_sha256=m['archive_sha256'],archive_bytes=m['archive_bytes'],restored=str(target),logical_files=55,
  checked=['membership','bytes','size','mode','uid','gid','mtime_ns','xattrs','single_link_independent_inode'],source_archive_unchanged=True,original_inode_recreated=False,project_code_executed=False,runtime_credit=False))
 print('55 actual downloaded files restored with recorded metadata; no project execution')
