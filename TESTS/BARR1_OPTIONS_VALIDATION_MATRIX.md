# BARR1["OPTIONS"] Validation Matrix v1.0

## Dictionary v1
- 01 = STANDARD
- 02 = VERIFIED

---

## A. Valid Cases

| ID  | Input                                | Expected Output                                      | Status |
|-----|--------------------------------------|------------------------------------------------------|--------|
| T01 | BARR1["OPTIONS"]=[01,02];            | ["STANDARD","VERIFIED"]                              | PASS   |
| T02 | BARR1["OPTIONS"]=[02,01];            | ["VERIFIED","STANDARD"]                              | PASS   |
| T03 | BARR1["OPTIONS"]=[01];               | ["STANDARD"]                                         | PASS   |
| T04 | BARR1["OPTIONS"]=[02];               | ["VERIFIED"]                                         | PASS   |
| T05 | BARR1["OPTIONS"]=[01,01,02];         | ["STANDARD","STANDARD","VERIFIED"]                   | PASS   |
| T06 | BARR1["OPTIONS"]=[02,02];            | ["VERIFIED","VERIFIED"]                              | PASS   |

---

## B. Unknown Handling

| ID  | Input                                | Expected Output                                      | Status            |
|-----|--------------------------------------|------------------------------------------------------|-------------------|
| T07 | BARR1["OPTIONS"]=[01,09,02];         | ["STANDARD","UNK_OPT1_09","VERIFIED"]                | PASS_WITH_UNKNOWN |
| T08 | BARR1["OPTIONS"]=[09,01];            | ["UNK_OPT1_09","STANDARD"]                          | PASS_WITH_UNKNOWN |
| T09 | BARR1["OPTIONS"]=[09,10];            | ["UNK_OPT1_09","UNK_OPT1_10"]                       | PASS_WITH_UNKNOWN |

---

## C. Invalid Structure

| ID  | Input                                | Reason                         | Status |
|-----|--------------------------------------|--------------------------------|--------|
| T10 | BARR1["RULE"]=[01,02];               | wrong field                    | FAIL   |
| T11 | BARR["OPTIONS"]=[01,02];             | missing version                | FAIL   |
| T12 | BARR1["OPTIONS"]="0102";             | scalar collapse                | FAIL   |
| T13 | BARR1["OPTIONS"]="01.02";            | invalid delimiter              | FAIL   |
| T14 | BARR1["OPTIONS"]=[1,2];              | invalid width                  | FAIL   |
| T15 | BARR1["OPTIONS"]=[OPT_STD];          | alias injection                | FAIL   |
| T16 | BARR1["OPTIONS"]=["STANDARD"];       | unpacked values                | FAIL   |
| T17 | BARR1["OPTIONS"]=[];                 | empty array invalid            | FAIL   |

---

## D. Invalid Decoder Behavior

| ID  | Input                                | Bad Behavior                   | Status |
|-----|--------------------------------------|--------------------------------|--------|
| T18 | [02,01]                              | sorted to [01,02]              | FAIL   |
| T19 | [01,01,02]                           | deduplicated                   | FAIL   |
| T20 | [01,09]                              | guessed value                  | FAIL   |
| T21 | [01,09,02]                           | dropped unknown                | FAIL   |
| T22 | [01,02]                              | wrong dictionary mapping       | FAIL   |

---

## Conformance Rule

A system is compliant only if:

- All PASS cases succeed exactly
- All PASS_WITH_UNKNOWN cases preserve unknowns correctly
- All FAIL cases are rejected or flagged
- No invalid behavior is observed

---

## Final Note

This matrix defines operational truth for BARR1["OPTIONS"].

If behavior deviates from this matrix, the implementation is non-compliant.
