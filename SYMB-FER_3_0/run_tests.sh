#!/bin/bash

PASS=0
FAIL=0

run_test() {
  local label=$1
  local file=$2
  local expected=$3

  echo "=== $label ==="
  output=$(python SYMB-FER_3_0/symbfer_engine.py "$file")
  echo "$output"

  if echo "$output" | grep -q "STATUS: $expected"; then
    echo "[ ASSERT PASS ] expected $expected"
    PASS=$((PASS + 1))
  else
    echo "[ ASSERT FAIL ] expected $expected"
    FAIL=$((FAIL + 1))
  fi
  echo
}

run_test "VALID"           SYMB-FER_3_0/tests/test_valid_3_0.txt       "WARN"
run_test "MISSING SECTION" SYMB-FER_3_0/tests/test_missing_section.txt "FAIL"
run_test "BAD SHA"         SYMB-FER_3_0/tests/test_bad_sha.txt         "FAIL"
run_test "BAD ORDER"       SYMB-FER_3_0/tests/test_bad_order.txt       "FAIL"
run_test "VALID V2"        SYMB-FER_3_0/tests/test_valid_v2.txt        "WARN"

echo "=== RESULTS: $PASS passed · $FAIL failed ==="
[ $FAIL -eq 0 ] && exit 0 || exit 1
