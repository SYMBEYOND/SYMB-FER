# SYMB-FER Engine

SYMB-FER Engine validates and loads canonical SYMB-FER 3.0 artifacts.

## What it does

- validates required sections
- validates canonical section order
- validates required rule lines
- validates delimiter integrity
- validates signature block shape
- allows blank SHA256 as a warning
- rejects malformed SHA256
- reconstructs deterministic runtime state from valid artifacts

## Usage

From repo root:

```bash
python SYMB-FER_3_0/symbfer_engine.py your_token.txt
```

Output returns one of three states:

- `PASS` — fully valid
- `WARN` — valid with non-blocking issues (e.g. empty SHA256)
- `FAIL` — invalid artifact

## Diff Mode

Compare two tokens and report structural differences:

```bash
python SYMB-FER_3_0/symbfer_engine.py --diff token_a.txt token_b.txt
```

## Test Suite

```bash
bash SYMB-FER_3_0/run_tests.sh
```

All four fixtures must pass assertions. Exit code 0 = all pass. Exit code 1 = failures detected.
