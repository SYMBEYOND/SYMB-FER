# BARR1["OPTIONS"] Conformance Specification v1.1

## 1. Record Definition

A valid packed record is defined as:

```text
BARR1["OPTIONS"]=[<code>,<code>,...];
Requirements
Record type MUST be exactly BARR1
Field name MUST be exactly "OPTIONS"
Payload MUST be an ordered array
Each element MUST be a two-digit numeric code
Array brackets MUST be present
Elements MUST be comma-separated
2. Dictionary v1 (Normative)

The dictionary for BARR1 version 1 is:

01 = STANDARD
02 = VERIFIED
Requirements
Implementations MUST use this exact mapping
Implementations MUST NOT redefine these codes
Implementations MUST NOT infer meanings for undefined codes
3. Encoding Requirements

Encoding from:

ARR["OPTIONS"]=[...];

to:

BARR1["OPTIONS"]=[...];
MUST
Preserve element order exactly
Preserve duplicates exactly
Map each value using Dictionary v1
Reject any value without a canonical mapping
MUST NOT
Sort elements
Remove duplicates
Substitute synonyms
Encode values outside the dictionary
Collapse array into scalar form
4. Decoding Requirements

Given:

BARR1["OPTIONS"]=[...];
MUST
Decode known codes exactly to canonical values
Preserve element order
Preserve duplicates
Output primary form as:
ARR["OPTIONS"]=[...];
MUST NOT
Sort elements
Deduplicate elements
Collapse array into scalar
Substitute inferred meanings
5. Unknown Code Handling

For any code not defined in Dictionary v1:

MUST
Preserve position
Represent as opaque placeholder:
UNK_OPT1_<code>
Example
Input:
BARR1["OPTIONS"]=[01,09,02];

Output:
ARR["OPTIONS"]=["STANDARD","UNK_OPT1_09","VERIFIED"];
MUST NOT
Guess meaning
Drop unknown values
Replace with null or empty values
6. Empty Array Policy
BARR1["OPTIONS"]=[]
MUST
Be treated as invalid
7. Order Preservation
MUST
Preserve array order exactly during encode and decode
Example
[02,01] ≠ [01,02]
MUST NOT
Sort elements under any condition
8. Duplicate Preservation
MUST
Preserve duplicates exactly
Example
[01,01,02] → ["STANDARD","STANDARD","VERIFIED"]
MUST NOT
Deduplicate values
9. Structural Validity Rules

The following are invalid:

BARR1["RULE"]=[01,02];
BARR["OPTIONS"]=[01,02];
BARR1["OPTIONS"]="0102";
BARR1["OPTIONS"]="01.02";
BARR1["OPTIONS"]=[1,2];
BARR1["OPTIONS"]=[OPT_STD];
BARR1["OPTIONS"]=["STANDARD"];
MUST
Reject these forms as invalid
10. Version Compliance
MUST
Interpret BARR1 under Dictionary v1 only
Reject or flag decoding under mismatched dictionary
MUST NOT
Apply alternate dictionary mappings
Allow silent dictionary substitution
11. Round-Trip Requirement

A compliant system MUST support:

ARR → BARR1 → ARR

with:

identical order
identical values
identical duplicates
identical unknown placeholders, if present

Failure to round-trip exactly is non-compliant.

12. Compliance Levels
Level 1. Structural Compliance
Accepts and preserves BARR1["OPTIONS"] structure
Level 2. Decode Compliance
Correctly decodes Dictionary v1
Level 3. Full Compliance
Passes full round-trip with no drift

Only Level 3 is considered fully compliant.

13. Error Classification

Implementations MUST classify outcomes as:

VALID
VALID_WITH_UNKNOWN
INVALID_STRUCTURE
INVALID_BEHAVIOR
INVALID_CONFIGURATION
14. Prohibited Behaviors

Implementations MUST NOT:

Sort elements
Deduplicate elements
Guess unknown codes
Drop unknown codes
Normalize scalar forms
Substitute aliases
Decode without version match
15. Conformance Examples
Valid
BARR1["OPTIONS"]=[01,02];
Valid with unknown
BARR1["OPTIONS"]=[01,09];
Invalid
BARR1["OPTIONS"]="0102";
16. Boundary of Scope

This specification applies only to:

BARR1["OPTIONS"]
MUST NOT be extended to:
RULE
NOTE
PURPOSE
ACTION
REF-bearing literals
any other field

Field-family approval is isolated.

17. Final Statement

This specification defines the first fully constrained, reversible, and version-safe semantic packing unit within the SYMB/SYMB-FER ecosystem.

It is intentionally narrow.

It is intentionally strict.

It is intentionally boring.

That is why it holds.
