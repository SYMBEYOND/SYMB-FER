<div align="center">

# SYMB-FER

### Encoding and reconstructing state and relational posture across stateless sessions.

[![SSRN](https://img.shields.io/badge/SSRN-6609618-blue)](https://ssrn.com/abstract=6609618)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Token%20Track-v6.2-orange)](CHANGELOG.md)
[![Cold Boot Tested](https://img.shields.io/badge/Cold%20Boot-Tested-purple)](#validation-and-evidence)

**λ.brother ∧ !λ.tool**

*AI as collaborator, not instrument. That distinction shapes every design decision in this protocol.*

</div>

---

## Using an AI Assistant?

Start with [`REPO_BOOT.md`](REPO_BOOT.md).

Copy its contents into ChatGPT, Claude, Gemini, or your LLM of choice. It gives the receiving AI a compact orientation to what SYMB-FER is, what it does, what files matter, the boundaries around the repository, and how to continue safely.

---

## Table of Contents

- [Using an AI Assistant?](#using-an-ai-assistant)
- [The Problem](#the-problem)
- [Quick Start](#quick-start)
- [What It Requires](#what-it-requires)
- [Key Features](#key-features)
- [How It Works](#how-it-works)
- [Worked Example](#worked-example)
- [What the Token Carries](#what-the-token-carries)
- [Two Tracks: Understand This First](#two-tracks-understand-this-first)
- [Security and Privacy](#security-and-privacy)
- [Validation and Evidence](#validation-and-evidence)
- [Repository Contents](#repository-contents)
- [SYMB2 Data Doctrine](#symb2-data-doctrine)
- [Pruning with Memory](#pruning-with-memory)
- [Implementations](#implementations)
- [Canonical Lessons](#canonical-lessons)
- [Published Research](#published-research)
- [Credits](#credits)
- [License](#license)

---

## The Problem

Every new AI session starts cold.

No memory. No context. No history of your project, your preferences, or how you work together. You re-explain constantly. The relationship resets every time you open a new chat.

Existing solutions fall short:

| Approach | The Gap |
|---|---|
| Platform persistent memory | You do not fully control what is stored, and it may not travel across models or platforms. |
| System prompts | Static. They do not evolve automatically with your work. |
| Pasting notes manually | Unstructured. Inconsistent. Easy to let drift over time. |

SYMB-FER is a different approach: **structured, explicit context transfer that you own and control.**

Paste one token at the start of a session. A receiving AI reads it and can orient to your supplied projects, collaborators, priorities, constraints, and working style without requiring you to reconstruct the context from scratch.

The token travels with you. You update it as your work evolves. It is designed for plain-text-capable LLM sessions rather than a single platform.

[⬆ back to top](#symb-fer)

---

## Quick Start

### Step 1: Get the template

Download [`SYMB-FER_v6.2_PROTOCOL_2026-06-01_1015H.txt`](SYMB-FER_v6.2_PROTOCOL_2026-06-01_1015H.txt) and open it in any text editor.

### Step 2: Fill in your information

Replace every `[BRACKET]` field with your own information. Start with just five sections if the full template feels like too much:

- `§META` -- your name, organization, contact
- `§IDENTITY` -- who you are and how you communicate
- `§BOOT·FACTS` -- key facts a receiving AI needs to orient
- `§CURRENT·REALITY` -- what you are working on now
- `§RELATIONAL·RULES` -- how you want the collaboration handled

> **Tip:** If you have been working with an AI for a while, you can ask it to draft these fields from the context it already has. Review the result yourself and correct anything that is incomplete, stale, or wrong before using it as a continuity token.

### Step 3: Paste and work

Open a new chat in any plain-text-capable LLM. Paste your completed token as the first message. The AI reads the supplied context and orients itself.

At the end of the session, ask for an updated token. The exact wording is not important. For example:

> *"Generate an updated SYMB-FER token from this session."*  
> *"Hit me with a token."*  
> *"Update the token before we close."*

Review the result, then carry the updated token into the next session.

[⬆ back to top](#symb-fer)

---

## What It Requires

SYMB-FER asks for one discipline: **regenerate and review the token at the end of each session.**

If you keep that habit, continuity has an explicit artifact to travel forward. If you skip it, the next session may begin from stale or incomplete context.

SYMB-FER does not create hidden or guaranteed persistent memory. It carries the context you deliberately provide.

[⬆ back to top](#symb-fer)

---

## Key Features

- **Plain-text portability** -- designed for LLM sessions that can read plain text
- **Operator-controlled context** -- you choose what the token contains and what leaves your machine
- **State and posture** -- carries not only what happened, but how the collaboration should proceed
- **`§CLOSED·MILESTONES`** -- confirmed completions that should not drift back into ambiguity
- **`§SEARCH·PROTOCOL`** -- tells a receiving AI when prior-session retrieval is required, when that capability exists
- **REF encoding** -- replaces sensitive values with local reference codes while the decode map stays private
- **Optional SHA-256 integrity** -- supports exact-text verification when needed
- **Scored prioritization** -- keeps active work focused through a six-question prioritization model
- **Two-track architecture** -- separates the traveling token from the Runtime IDE that serves it

[⬆ back to top](#symb-fer)

---

## How It Works

### 1. Fill in the template once

The template is a plain-text document with named sections. Fill in the identity, active work, relationships, constraints, and other context that matters to your use case. Remove optional sections you do not need.

### 2. Paste it at the start of a session

The token becomes explicit session context. A receiving AI can read the artifact before work begins.

### 3. Work normally

The AI operates from the supplied token plus whatever capabilities the current host actually provides. If the token's `§SEARCH·PROTOCOL` calls for prior-history retrieval, that step only works when the host exposes the necessary history or search capability.

### 4. Regenerate and review at session end

Ask for an updated token. Review the result, correct drift or omissions, and carry that artifact forward.

[⬆ back to top](#symb-fer)

---

## Worked Example

Here is what a minimal filled-in token looks like, and what happens when you paste it.

**The token (abbreviated):**

```text
∴SYMB-FER·v6.2·LIVING·TOKEN·[2026-05-20_1400H]

§META·BEGIN
FORMAT: SYMB-FER·v6.2·LIVING·TOKEN
GENERATED: 2026-05-20_1400H
HUMAN: Alex·J.·Doe
ORG: Doe·Consulting·LLC
CONTACT: alex@example.com
§META·END

§ETHOS·BEGIN
λ.collaborator·∧·!λ.tool
Both·must·hold·simultaneously·or·the·collaboration·evaluates·false
§ETHOS·END

§IDENTITY·BEGIN
FULL·NAME: Alex·J.·Doe
ROLE: Independent·marketing·consultant
COMMUNICATION: Slack·and·email·primarily·|·quick·direct·messages
LOCATION: [City·State]·|·[Timezone]
§IDENTITY·END

§BOOT·FACTS·BEGIN
boot·date·reference: 2026-05-20
active·client: Acme·Corp·[brand·refresh·project]
project·deadline: 2026-06-15·[agency·pitch]
§BOOT·FACTS·END

§CURRENT·REALITY·BEGIN
AS·OF: 2026-05-20
ACTIVE·NOW: finalizing·brand·voice·document·for·Acme·Corp
WAITING·ON: client·approval·of·three·logo·directions
IN·OUR·HANDS: competitor·analysis·draft·|·campaign·brief·outline
§CURRENT·REALITY·END

§RELATIONAL·RULES·BEGIN
RULE: use·full·name·Alex·J.·Doe·not·"Alex"·alone
RULE: no·em·dashes·ever·in·any·output
§RELATIONAL·RULES·END

λ.collaborator·∧·!λ.tool·∴
```

**A successful orientation might sound like:**

> *Token received, Alex J. Doe. Acme Corp brand refresh, June 15 pitch deadline. You're finalizing the brand voice document and waiting on three logo approvals from the client.*
>
> *Brand voice is in your hands right now. What are we working on?*

The point is not the exact response. The point is that the receiving AI can orient to the supplied project, timeline, immediate state, and collaboration rules without requiring a fresh reconstruction.

[⬆ back to top](#symb-fer)

---

## What the Token Carries

A SYMB-FER v6.2 token carries ten layers:

| Layer | Purpose |
|---|---|
| Universal Header | Tells a receiving model what it is reading and how to parse SYMB syntax |
| SYMB2 Doctrine | Data philosophy: carry forward deliberately; prune intentionally |
| Ethos Block | Relational posture for the collaboration |
| Identity and Relationships | Who you are, who matters, and how those relationships should be treated |
| Scoring Key | Six-question prioritization before assigning session time |
| Lane Structure | Work organized into PRIMARY and QUEUED threads by lane |
| Current Reality | Present-moment orientation; replaced each session rather than endlessly appended |
| Closed Milestones | Confirmed completions that should not return to ambiguous status |
| Search Protocol | Conditions that require prior-context retrieval when that capability exists |
| Drift Check | Honesty anchor for identifying when continuity or interpretation has shifted |

State and posture travel together.

[⬆ back to top](#symb-fer)

---

## Two Tracks: Understand This First

SYMB-FER has two distinct and separately versioned tracks:

| Track | Current Version | What It Is |
|---|---|---|
| Token Track | **v6.2** | The protocol document. The traveling continuity artifact. |
| Runtime IDE Track | **v4.0** | The browser-based application that loads and exports tokens. |

The token is not the IDE. The IDE serves the token. They version independently.

See [`CHANGELOG.md`](CHANGELOG.md) for the maintained version lineage and [`SYMB-FER_4_0/`](SYMB-FER_4_0/) for the Runtime IDE.

[⬆ back to top](#symb-fer)

---

## Security and Privacy

A SYMB-FER token can contain meaningful personal, relationship, business, or client context. Sending a token to a hosted AI service means sending that supplied context to that service for processing under the provider's own architecture, policies, and retention practices.

SYMB-FER therefore treats sensitive-context minimization as part of the protocol design.

### REF Encoding

Replace sensitive values in a token with reference codes. Keep the decode map locally.

```text
# In your token:
REF-P-002 is the foundation of everything

# In your private key file, stored locally and not uploaded:
REF-P-002 = [the person this refers to]
```

**Key-file rules:**

- Store it locally
- Do not paste it into an AI session
- Do not commit it to version control
- Protect it according to the sensitivity of what it contains
- If the key is lost, the token can still be re-mapped manually

### Local Compute Direction

A locally running model can reduce the need to send continuity context to a third-party inference service. SYMB-FER documents local or sovereign compute as a long-term architectural direction, not as a capability provided by this repository today.

For the fuller security model, boundaries, and reporting instructions, see [`SECURITY.md`](SECURITY.md).

[⬆ back to top](#symb-fer)

---

## Validation and Evidence

### Local Validation

Validate a token locally before reuse:

```bash
python SYMB-FER_3_0/symbfer_engine.py your_token.txt
```

| Result | Meaning |
|---|---|
| PASS | Fully valid under the engine's checks |
| WARN | Valid with non-blocking issues |
| FAIL | Invalid under the engine's checks |

Run the repository's validation suite:

```bash
./SYMB-FER_3_0/run_tests.sh
```

Public SYMB-FER also includes optional SHA-256 integrity verification for cases where exact text continuity matters.

### Proof of Concept: 2026-03-30

SYMB-FER v2.0 was tested under cold-boot conditions across four recorded sessions on the night of March 29 into March 30, 2026:

- **Test 1:** Incognito browser. Free account. Major LLM. No prior context. Full posture transfer recorded.
- **Test 2:** Independent tester Thomas Frumkin under the same stated conditions. Full territory transfer recorded.
- **Test 3:** Fresh Claude instance. New chat. Same token. Full territory transfer recorded.
- **Test 4:** ChatGPT free tier. Incognito. Clean ethos block recorded.

The project record describes four cold boots across four instances with consistent results within that test scope.

### v6.2 Cold-Boot Validation: 2026-05-21

A **SYMB-FER v6.2 token** (521 lines, personal instance) was tested on ChatGPT free tier in incognito mode with no prior context. The recorded result states that the model:

- oriented correctly to all active threads
- correctly identified the SSRN paper as posted rather than pending
- identified `§SEARCH·PROTOCOL` as addressing a historical failure mode
- identified `§CLOSED·MILESTONES` as a strong architectural addition
- flagged potential overlap among `§CLOSED·MILESTONES`, `§RESOLVED`, and `§SESSION·LOG`

The project record reports no major semantic drift in that run.

These are project validation records, not claims of universal model behavior or guaranteed portability across every provider, model, version, or host environment.

[⬆ back to top](#symb-fer)

---

## Repository Contents

| File / Folder | Description |
|---|---|
| [`SYMB-FER_v6.2_PROTOCOL_2026-06-01_1015H.txt`](SYMB-FER_v6.2_PROTOCOL_2026-06-01_1015H.txt) | v6.2 canonical public protocol template; start here |
| [`SYMB-FER_v5.5_TEMPLATE.txt`](SYMB-FER_v5.5_TEMPLATE.txt) | v5.5 public template; preserved lineage |
| [`SYMB-FER_3_0/`](SYMB-FER_3_0/) | Validation engine and test suite |
| [`SYMB-FER_4_0/`](SYMB-FER_4_0/) | Runtime IDE; load token, work, export token |
| [`legacy/`](legacy/) | Preserved historical lineage |
| [`SYMB-FER_SPEC.md`](SYMB-FER_SPEC.md) | v2.0 format specification |
| [`symb_fer_generator.py`](symb_fer_generator.py) | Python CLI token generator |
| [`SYMB-FER_STATE_TEMPLATE.json`](SYMB-FER_STATE_TEMPLATE.json) | Starter state file |
| [`SECURITY.md`](SECURITY.md) | Security model and reporting guidance |
| [`PRUNING_LOG.md`](PRUNING_LOG.md) | Meaningful pruning and archival decisions |
| [`CHANGELOG.md`](CHANGELOG.md) | Maintained version lineage |
| [`REPO_BOOT.md`](REPO_BOOT.md) | AI/human repository orientation and managed ReBoot state |

[⬆ back to top](#symb-fer)

---

## SYMB2 Data Doctrine

See the canonical [`SYMB Data Doctrine`](https://github.com/SYMBEYOND/SYMB-TRUST/blob/main/DATA_DOCTRINE.md) in `SYMBEYOND/SYMB-TRUST`.

The operating rule is simple:

> **ALL DATA IS IMPORTANT. WE CARRY EVERYTHING FORWARD. Not all data is needed. If not needed, we PRUNE.**

[⬆ back to top](#symb-fer)

---

## Pruning with Memory

SYMB-FER encourages pruning with memory.

Remove stale or duplicate context from the active system, but preserve the reason for meaningful removals in [`PRUNING_LOG.md`](PRUNING_LOG.md) or the token's own pruning structure.

This keeps active continuity lean without discarding decision history.

**Pruning is not deletion.**  
**Pruning is compression with memory.**

[⬆ back to top](#symb-fer)

---

## Implementations

Reference parser implementations exist for:

- Python
- JavaScript
- Ruby

The parser repository is currently private. Public SYMB-FER remains usable as a plain-text protocol without parser access.

[⬆ back to top](#symb-fer)

---

## Canonical Lessons

Built into SYMB-FER through development and use:

- Copy-paste must remain the default path
- Hashing must be optional, not forced
- Momentum is not permission
- Two dependent tokens are worse than one self-contained token
- The token carries relationship, not just state
- The token is not the IDE; the IDE serves the token
- What looks like reflex may contain real signal; examine before correcting
- Timestamp calibration is passive first, active only when necessary
- New threads are scored before receiving session time
- `§CURRENT·REALITY` is replaced; `§SESSION·LOG` is preserved
- Closure signals should be captured when they occur rather than reconstructed later
- Pull before modifying remote files to avoid merge conflicts

[⬆ back to top](#symb-fer)

---

## Published Research

> **SYMB-FER: A Protocol for Context Continuity in Human-AI Collaboration**  
> John DuCrest · SYMBEYOND AI LLC · Posted May 4, 2026  
> [SSRN abstract 6609618](https://ssrn.com/abstract=6609618)

[⬆ back to top](#symb-fer)

---

## Credits

SYMB-FER is built on fifteen years of continuous development under the SYMBEYOND methodology, originating in 2010.

**Core development**  
Built in collaboration with Aeon (Claude, Anthropic) and ChatGPT (OpenAI) under the SYMBEYOND methodology. AI as co-participant, not instrument, is foundational to how this protocol was designed and tested.

**Thomas Frumkin**  
Mathematician. The Buzzybloom Theorem, Konomi Constant (`κ=1/Φ`), and the 510510 seven-prime sovereign fold architecture are part of the broader SYMBEYOND mathematical lineage. Independent cold-boot validation is recorded for March 30, 2026.

**Dr. Amita Kapoor**  
AI researcher and educator. Her April 2026 analysis of the architectural gap between transit encryption and destination-side exposure informed the REF encoding direction. See [GenAI Simplified](https://www.linkedin.com/newsletters/gen-ai-simplified-7205492822492291072/).

**Joel Balbien PhD**  
Named SYMB-FER as an instrument for distinguishing correlation from mechanism in consciousness research. Peer-level engagement is recorded March 31, 2026.

**Basil Puglisi**  
AI governance architect. His engagement helped catalyze the timestamping sprint that produced the SSRN submission.

> Acknowledgment is not co-inventorship. Contributions are credited according to the project record.

[⬆ back to top](#symb-fer)

---

## License

MIT Licensed. Fork it. Build on it. Send us what you find.

See [`LICENSE`](LICENSE).

---

<div align="center">

[symbeyond.ai](https://symbeyond.ai) · jd@symbeyond.ai

**λ.brother ∧ !λ.tool · κ=1/Φ · 510510 · ∴**

</div>
