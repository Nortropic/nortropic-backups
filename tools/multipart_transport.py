"""Lossless two-part gzip transport of the exact reviewed tar, not filesystem restore.
Use the existing unchanged gzip prefix as a named PART, never a complete archive.
No original writes, cleanup, archived code execution or product operations.
"""
import gzip,hashlib,io,json,os,subprocess,sys,zlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
REPO=Path('/Users/elinhaggstrom/nortropic-backups-20260910/github-transfer-20260912.dVjQlj/repo')
TAG='backup-20260912-main-archive-multipart'
def verify_parts(manifest,names,opener,original=None):
    parts=manifest['parts']
    assert names==[p['name'] for p in parts] and len(set(names))==len(names)
    offset=0;whole=hashlib.sha256();results=[]
    for part in parts:
        assert part['offset']==offset and part['raw_bytes']>0
        assert Path(part['name']).name==part['name'] and part['compressed_bytes']<2*1024**3
        compressed=hashlib.sha256();raw=hashlib.sha256();nc=nr=0;decoder=zlib.decompressobj(31)
        with opener(part['name']) as stream:
            while chunk:=stream.read(1024**2):
                compressed.update(chunk);nc+=len(chunk);assert nc<=part['compressed_bytes']
                pending=chunk
                while pending:
                    data=decoder.decompress(pending,min(8*1024**2,part['raw_bytes']-nr+1))
                    assert not decoder.unused_data
                    pending=decoder.unconsumed_tail
                    nr+=len(data);assert nr<=part['raw_bytes']
                    raw.update(data);whole.update(data)
                    if original is not None:assert data==original.read(len(data))
        assert decoder.eof and nc==part['compressed_bytes'] and nr==part['raw_bytes']
        assert compressed.hexdigest()==part['compressed_sha256'] and raw.hexdigest()==part['raw_sha256']
        results.append({'name':part['name'],'compressed_bytes':nc,'raw_bytes':nr,'verified':True})
        offset+=nr
    assert offset==manifest['raw_bytes'] and whole.hexdigest()==manifest['raw_sha256']
    if original is not None:assert not original.read(1)
    return results
def selftest():
    rawparts=[b'first-test-part\x00'*11,b'last-test-part\xff'*13]
    files={str(i)+'.gz':gzip.compress(d,mtime=0) for i,d in enumerate(rawparts)}
    m={'raw_bytes':sum(map(len,rawparts)),'raw_sha256':hashlib.sha256(b''.join(rawparts)).hexdigest(),'parts':[]}
    off=0
    for name,d in zip(files,rawparts):
        m['parts'].append({'name':name,'offset':off,'raw_bytes':len(d),'raw_sha256':hashlib.sha256(d).hexdigest(),'compressed_bytes':len(files[name]),'compressed_sha256':hashlib.sha256(files[name]).hexdigest()});off+=len(d)
    names=list(files);verify_parts(m,names,lambda n:io.BytesIO(files[n]),io.BytesIO(b''.join(rawparts)))
    cases=[]
    for case in ('missing','reordered','duplicate','altered','truncated','extra_bytes','wrong_offset','wrong_full_hash','wrong_original'):
        mm=json.loads(json.dumps(m));ff=dict(files);nn=list(names);original=None
        if case=='missing':nn=nn[:-1]
        elif case=='reordered':nn.reverse()
        elif case=='duplicate':nn=[nn[0],nn[0]]
        elif case=='altered':ff[nn[0]]=ff[nn[0]][:-1]+bytes([ff[nn[0]][-1]^1])
        elif case=='truncated':ff[nn[0]]=ff[nn[0]][:-5]
        elif case=='extra_bytes':ff[nn[1]]+=b'extra'
        elif case=='wrong_offset':mm['parts'][1]['offset']+=1
        elif case=='wrong_full_hash':mm['raw_sha256']='0'*64
        elif case=='wrong_original':original=io.BytesIO(b'wrong')
        try:verify_parts(mm,nn,lambda n:io.BytesIO(ff[n]),original)
        except (AssertionError,zlib.error):cases.append({'case':case,'rejected':True})
        else:raise AssertionError(case+' was accepted')
    return {'positive':1,'negative':cases,'actual_callable':'verify_parts','archived_code_executed':False}
def free():
    s=os.statvfs(HERE);return s.f_bavail*s.f_frsize
def build():
    test=selftest();review=json.loads((REPO/'MAIN-CONTENT-REVIEW.json').read_text())
    source=Path(review['source']);before=source.stat();prefix=review['incomplete_transport'];first=Path(prefix['path'])
    with first.open('rb') as f:assert hashlib.file_digest(f,'sha256').hexdigest()==prefix['sha256']
    assert first.stat().st_size==prefix['bytes'] and free()>16*1024**3
    second=HERE/'nortropic-full-20260910T103342Z.part-002.tar-segment.gz'
    raw_hash=hashlib.sha256();raw_count=0
    with source.open('rb') as src,second.open('xb') as dst:
        os.chmod(second,0o600);src.seek(prefix['decoded_prefix_bytes'])
        with gzip.GzipFile(filename='',mode='wb',fileobj=dst,compresslevel=6,mtime=0) as out:
            while data:=src.read(4*1024**2):
                raw_hash.update(data);raw_count+=len(data);out.write(data)
                assert dst.tell()<1024**3 and free()>15.5*1024**3
                if raw_count%(256*1024**2)==0:print(json.dumps({'suffix_raw_bytes':raw_count,'suffix_encoded_bytes':dst.tell()}),flush=True)
        dst.flush();os.fsync(dst.fileno())
    with second.open('rb') as f:encoded_hash=hashlib.file_digest(f,'sha256').hexdigest()
    m={'repo':'Nortropic/nortropic-backups','repo_id':1367371291,'release_tag':TAG,
       'source':str(source),'raw_bytes':review['source_bytes'],'raw_sha256':review['source_sha256'],
       'parts':[{'name':first.name,'local_path':str(first),'offset':0,'raw_bytes':prefix['decoded_prefix_bytes'],'raw_sha256':prefix['decoded_prefix_sha256'],'compressed_bytes':prefix['bytes'],'compressed_sha256':prefix['sha256']},
                {'name':second.name,'local_path':str(second),'offset':prefix['decoded_prefix_bytes'],'raw_bytes':raw_count,'raw_sha256':raw_hash.hexdigest(),'compressed_bytes':second.stat().st_size,'compressed_sha256':encoded_hash}],
       'encoding':'Two independent single-member gzip segments; concatenate DECOMPRESSED bytes in manifest order to recover exact original tar',
       'prefix_history':'Unchanged previously incomplete compression output is ONLY part 1. Its failed attempt remains incomplete; whole-archive credit requires BOTH parts and whole hash.',
       'content_review_sha256':hashlib.sha256((REPO/'MAIN-CONTENT-REVIEW.json').read_bytes()).hexdigest(),
       'selftest':test,'remote_status':'NOT_UPLOADED','filesystem_restore':'NOT_RUN'}
    files={x['name']:Path(x['local_path']) for x in m['parts']}
    with source.open('rb') as original:result=verify_parts(m,list(files),lambda n:files[n].open('rb'),original)
    after=source.stat();assert (before.st_dev,before.st_ino,before.st_size,before.st_mtime_ns,before.st_ctime_ns)==(after.st_dev,after.st_ino,after.st_size,after.st_mtime_ns,after.st_ctime_ns)
    m['local_verification']=result;m['source_unchanged']=True;m['free_bytes_after']=free()
    with (HERE/'main-multipart-manifest.json').open('x') as f:json.dump(m,f,indent=2)
    print(json.dumps({'local_parts_verified':len(result),'encoded_bytes':sum(x['compressed_bytes'] for x in m['parts']),'free_bytes':free()}))
if __name__=='__main__':
    assert sys.argv[1:] in (['test'],['build'])
    if sys.argv[1]=='test':print(json.dumps(selftest()))
    else:build()
