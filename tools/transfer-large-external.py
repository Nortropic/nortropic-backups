"""Two reviewed large archives, fixed raw segments, no local segment files.
Uses the configured gh CLI, not extracted credentials. No extraction/deletion.
"""
import copy,datetime,hashlib,io,json,os,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
BASE=Path('/Users/elinhaggstrom/nortropic-backups-20260910/full-20260910T103342Z')
REMOTE='Nortropic/nortropic-backups'
TAG='backup-20260912-large-scratchpad-segments'
NAMES=('external/scratchpad-refresh-20260910T195603Z.tar','external/scratchpad-refresh-20260910T202553Z.tar')
CHUNK=128*1024**2
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def ident(p):
 s=p.stat();return [s.st_dev,s.st_ino,s.st_mode,s.st_size,s.st_mtime_ns,s.st_ctime_ns]
def save(name,x):
 with (HERE/name).open('x') as f:json.dump(x,f,indent=2);f.write('\n')
def api(path):return json.loads(subprocess.check_output(['gh','api',path]))
def chunks(f,size):
 remaining=size
 while remaining:
  b=f.read(min(1024**2,remaining))
  if not b:raise ValueError('truncated source')
  remaining-=len(b);yield b
def validate(row):
 assert row['path'] in NAMES and row['bytes']>2**31
 offset=0;names=set()
 for i,p in enumerate(row['parts'],1):
  assert p['offset']==offset and p['bytes']==min(CHUNK,row['bytes']-offset)>0
  assert p['name']==Path(row['path']).name+'.part-%03d.raw'%i and p['name'] not in names
  assert len(p['sha256'])==64 and all(c in '0123456789abcdef' for c in p['sha256'])
  offset+=p['bytes'];names.add(p['name'])
 assert offset==row['bytes']
def reviewed_rows():
 review=json.loads((HERE/'external-archive-review.json').read_text())
 g=json.loads((HERE/'external-git-review.json').read_text())
 n=json.loads((HERE/'flagged-content-review.json').read_text())
 assert g['fsck_exit']==0 and not g['findings'] and g['source_archives_unchanged']
 assert len(g['nested'])==1 and g['nested'][0]['sha256']==n['nested_archive']['sha256']=='2d8cbc39da762cc088ff170de24e9f3f2513de6c8ae58ba6003f4e34abc6e20d'
 assert n['nested_archive']['regular_count']==21
 rows=[r for r in review['archives'] if r['path'] in NAMES]
 assert len(rows)==2
 for r in rows:assert r['issues'] and all(i['reason']=='UNREVIEWED_GIT_PACK' and i['sha256'] in g['packs'] for i in r['issues'])
 return rows
def main(mode):
 assert mode in ('prepare','upload','verify','selftest')
 if mode=='selftest':
  data=b'abcdef';assert b''.join(chunks(io.BytesIO(data),6))==data
  try:list(chunks(io.BytesIO(data),7))
  except ValueError:pass
  else:raise AssertionError('truncation accepted')
  assert b''.join(chunks(io.BytesIO(data),3))==b'abc'
  row=dict(path=NAMES[0],bytes=2**31+1,parts=[])
  for off in range(0,row['bytes'],CHUNK):row['parts'].append(dict(name=Path(row['path']).name+'.part-%03d.raw'%(len(row['parts'])+1),offset=off,bytes=min(CHUNK,row['bytes']-off),sha256='a'*64))
  validate(row)
  mutations=[lambda r:r['parts'].pop(),lambda r:r['parts'].reverse(),lambda r:r['parts'][0].update(offset=1),lambda r:r['parts'][0].update(bytes=0),lambda r:r['parts'][0].update(name='../bad'),lambda r:r['parts'][0].update(sha256='x'*64),lambda r:r.update(bytes=r['bytes']+1),lambda r:r['parts'].append(r['parts'][-1])]
  for m in mutations:
   bad=copy.deepcopy(row);m(bad)
   try:validate(bad)
   except AssertionError:pass
   else:raise AssertionError('invalid plan accepted')
  save('large-external-selftests.json',dict(positive=3,negative=9,exit=0,scope='actual chunk reader and partition validator; not remote or runtime credit'))
  print('3 positive / 9 negative actual-helper checks PASS');return
 if mode=='prepare':
  results=[]
  for r in reviewed_rows():
   source=BASE/r['path'];before=ident(source);h=hashlib.sha256();parts=[]
   with source.open('rb') as f:
    for offset in range(0,r['bytes'],CHUNK):
     size=min(CHUNK,r['bytes']-offset);ph=hashlib.sha256()
     for b in chunks(f,size):ph.update(b);h.update(b)
     parts.append(dict(name=source.name+'.part-%03d.raw'%(len(parts)+1),offset=offset,bytes=size,sha256=ph.hexdigest()))
    assert not f.read(1)
   assert h.hexdigest()==r['sha256'] and ident(source)==before
   row=dict(path=r['path'],bytes=r['bytes'],sha256=r['sha256'],identity=before,parts=parts);validate(row);results.append(row)
  save('large-external-manifest.json',dict(archives=results,encoding='raw consecutive segments; concatenate in numbered order per archive',review_sha256=sha(HERE/'external-archive-review.json'),git_review_sha256=sha(HERE/'external-git-review.json'),nested_review_sha256=sha(HERE/'flagged-content-review.json')))
  print('prepared',sum(len(r['parts']) for r in results),'segments without local payload copies');return
 manifest=json.loads((HERE/'large-external-manifest.json').read_text());rows=manifest['archives']
 assert len(rows)==2 and {r['path'] for r in rows}==set(NAMES)
 for key,name in [('review_sha256','external-archive-review.json'),('git_review_sha256','external-git-review.json'),('nested_review_sha256','flagged-content-review.json')]:assert manifest[key]==sha(HERE/name)
 reviewed_rows()
 for r in rows:validate(r);assert ident(BASE/r['path'])==r['identity'] and sha(BASE/r['path'])==r['sha256']
 repo=api('repos/'+REMOTE);assert repo['id']==1367371291 and repo['private'] is True
 if mode=='upload':
  cmd=['gh','release','create',TAG,'--repo',REMOTE,'--target','main','--latest=false','--title','Two historical scratchpad archives, raw multipart backup','--notes','Consecutive numbered raw segments. Reassemble using LARGE-EXTERNAL-MANIFEST.json; verify every segment and full archive hash. No filesystem restoration or runtime credit.']
  p=subprocess.run(cmd,capture_output=True,text=True);save('large-external-create.json',dict(command=cmd,exit=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0
 rel=api('repos/'+REMOTE+'/releases/tags/'+TAG);assert not rel['draft']
 assets={a['name']:a for a in rel['assets']}
 if mode=='upload':assert not assets
 else:assert set(assets)=={p['name'] for r in rows for p in r['parts']}
 results=[]
 for r in rows:
  source=BASE/r['path'];before=ident(source);full=hashlib.sha256();partresults=[]
  with source.open('rb') as f:
   for part in r['parts']:
    name=part['name'];ph=hashlib.sha256();size=0
    err=HERE/(name+'.'+mode+'.stderr')
    print(json.dumps(dict(mode=mode,part=name)),flush=True)
    if mode=='upload':
     url='https://uploads.github.com/repos/'+REMOTE+'/releases/'+str(rel['id'])+'/assets?name='+name
     cmd=['gh','api',url,'--method','POST','--input','-','-H','Content-Type: application/octet-stream','-H','Content-Length: '+str(part['bytes'])]
     with err.open('xb') as e:
      proc=subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=e)
      try:
       for b in chunks(f,part['bytes']):proc.stdin.write(b);ph.update(b);full.update(b);size+=len(b)
       proc.stdin.close();body=proc.stdout.read();rc=proc.wait()
      finally:
       if proc.poll() is None:proc.terminate();proc.wait()
       proc.stdout.close()
     save(name+'.upload-response.json',dict(command=cmd,exit=rc,response=json.loads(body) if rc==0 else None,stderr_file=str(err)))
     assert rc==0 and err.stat().st_size==0
     asset=json.loads(body)
    else:
     asset=assets[name];cmd=['gh','release','download',TAG,'--repo',REMOTE,'--pattern',name,'--output','-']
     with err.open('xb') as e:
      proc=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=e)
      try:
       while b:=proc.stdout.read(1024**2):
        assert size+len(b)<=part['bytes'] and f.read(len(b))==b
        ph.update(b);full.update(b);size+=len(b)
       assert proc.wait()==0 and err.stat().st_size==0
      finally:
       proc.stdout.close()
       if proc.poll() is None:proc.terminate();proc.wait()
    assert asset['name']==name and asset['state']=='uploaded' and asset['size']==size==part['bytes'] and asset['digest']=='sha256:'+ph.hexdigest()=='sha256:'+part['sha256']
    result=dict(name=name,asset_id=asset['id'],bytes=size,sha256=ph.hexdigest(),offset=part['offset'],command=cmd,exit=0,stderr_bytes=0)
    partresults.append(result)
    with (HERE/('large-external-'+mode+'-progress.jsonl')).open('a') as log:log.write(json.dumps(result)+'\n')
   assert not f.read(1)
  assert full.hexdigest()==r['sha256'] and ident(source)==before
  results.append(dict(path=r['path'],bytes=r['bytes'],sha256=full.hexdigest(),parts=partresults,source_unchanged=True))
 save('large-external-'+mode+'-receipt.json',dict(time_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),repo=REMOTE,repo_id=repo['id'],private=True,release_id=rel['id'],release_tag=TAG,archives=results,manifest_sha256=sha(HERE/'large-external-manifest.json'),status='REMOTE_MULTIPART_ARCHIVE_RECONSTRUCTION_VERIFIED' if mode=='verify' else 'UPLOADED_NOT_REMOTE_VERIFIED',filesystem_restore='NOT_RUN',deleted=False,runtime_credit=False))
if __name__=='__main__':main(sys.argv[1])
