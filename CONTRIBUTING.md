# Contributing

## Good fits

- New synthetic layout presets
- Locale packs for fake dates/currency
- CLI flags and reproducibility tests

## Rules

- Never include real customer PII
- Keep SYNTHETIC labels visible
- Prefer small PRs

```bash
python -m venv .venv
.venv/bin/pip install -e ".[test]"
.venv/bin/pytest -q
```
