#!/bin/bash

PASS=0
FAIL=0

run_test() {
  local label=$1
  local file=$2
  local expected=$3

  echo "=== $label ==="
  output=$(python3 SYMB-FER_6_2/validate_v6_2.py "$file")
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

run_test "VALID"                  SYMB-FER_6_2/tests/test_valid_v6_2.txt              "PASS"
run_test "SHA PENDING"            SYMB-FER_6_2/tests/test_sha_pending.txt             "WARN"
run_test "MISSING SECTION"        SYMB-FER_6_2/tests/test_missing_section.txt         "FAIL"
run_test "UNMATCHED END"          SYMB-FER_6_2/tests/test_unmatched_end.txt           "FAIL"
run_test "BAD SHA"                SYMB-FER_6_2/tests/test_bad_sha.txt                 "FAIL"
run_test "VERSION MISMATCH"       SYMB-FER_6_2/tests/test_version_mismatch.txt        "FAIL"
run_test "SECTION ORDER"          SYMB-FER_6_2/tests/test_section_order.txt           "WARN"
run_test "NOTATION OPTIONAL"      SYMB-FER_6_2/tests/test_notation_optional.txt       "PASS"
run_test "SHA IN SIG ONLY"        SYMB-FER_6_2/tests/test_sha_in_sig_only.txt         "FAIL"
run_test "NESTED TOP LEVEL"       SYMB-FER_6_2/tests/test_nested_top_level.txt        "FAIL"
run_test "VERSION 6.20"           SYMB-FER_6_2/tests/test_version_6_20.txt            "FAIL"
run_test "MISSING REFER TRIGGER"  SYMB-FER_6_2/tests/test_missing_refer_trigger.txt    "FAIL"
run_test "MISSING TIMESTAMP"      SYMB-FER_6_2/tests/test_missing_timestamp_calibration.txt "FAIL"
run_test "MISSING TIME ANCHOR"    SYMB-FER_6_2/tests/test_missing_time_anchor.txt      "FAIL"

echo "=== RESULTS: $PASS passed · $FAIL failed ==="
[ $FAIL -eq 0 ] && exit 0 || exit 1
