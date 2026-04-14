#!/bin/bash

echo "=== VALID ==="
python SYMB-FER_3_0/symbfer_engine.py SYMB-FER_3_0/tests/test_valid_3_0.txt
echo

echo "=== MISSING SECTION ==="
python SYMB-FER_3_0/symbfer_engine.py SYMB-FER_3_0/tests/test_missing_section.txt
echo

echo "=== BAD SHA ==="
python SYMB-FER_3_0/symbfer_engine.py SYMB-FER_3_0/tests/test_bad_sha.txt
echo

echo "=== BAD ORDER ==="
python SYMB-FER_3_0/symbfer_engine.py SYMB-FER_3_0/tests/test_bad_order.txt
echo
