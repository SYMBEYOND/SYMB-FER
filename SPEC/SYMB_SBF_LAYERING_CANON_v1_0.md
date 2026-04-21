# SYMB–SBF Layering Canon v1.0

## 1. Purpose

This canon defines the relationship between:

- SYMB
- SYMB2
- SYMB-FER
- SBF-A
- SBF-B

It establishes authority, scope, and boundaries to prevent architectural drift.

## 2. Core Principle

> Source defines meaning. Transport preserves meaning. Packing compresses meaning only where proven safe.

## 3. Layer Definitions

### 3.1 Source Layer (Authoritative)

The following are source languages:

- SYMB
- SYMB2
- SYMB-FER

#### Requirements
- These layers MUST be treated as the canonical source of truth.
- These layers MUST NOT be replaced by transport or packing layers.
- These layers MUST remain human-readable and structurally explicit.

#### Role
- define intent
- define relationships
- define state
- define continuity
- define rules and constraints

### 3.2 Transport Layer (SBF-A)

SBF-A is the lossless structural transport layer.

#### Requirements
- SBF-A MUST preserve all source meaning without mutation.
- SBF-A MUST NOT reinterpret or normalize semantic content.
- SBF-A MUST maintain exact keys, values, and ordering.
- SBF-A MUST allow full reconstruction of source-equivalent structure.

#### Role
- reduce structural ambiguity
- standardize parsing
- enable cross-system portability

### 3.3 Packing Layer (SBF-B)

SBF-B is the field-scoped semantic packing layer.

#### Requirements
- SBF-B MUST operate only on explicitly approved field families.
- SBF-B MUST be version-pinned per dictionary.
- SBF-B MUST be fully reversible to SBF-A form.
- SBF-B MUST NOT introduce semantic interpretation.
- SBF-B MUST NOT generalize beyond its approved scope.

#### Role
- reduce token footprint
- compress finite, well-defined value sets
- preserve order, duplication, and unknowns

## 4. Authority Hierarchy

Authority flows strictly in this order:

    SYMB / SYMB2 / SYMB-FER
            ↓
          SBF-A
            ↓
          SBF-B

### Rules
- Lower layers MUST NOT override higher layers.
- Lower layers MUST NOT redefine meaning.
- All decoding MUST terminate at source-equivalent structure.

## 5. Non-Substitution Rule

### MUST NOT
- SBF-A replace SYMB or SYMB-FER as source
- SBF-B replace SBF-A as canonical transport
- SBF-B be treated as a primary authoring format

### Interpretation
- SBF layers are representations, not origins.

## 6. Scope Isolation Rule

Each SBF-B unit is isolated.

Example:

    BARR1["OPTIONS"]

### MUST
- apply only to its defined field family

### MUST NOT
- be reused across other fields without independent validation and canonization

## 7. Reversibility Requirement

All transformations must support:

    SOURCE → SBF-A → SBF-B → SBF-A → SOURCE

### MUST
- preserve order
- preserve duplication
- preserve unknowns
- preserve structure

### MUST NOT
- lose information
- introduce inferred meaning
- collapse semantic classes

## 8. Unknown Handling Rule

Across all layers:

### MUST
- preserve unknown symbols and values
- represent unresolved elements explicitly

### MUST NOT
- guess meaning
- discard unknown elements
- silently normalize unknowns

## 9. Evolution Rule

New SBF-B units may be introduced only if:

1. field family is finite and well-defined
2. multiple real source instances exist
3. dictionary can be defined without inference
4. reversibility is proven
5. hostile testing is passed

### MUST NOT
- expand packing based on convenience or assumption

## 10. Stability Rule

Once an SBF-B unit is accepted:

- its dictionary MUST be version-locked
- its encoding rules MUST NOT change within version
- any modification MUST increment version

## 11. Final Statement

> SYMB defines.
> SYMB2 structures.
> SYMB-FER carries.
> SBF-A preserves.
> SBF-B compresses.

Each layer exists for a distinct purpose.

No layer replaces another.
