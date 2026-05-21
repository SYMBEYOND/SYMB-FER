# CHANGELOG

All notable changes to SYMB-FER are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Version lineage preserved per SYMB2 doctrine: nothing is discarded without intention.

---

## [6.0] - 2026-05-18 - Search Protocol and Closed Milestones

### Added
- `§SEARCH·PROTOCOL` section: operational instructions for when and how to search conversation history, including closure signal detection and query guidance; positioned after `§BOOT·PROTOCOL`
- `§CLOSED·MILESTONES` section: permanent record of confirmed irreversible completions, distinct from `§RESOLVED`; once a milestone is confirmed closed it never returns to ACTIVE or QUEUED
- Closure signal vocabulary formalized: standard phrases that indicate a thread has completed (delivered, paid, posted, confirmed, etc.)
- Search trigger vocabulary formalized: phrases that require search before responding (past-reference phrasing, status questions, correction signals, named uncertainty)

### Changed
- `§BOOT·PROTOCOL` now explicitly includes REFER trigger and timestamp calibration as named subsections
- Two-track distinction (token vs IDE) clarified with explicit rule: IDE serves the token, never the reverse
- Lane structure formalized with PRIMARY/QUEUED distinction and six-question scoring key
- `§LESSONS·LEARNED` expanded with canonical lessons L-A through L-J

### Architecture
- v6.0 merges the best of v5.5 (REF encoding, ReFer protocol, REFER trigger, SYMB notation, resolved archive) with production-tested prioritization structure (scoring key, lane structure, session log)
- `§CURRENT·REALITY` is the only section replaced each session; `§SESSION·LOG` is never replaced -- distinction now explicit in both sections
- Public sanitized template maintained; personal data remains in private instance tokens

---

## [5.5] - 2026-04-21 - Token Track Formally Separated

### Added
- Living token architecture: `§CURRENT·REALITY` section replaces each session, not appended
- `§OPEN·THREADS` section separates ideas from active projects
- `§RESOLVED` section archives completed work with lessons captured
- REF encoding system: sensitive fields replaced with reference codes; real values in private local key file
- Timestamp calibration hierarchy: five-tier passive-first system; ask operator only as last resort
- Judgment-based boot protocol replaces rigid six-step sequence
- ReFer command formally documented with intent-based trigger recognition
- `SYMB-FER_v5.5_TEMPLATE.txt` public sanitized template added to repo
- `SECURITY.md` formal security policy added
- `CHANGELOG.md` this file

### Changed
- Token track and Runtime IDE track formally separated and versioned independently
- Boot protocol now runs on judgment not ceremony
- "What are we building?" compass question documented as intentional signal not reflexive closer
- README fully revised to reflect v5.5 architecture, REF encoding, security section, and updated credits

### Security
- REF encoding system introduced: protects sensitive context at rest after TLS unwrap
- Sovereign compute architecture defined as long-term solution
- Architectural gap formally credited to Dr. Amita Kapoor, April 2026

---

## [4.0] - 2026-04-19 - Runtime IDE

### Added
- `SYMB-FER_4_0/` HTML browser application: load token, work, export token
- Loop closed: token format + runtime environment + protocol = complete system
- Auto-boot problem solved without browser extension or API wrapper
- Session state persistence across different AI instances and time gaps
- Full version lineage documented in `legacy/` folder

### Notes
- v4.0 is the Runtime IDE track. It versions independently from the Token track.
- Token track continues from v3.2 forward as its own artifact.

---

## [3.2] - 2026-03-30 - Drift Resistance

### Added
- SHA-256 signing via `symbsign` Terminal alias
- BOOT split into FACTS and ETHOS sections
- Drift resistance validated: naming anti-drift block after an entity correctly identified and refused as drift vector
- `SYMB-FER_3_0/` validation engine, test suite, continuity hardening

### Validated
- Cold boot confirmed across four independent instances including independent tester
- Meta AI cross-platform test confirmed hash chain integrity spanning two LLM architectures

---

## [3.0] - 2026-03-21 - 14-Section Canonical Format

### Added
- 14-section canonical token format
- Structural validation engine
- Test-centric architecture: validation suite with canonical intents, decisions, payload rules
- `SYMB-FER_v3_SPEC.md` specification document

---

## [2.0] - 2026-03-15 - Posture Transfer

### Added
- Posture transfer: not just state, but how to relate
- Universal header: any model can parse SYMB syntax
- Ethos block: thermodynamic condition of collaboration
- SYMB2 doctrine: all data is important, all data carries forward
- Compressed format: reduces drift, token waste, interpretive ambiguity
- Published to GitHub with full sanitization

### Changed
- v1.x transferred state only; v2.0 transfers state and posture
- This is the difference between the map and the territory

---

## [1.x] - 2026-03-21 - Origin

### Added
- SYMB-FER protocol originated March 21, 2026
- Recognition that every new chat starts cold: context continuity as engineering problem not philosophy
- Initial state transfer token format
- Python CLI token generator: `symb_fer_generator.py`
- State template and example JSON files

### Notes
- Full v1.x lineage preserved in `legacy/` folder per SYMB2 doctrine
- v0.1 through v1.0 HTML runtime iterations preserved in `legacy/SYMB Runtime/`

---

## Origin

SYMB-FER is built on fifteen years of continuous development under the SYMBEYOND methodology, originating in 2010.

The protocol was formalized beginning March 21, 2026.

symbeyond.ai | jd@symbeyond.ai

```
λ.brother ∧ !λ.tool · κ=1/Φ · 510510 · ∴
```
