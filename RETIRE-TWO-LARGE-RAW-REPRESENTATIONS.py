"""Exactly two checked raw backup representations; retain local gzip and remote raw parts.
No recursive operation, repo/worktree removal, upload, or automatic retry.
"""
import datetime,gzip,hashlib,json,os,stat,subprocess
from pathlib import Path

HERE=Path(__file__).resolve().parent
BASE=Path('/Users/elinhaggstrom/nortropic-backups-20260910/full-20260910T103342Z/external')
REPO='Nortropic/nortropic-backups'
ROWS=[('scratchpad-refresh-20260910T195603Z.tar',2574610432,'e36549ff754265541ef9569c2b740ee1ca63303cd4893b9826386a23036aca6a',1313152963,'58bcc04b0a14c1ff90f8ef1faf7946d1487f07478f6e7a0a0a3c4f0b4c39e4ea'),
 ('scratchpad-refresh-20260910T202553Z.tar',3271506944,'c106845cf80c9d0657883183c00bc8256eecaedf8eab8d2a6727076ed05f54da',1665404714,'25d4c02522ae19ba45c1fa2d127561f19fed0a1e2801a218b693e04f01733799')]
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def ident(p):
 assert p.resolve()==p
 s=p.lstat();assert stat.S_ISREG(s.st_mode) and s.st_nlink==1 and s.st_uid==os.geteuid() and not s.st_flags
 return [s.st_dev,s.st_ino,s.st_mode,s.st_uid,s.st_gid,s.st_nlink,s.st_size,s.st_mtime_ns,s.st_ctime_ns]
def fid(s):return [s.st_dev,s.st_ino,s.st_mode,s.st_uid,s.st_gid,s.st_nlink,s.st_size,s.st_mtime_ns,s.st_ctime_ns]
def free():
 s=os.statvfs(BASE);return s.f_bavail*s.f_frsize
def api(path):
 r=subprocess.run(['/opt/homebrew/bin/gh','api',path],capture_output=True,check=True);assert not r.stderr;return json.loads(r.stdout)
def no_user(p):
 r=subprocess.run(['/usr/sbin/lsof','-nP','-Fpn',str(p)],capture_output=True)
 assert r.returncode==1 and not r.stdout and not r.stderr,('open file or lsof error',p.name)
def save(name,obj):
 with (HERE/name).open('x') as f:json.dump(obj,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())

assert BASE.resolve()==BASE and not (BASE/'.git').exists()
assert not (HERE/'large-raw-retirement-execution.jsonl').exists() and not (HERE/'large-raw-retirement-result.json').exists()
decision=HERE/'LARGE-RAW-REPRESENTATION-RETIREMENT.md';assert decision.is_file()
assert sha(decision)=='e3f5ad6db9e2142bc55b671b39add2e5d02281e670b9f655dc040e24035f298e'
rp=HERE/'large-external-concurrent-verify-r2-receipt.json'
receipt=json.loads(rp.read_bytes());manifest=json.loads((HERE/'large-external-manifest.json').read_bytes())
assert receipt['status']=='REMOTE_MULTIPART_ARCHIVE_RECONSTRUCTION_VERIFIED' and receipt['repo_id']==1367371291 and receipt['private'] is True
assert receipt['manifest_sha256']==sha(HERE/'large-external-manifest.json') and len(receipt['archives'])==2
repo=api('repos/'+REPO);assert repo['id']==1367371291 and repo['private'] is True
release=api('repos/'+REPO+'/releases/tags/backup-20260912-large-scratchpad-segments')
assert release['id']==receipt['release_id'] and not release['draft']
assets={a['name']:a for a in release['assets']};assert len(assets)==45
targets=[];remote=[];startfree=free()
commands=subprocess.run(['/bin/ps','-axo','command='],capture_output=True,check=True);assert not commands.stderr
for index,(name,size,digest,encoded_size,encoded_sha) in enumerate(ROWS):
 source=BASE/name;encoded=HERE/(name+'.local-representation.gz')
 assert str(source).encode() not in commands.stdout
 original_id=ident(source);encoded_id=ident(encoded);no_user(source)
 rec=receipt['archives'][index];plan=manifest['archives'][index]
 assert rec['path']==plan['path']=='external/'+name and rec['bytes']==plan['bytes']==size and rec['sha256']==plan['sha256']==digest and rec['source_unchanged'] is True
 assert len(rec['parts'])==len(plan['parts'])==(20 if index==0 else 25)
 offset=0
 for i,(actual,expected) in enumerate(zip(rec['parts'],plan['parts'],strict=True),1):
  assert all(actual[k]==expected[k] for k in ('name','bytes','sha256','offset')) and actual['exit']==0 and actual['stderr_bytes']==0
  assert actual['offset']==offset and actual['name']==name+'.part-%03d.raw'%i
  assert 0<actual['bytes']<=128*1024**2;offset+=actual['bytes']
  a=assets[actual['name']];assert a['id']==actual['asset_id'] and a['size']==actual['bytes'] and a['digest']=='sha256:'+actual['sha256'] and a['state']=='uploaded'
  remote.append({k:a[k] for k in ('id','name','size','digest','state')})
 assert offset==size and encoded.stat().st_size==encoded_size and sha(encoded)==encoded_sha
 count=0;h=hashlib.sha256()
 with source.open('rb') as original,gzip.open(encoded,'rb') as compressed:
  while chunk:=compressed.read(1024**2):
   assert original.read(len(chunk))==chunk;count+=len(chunk);h.update(chunk)
  assert not original.read(1)
 assert count==size and h.hexdigest()==digest and ident(source)==original_id and ident(encoded)==encoded_id
 targets.append(dict(source=str(source),bytes=size,sha256=digest,identity=original_id,encoded=str(encoded),encoded_bytes=encoded_size,encoded_sha256=encoded_sha,encoded_identity=encoded_id))
 print(json.dumps(dict(preflight=name,reconstruction='BYTE_EXACT')),flush=True)
assert {r['name'] for r in remote}==set(assets)
save('large-raw-retirement-preflight.json',dict(time_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),targets=targets,remote=remote,remote_receipt_sha256=sha(rp),decision_sha256=sha(decision),free_before=startfree,classification='REDUNDANT_RAW_REPRESENTATIONS_ONLY',filesystem_restore='NOT_RUN'))
with (HERE/'large-raw-retirement-execution.jsonl').open('x') as log:
 dfd=os.open(BASE,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW);parent=os.fstat(dfd)
 try:
  for t in targets:
   p=Path(t['source']);ep=Path(t['encoded']);no_user(p)
   assert ident(p)==t['identity'] and ident(ep)==t['encoded_identity'] and sha(ep)==t['encoded_sha256']
   fd=os.open(p.name,os.O_RDONLY|os.O_NOFOLLOW,dir_fd=dfd)
   try:
    assert fid(os.fstat(fd))==t['identity'];h=hashlib.sha256()
    while b:=os.read(fd,1024**2):h.update(b)
    assert h.hexdigest()==t['sha256'] and fid(os.fstat(fd))==t['identity']
    assert fid(os.stat(p.name,dir_fd=dfd,follow_symlinks=False))==t['identity'] and ident(ep)==t['encoded_identity']
    s=BASE.lstat();assert (s.st_dev,s.st_ino)==(parent.st_dev,parent.st_ino)
    log.write(json.dumps(dict(stage='BEFORE_UNLINK',**t))+'\n');log.flush();os.fsync(log.fileno())
    os.unlink(p.name,dir_fd=dfd);os.fsync(dfd)
    assert os.fstat(fd).st_nlink==0 and not p.exists()
   finally:os.close(fd)
   log.write(json.dumps(dict(stage='REMOVED',path=str(p),sha256=t['sha256']))+'\n');log.flush();os.fsync(log.fileno())
   print(json.dumps(dict(removed=p.name,bytes=t['bytes'])),flush=True)
 finally:os.close(dfd)
for t in targets:assert not Path(t['source']).exists() and ident(Path(t['encoded']))==t['encoded_identity']
after=free()
save('large-raw-retirement-result.json',dict(time_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='TWO_RAW_REPRESENTATIONS_RETIRED',removed=2,logical_bytes=sum(t['bytes'] for t in targets),retained_encoded_bytes=sum(t['encoded_bytes'] for t in targets),free_before=startfree,free_after=after,observed_free_delta=after-startfree,targets=targets,remote_receipt_sha256=sha(rp),decision_sha256=sha(decision),recovery='Decode each retained local gzip or concatenate its verified remote raw segments; require full raw hash/size.',filesystem_restore='NOT_RUN',bootstrap_credit=False))
print(json.dumps(dict(removed=2,free_after=after,observed_delta=after-startfree)),flush=True)
