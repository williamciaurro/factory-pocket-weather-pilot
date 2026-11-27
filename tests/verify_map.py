from pathlib import Path
root = Path(__file__).resolve().parents[1]
assert {str(p.relative_to(root)).replace(chr(92), '/') for p in (root / '.github').rglob('*')} == {
    '.github/pull_request_template.md', '.github/workflows', '.github/workflows/verify.yml'}
text = (root / 'README.md').read_text(encoding='utf-8')
entry = '- `.github/` — [pull request template](.github/pull_request_template.md).'
assert text.splitlines().count(entry) == 1
assert (root / '.github/pull_request_template.md').is_file()
