"""Finite concurrent readback of exactly the 45 declared segments as uploaded.
No upload/retry/extraction or deletion. At most 15 minutes waiting per part.
"""
import datetime,hashlib,json,subprocess,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
BASE=Path('/Users/elinhaggstrom/nortropic-backups-20260910/full-20260910T103342Z')
REMOTE='Nortropic/nortropic-backups';TAG='backup-20260912-large-scratchpad-segments'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def ident(p):
 s=p.stat();return [s.st_dev,s.st_ino,s.st_mode,s.st_size,s.st_mtime_ns,s.st_ctime_ns]
def api(p):return json.loads(subprocess.check_output(['gh','api',p]))
mp=HERE/'large-external-manifest.json';manifest_sha=sha(mp);m=json.loads(mp.read_text())
assert len(m['archives'])==2 and sum(len(r['parts']) for r in m['archives'])==45
repo=api('repos/'+REMOTE);assert repo['id']==1367371291 and repo['private'] is True
rel=api('repos/'+REMOTE+'/releases/tags/'+TAG);assert not rel['draft']
results=[]
for r in m['archives']:
 source=BASE/r['path'];assert ident(source)==r['identity'] and sha(source)==r['sha256']
 before=ident(source);full=hashlib.sha256();offset=0;parts=[]
 with source.open('rb') as original:
  for i,p in enumerate(r['parts'],1):
   assert p['offset']==offset and p['name']==source.name+'.part-%03d.raw'%i and 0<p['bytes']<=128*1024**2
   response_path=HERE/(p['name']+'.upload-response.json');deadline=time.monotonic()+900
   while True:
    try:uploaded=json.loads(response_path.read_text());break
    except (FileNotFoundError,json.JSONDecodeError):
     assert time.monotonic()<deadline,('upload receipt wait expired',p['name']);time.sleep(2)
   assert uploaded['exit']==0
   asset=api('repos/'+REMOTE+'/releases/assets/'+str(uploaded['response']['id']))
   assert asset['name']==p['name'] and asset['size']==p['bytes'] and asset['digest']=='sha256:'+p['sha256'] and asset['state']=='uploaded'
   cmd=['gh','release','download',TAG,'--repo',REMOTE,'--pattern',p['name'],'--output','-']
   err=HERE/(p['name']+'.concurrent-verify.stderr');print(json.dumps(dict(downloading=p['name'])),flush=True)
   with err.open('xb') as e:
    proc=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=e);h=hashlib.sha256();size=0
    try:
     while b:=proc.stdout.read(1024**2):
      assert size+len(b)<=p['bytes'] and original.read(len(b))==b
      size+=len(b);h.update(b);full.update(b)
     assert proc.wait()==0 and err.stat().st_size==0
    finally:
     proc.stdout.close()
     if proc.poll() is None:proc.terminate();proc.wait()
   assert size==p['bytes'] and h.hexdigest()==p['sha256'];offset+=size
   row=dict(name=p['name'],offset=p['offset'],bytes=size,sha256=h.hexdigest(),asset_id=asset['id'],command=cmd,exit=0,stderr_bytes=0)
   parts.append(row)
   with (HERE/'large-external-concurrent-verify-progress.jsonl').open('a') as f:f.write(json.dumps(row)+'\n')
   print(json.dumps(dict(verified=p['name'],bytes=size)),flush=True)
  assert not original.read(1)
 assert offset==r['bytes'] and full.hexdigest()==r['sha256'] and ident(source)==before
 results.append(dict(path=r['path'],bytes=offset,sha256=full.hexdigest(),parts=parts,source_unchanged=True))
assert sha(mp)==manifest_sha
final=api('repos/'+REMOTE+'/releases/tags/'+TAG)
assert final['id']==rel['id'] and not final['draft'] and {a['name'] for a in final['assets']}=={p['name'] for r in m['archives'] for p in r['parts']}
receipt=dict(time_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),repo=REMOTE,repo_id=repo['id'],private=True,release_id=rel['id'],release_tag=TAG,archives=results,manifest_sha256=manifest_sha,status='REMOTE_MULTIPART_ARCHIVE_RECONSTRUCTION_VERIFIED',filesystem_restore='NOT_RUN',deleted=False,runtime_credit=False)
with (HERE/'large-external-concurrent-verify-receipt.json').open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
