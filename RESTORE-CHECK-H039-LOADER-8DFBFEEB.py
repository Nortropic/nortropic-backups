"""Read-only reconstruction of the six downloaded files. Never executes project code."""
import datetime, hashlib, json, re, subprocess
from pathlib import Path

catalogue = Path(__file__).resolve().parent
selection = json.loads((catalogue / 'H039-LOADER-8DFBFEEB-SELECTION.json').read_bytes())
receipt = json.loads((catalogue / 'H039-LOADER-8DFBFEEB-RESTORE.json').read_bytes())
restored = Path(receipt['restored'])
base = '/private/tmp/nortropic-h039-verifier-py39-D-restore-3jifhdp2'
candidate = Path('/Users/elinhaggstrom/nortropic-repos/work/test-author-h039-loader-D571a47b8-20260913')
patch_source = Path('/Users/elinhaggstrom/nortropic/evidence/v316-h039-continuity-review-20260912/h039-loader-before-native-8dfbfeeb.patch')
patch = (restored / str(patch_source).lstrip('/')).read_bytes()
assert hashlib.sha256(patch).hexdigest() == 'c6fb74759f76809a34221986a953831ecada9ba0bc4a2f9fd67ffced65b273b5'

commands = []
def git(repo, *args):
    argv = ['/usr/bin/git', '-C', str(repo), *args]
    r = subprocess.run(argv, capture_output=True, timeout=30)
    commands.append(dict(argv=argv, exit=r.returncode, stderr_bytes=len(r.stderr)))
    assert r.returncode == 0 and not r.stderr
    return r.stdout

assert git(candidate, 'diff', '--full-index', 'HEAD') == patch
assert git(base, 'rev-parse', 'HEAD').decode().strip() == selection['base_commit']
assert git(base, 'rev-parse', 'HEAD^{tree}').decode().strip() == selection['base_tree']
expected = {str(Path(r['path']).relative_to(candidate)): r for r in selection['rows'][:6]}
seen, rows = set(), []
parts = patch.split(b'diff --git ')
assert parts[0] == b''
for part in parts[1:]:
    lines = part.splitlines(keepends=True)
    left, right = lines[0].decode().strip().split(' ')
    name = left[2:]
    assert left == 'a/' + name and right == 'b/' + name and name in expected and name not in seen
    seen.add(name)
    original = git(base, 'show', selection['base_commit'] + ':' + name).splitlines(keepends=True)
    output, position, i, hunks = [], 0, 1, 0
    while i < len(lines):
        if not lines[i].startswith(b'@@ '):
            assert lines[i].startswith((b'index ', b'--- ', b'+++ '))
            i += 1
            continue
        match = re.match(rb'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@', lines[i])
        assert match
        start = int(match[1]) - 1
        old_count, new_count = int(match[2] or b'1'), int(match[4] or b'1')
        assert start >= position
        output.extend(original[position:start])
        position, i, used, added = start, i + 1, 0, 0
        while i < len(lines) and not lines[i].startswith(b'@@ '):
            line = lines[i]
            assert line[:1] in (b' ', b'+', b'-')
            if line[:1] in (b' ', b'-'):
                assert original[position] == line[1:]
                position += 1
                used += 1
            if line[:1] in (b' ', b'+'):
                output.append(line[1:])
                added += 1
            i += 1
        assert (used, added) == (old_count, new_count)
        hunks += 1
    output.extend(original[position:])
    result, row = b''.join(output), expected[name]
    archived = (restored / row['path'].lstrip('/')).read_bytes()
    assert result == archived == Path(row['path']).read_bytes()
    assert hashlib.sha256(result).hexdigest() == row['sha256']
    rows.append(dict(path=name, hunks=hunks, sha256=row['sha256'], bytes=len(result)))
assert seen == set(expected)
for row in selection['rows']:
    assert hashlib.sha256(Path(row['path']).read_bytes()).hexdigest() == row['sha256']
assert not git(candidate, 'diff', '--cached', '--name-only')
print(json.dumps(dict(
    time_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    status='SIX_DOWNLOADED_FILES_AND_PATCH_RECONSTRUCTED_FROM_PRIOR_RESTORED_D_GIT_OBJECTS',
    base_commit=selection['base_commit'], base_tree=selection['base_tree'], base_object_source=base,
    patch_sha256=hashlib.sha256(patch).hexdigest(), rows=rows, commands=commands,
    all_28_original_files_still_match_selection=True, staging_empty=True,
    originals_written=False, project_code_executed=False, runtime_credit=False,
    full_new_remote_base_delta_restore=False,
    earlier_diagnostic='289126 stopped at textual git-diff comparison before reconstruction. 7330ac proved only short versus full index headers (396 bytes for six files). Corrected comparison uses --full-index; archived/source bytes were unchanged.'
), indent=2))
