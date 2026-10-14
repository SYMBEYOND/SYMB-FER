# SYMB-FER v6.2 Validator

Validates SYMB-FER v6.2 tokens.

## Usage

```bash
python3 validate_v6_2.py <path-to-token.txt>
```

Exit code 0 on PASS or WARN, exit code 1 on FAIL.

## Validation Rules

1. **UTF-8 encoding**: Token must be valid UTF-8
2. **Section structure**: All §NAME·BEGIN/END pairs must match with proper nesting (only REFER·TRIGGER, TIMESTAMP·CALIBRATION, TIME·ANCHOR allowed inside BOOT·PROTOCOL)
3. **Required sections**: All 33 sections must be present (including nested sections)
4. **Section order**: Sections must appear in template order (WARN if different, doesn't FAIL)
5. **Version consistency**: Header line, §META FORMAT, and TOKEN·TRACK must all say v6.2
6. **SHA256 format**: Must be 64 lowercase hex chars or blank (blank is WARN)
7. **Delimiter integrity**: Must contain middle-dot (U+00B7) delimiters

## Tests

```bash
bash run_tests.sh
```

Tests cover: valid token, missing section, unmatched END, bad SHA256, version mismatch.
