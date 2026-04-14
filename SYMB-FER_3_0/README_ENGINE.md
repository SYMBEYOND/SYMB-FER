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
python SYMB-FER_3_0/symbfer_engine.py SYMB-FER_3_0/tests/test_valid_3_0.txt
