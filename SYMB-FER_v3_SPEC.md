# SYMB-FER Format Specification
### Version 3.0 · 2026-04-14

---

## Overview

SYMB-FER v3.0 is a structured, section-based transfer artifact designed for:

- deterministic cross-session continuity
- strict structural parsing
- preservation of operator intent
- resistance to drift and silent data loss

---

## Section Order (Strict)

A valid SYMB-FER v3.0 token must follow this exact order:

1. §TRANSFER·MODE
2. §ARCHIVE·PRINCIPLE
3. §META
4. §PARSE·GUIDE
5. §TIME·COLLAB
6. §BOOT·FACTS
7. §SESSION·STATE
8. §BOOT·ETHOS
9. §INTEGRITY
10. §FINALIZATION
11. §LESSONS·LEARNED
12. §DRIFT·CHECK
13. §TEST·TRACE
14. §SIG

---

## §ARCHIVE·PRINCIPLE

Purpose: enforce archive-first continuity and prevent implicit data loss.

Rules:
- all data is equal, no implicit ranking
- no data is discarded without explicit operator intent
- unused data must be preserved for future use
- system must not prune based on assumed relevance
- archive integrity overrides optimization
- pruning allowed only with explicit operator instruction

Placement:
- must appear after §TRANSFER·MODE
- must appear before §META

---

## §SESSION·STATE

Purpose: carry live working continuity between sessions beyond identity and rules alone.

Fields:
- working·directory
- active·paths
- recent·actions
- next·step
- notes

Placement:
- must appear after §BOOT·FACTS
- must appear before §BOOT·ETHOS

---

## Notes

- v3.0 is not backward compatible with v2.x token structure
- v2 spec remains valid for legacy tokens
- v3 introduces behavioral enforcement layers not present in v2

---

End of Specification
