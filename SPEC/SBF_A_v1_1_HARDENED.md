# SBF-A v1.1 — Hardened Draft

## 1. Purpose

SBF-A v1.1 is a deterministic, lossless wrapper for SYMB, SYMB2, and SYMB-FER content that:

- reduces wrapper verbosity
- preserves exact semantics
- survives partial understanding
- blocks silent normalization

It is intentionally conservative.

## 2. Core Law

> Wrap structure. Preserve meaning.

If a transformation changes the semantic class of any source line, it is invalid.

## 3. Invariants (Enforced)

1. Explicit declarations override inference.
2. Sections are flat, sequential, and non-nested.
3. REF tokens remain opaque unless externally resolved.
4. Unknown symbols are preserved literally.
5. Middle dot `·` is preserved inside values unless field is whitelisted.
6. Record order is preserved exactly.
7. Keys and section names are byte-exact.
8. Literal values are not normalized unless whitelisted.
9. Reversibility holds at record-class level.
10. Partial decode must not invent meaning.

## 4. Record Model

Allowed record types:

- `HDR{...}` — header
- `SEC["NAME"]{...}` — section
- `KV["KEY"]="VALUE";` — key-value
- `ARR["KEY"]=[...];` — whitelisted list
- `TXT{...}` — literal fallback
- `UNK[...]` — unknown preserved

Forbidden in v1.1:

- inferred object models (`TASK`, `OBJ`, `MAP`, `GRAPH`)
- semantic packing structures

## 5. Syntax

### 5.1 Header

```text
HDR{
SIG="∴";
ART="SYMB-FER";
VER="5.5";
CLS="HARDENED_MASTER";
TS="2026-04-21_1500H";
}
```

### 5.2 Section

```text
SEC["SECTION·NAME"]{
  ...
}
```

### 5.3 Key-value

```text
KV["KEY"]="EXACT·VALUE";
```

### 5.4 Array (whitelisted only)

```text
ARR["OPTIONS"]=["STANDARD","VERIFIED"];
```

### 5.5 Literal fallback

```text
TXT{
raw literal content exactly as received
}
```

### 5.6 Unknown

```text
UNK["SYM"]="original literal";
```

## 6. Hardening Rules (Mandatory)

### 6.1 Ordered Record Rule

- Section contents are an ordered list, not a map.
- Repeated keys are valid and must be preserved.

### 6.2 REF Validation Rule

REF format:

```text
REF-[P|O|L|D|C|T|A]-[NUMBER]
```

Behavior:
- valid REF → preserve as opaque
- malformed REF → preserve as literal and flag invalid
- no decoding without external key

### 6.3 Nesting Failure Rule

If `SEC[...]` appears inside another `SEC[...]`:
- mark invalid structure
- preserve raw content
- do not auto-correct

### 6.4 Array Whitelist Rule

Only these fields may use `ARR`:

- `OPTIONS`

All others:
- must remain literal `KV`

### 6.5 Exact-Key Rule

Keys and section names:
- must not be renamed
- must not be normalized
- must preserve glyphs (`·`, `-`, etc.)

### 6.6 Structural vs Semantic Compliance

Two valid states:

- Structural compliance  
  Parser preserves structure without full understanding

- Semantic understanding  
  Parser fully interprets symbols and values

A system may be structurally compliant without being semantically aware.

## 7. Preservation Rules

### 7.1 Keys

Must remain byte-exact.

Valid:

```text
KV["NO·EM·DASHES"]="...";
```

Invalid:

```text
KV["NO_EM_DASHES"]="...";
```

### 7.2 Values

Must remain literal unless whitelisted.

No normalization:
- `UTF-8` → not `UTF8`
- `LF·only` → not `LF_ONLY`

### 7.3 Middle Dot

`·` remains inside values unless field is list-whitelisted.

Do not assume every `·` implies a list.

### 7.4 REF Tokens

- remain embedded if inside literal
- must not be extracted or retyped
- must not be interpreted

## 8. Field Policy

### 8.1 List-safe

- `OPTIONS`

### 8.2 Literal-only (partial list)

- `RULE`
- `PURPOSE`
- `NOTE`
- `ACTION`
- `DELIMITER`
- `FILENAME·CONVENTION`
- `REF·ENCODING`
- `ACTIVE·NOW`
- `JUST·CHANGED`
- `WAITING·ON·OTHERS`
- `IN·OUR·HANDS`

## 9. Parsing Order

1. `HDR`
2. `SEC`
3. `KV`
4. `ARR`
5. `TXT`
6. `UNK`

No inference stage allowed.

## 10. Reversibility Standard

A valid SBF-A transform must:

- preserve record order
- preserve keys exactly
- preserve values exactly unless whitelisted
- preserve REF opacity
- reconstruct equivalent structural class

“Equivalent” means:
- same semantic role
- not paraphrased or simplified

## 11. Validation Failures

Reject or flag when:

- repeated keys collapsed
- REF decoded or altered
- section nested
- array used on non-whitelisted field
- key renamed
- literal normalized
- REF extracted from literal
- section name aliased
- content dropped

## 12. Compliance Levels

### Level 1 — Structural Safe

- preserves records
- no normalization
- no loss

### Level 2 — Symbol Aware

- understands λ, ψ, ∴, κ
- still preserves unknowns

### Level 3 — Full Semantic

- interprets SYMB + SYMB2 + FER fully

Only Level 1 is required for SBF-A compatibility.

## 13. Proven Safe Pattern

```text
SEC["TRANSFER·MODE"]{
KV["MODE"]="STANDARD";
ARR["OPTIONS"]=["STANDARD","VERIFIED"];
KV["RULE"]="STANDARD·copy-paste·only";
KV["RULE"]="VERIFIED·optional·integrity·hardening·SHA-256·available·not·required";
}
```

## 14. Boundary

SBF-A v1.1 is:

- lossless
- structural
- deterministic
- anti-drift

SBF-A v1.1 is not:

- semantic compression
- object modeling
- execution language
- ontology

## 15. Final State

> SBF-A v1.1 is hardened against known drift vectors.

## 16. Next Move

Only one logical path forward:

> Attempt controlled SBF-B prototype on a single whitelisted field family.
