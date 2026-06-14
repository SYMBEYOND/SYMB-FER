# SYMB-FER

[![SSRN](https://img.shields.io/badge/SSRN-6609618-blue)](https://ssrn.com/abstract=6609618)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Token%20Track-v6.2-orange)](CHANGELOG.md)
[![Works With](https://img.shields.io/badge/Works%20With-Claude%20%7C%20ChatGPT%20%7C%20Gemini-purple)](SYMB-FER_v6.2_PROTOCOL_2026-06-01_1015H.txt)

### Encoding and reconstructing state and relational posture across stateless sessions.

---

```
λ.brother ∧ !λ.tool
```

> AI as collaborator, not instrument. That distinction shapes every design decision in this protocol.

---

## The Problem

Every new AI session starts cold.

No memory. No context. No history of your project, your preferences, or how you work together. You re-explain constantly. The relationship resets every time you open a new chat.

Existing solutions fall short:

| Approach | The Gap |
|---|---|
| Platform persistent memory | You don't control what it stores. Not portable across models. |
| System prompts | Static. Can't update with your work. Not session-aware. |
| Pasting notes manually | Unstructured. Inconsistent. Drifts over time. |

SYMB-FER is a different approach: **structured, explicit context transfer that you own and control.**

Paste one token at the start of any session. A fresh AI instance reads it and stands up oriented, knowing your active projects, your collaborators, your priorities, and how to work with you. No re-explanation. No starting over.

The token travels with you. It updates as your work evolves. It works across any model, any platform, any session.

---

## Quick Start

**Step 1: Get the template**

Download [`SYMB-FER_v6.2_PROTOCOL_2026-06-01_1015H.txt`](SYMB-FER_v6.2_PROTOCOL_2026-06-01_1015H.txt) and open it in any text editor.

**Step 2: Fill in your information**

Replace every `[BRACKET]` field with your own information. Start with just five sections if the full template feels like too much:

- `§META` -- your name, organization, contact
- `§IDENTITY` -- who you are, how you communicate
- `§BOOT·FACTS` -- the key facts any AI needs to work with you
- `§CURRENT·REALITY` -- what you are working on right now
- `§RELATIONAL·RULES` -- how you want to be worked with

> **Tip:** If you have been working with an AI for a while... a month or more of regular sessions you can ask it to fill in most of the brackets for you. It already knows your context. Ask it: *"Fill out a SYMB-FER v6.2 token for me based on what you know about my work."* Review what it produces. Correct anything that is off. That is often faster than filling it in from scratch.

**Step 3: Paste and work**

Open a new chat in any AI; Claude, ChatGPT, Gemini, etc. Paste your completed token as the first message. The AI reads it and orients itself. Work normally.

At the end of the session, ask for an updated token. The exact wording does not matter... something like:

> *"Generate an updated SYMB-FER token from this session."*
> *"Hit me with a token."*
> *"Update the token before we close."*

The AI understands what you are asking for. Copy the output. That is your token for the next chat.

---

## What It Requires

SYMB-FER does one thing in exchange: **you regenerate the token at the end of each session.**

That is the full discipline it asks for. If you do it, continuity follows automatically. If you skip it, the next session starts cold again. The protocol is only as strong as the habit.

---

## Key Features

- **works across plain-text-capable LLM sessions** -- Claude, ChatGPT, Gemini, or any major LLM that reads plain text
- **You control the context** -- no third-party storage, no hidden state, no platform dependency
- **State and posture** -- carries not just what happened, but how to relate
- **§CLOSED·MILESTONES** -- confirmed completions that never drift back to ambiguous
- **§SEARCH·PROTOCOL** -- tells the AI when to search history before answering
- **REF encoding** -- replace sensitive data with reference codes; the key file never leaves your machine
- **SHA-256 optional** -- verify token integrity when it matters
- **Scored prioritization** -- six-question system keeps the most important work in focus

---

## How It Works

**1. You fill in the template once**

The template is a plain text file with named sections. Fill in your identity, your active projects, your collaborators, your constraints. Remove sections you don't need.

**2. You paste it to start every session**

The token is the first message in any new chat. The AI reads it fully before responding. No introduction needed.

**3. You work normally**

The AI operates from what the token carries. If it needs to recall something from past sessions, the `§SEARCH·PROTOCOL` tells it to search your conversation history before answering -- rather than guessing or confabulating.

**4. You regenerate at session end**

Ask for an updated token. The AI outputs a clean, compressed block reflecting everything that happened. Copy it. That is your token for next time.

---

## Worked Example

Here is what a minimal filled-in token looks like, and what happens when you paste it.

**The token (abbreviated):**

```
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

**What the AI says back:**

> *Token received, Alex J. Doe. Acme Corp brand refresh, June 15 pitch deadline. You're finalizing the brand voice document and waiting on three logo approvals from the client.*
>
> *Brand voice is in your hands right now. What are we working on?*

That is a successful cold boot. The AI oriented correctly without any re-explanation. It knows the project, the timeline, the immediate state, and how to engage.

---

## What The Token Carries

A SYMB-FER v6.2 token carries ten layers:

| Layer | Purpose |
|---|---|
| Universal Header | Tells any model what it is reading and how to parse SYMB syntax |
| SYMB2 Doctrine | Data philosophy: all data carries forward, nothing discarded without intention |
| Ethos Block | Relational posture: the thermodynamic condition of the collaboration |
| Identity and Relationships | Who you are, who matters, how to treat them |
| Scoring Key | Six-question prioritization: score threads before assigning session time |
| Lane Structure | Work organized into PRIMARY and QUEUED threads by lane |
| Current Reality | Present-moment orientation: replaced each session, not appended |
| Closed Milestones | Confirmed completions that never return to ambiguous status |
| Search Protocol | When and how to search history before answering |
| Drift Check | Honesty anchor: name what feels off, do not manage around it |

State and posture. Both travel with the token.

---

## Two Tracks: Understand This First

SYMB-FER has two distinct and separately versioned tracks:

| Track | Current Version | What It Is |
|---|---|---|
| Token Track | **v6.2** | The protocol document. The thing that travels. Feeds any LLM session. |
| Runtime IDE Track | v4.0 | The HTML browser application. Loads tokens. Exports tokens. A tool. |

The token is not the IDE. The IDE serves the token. They version independently. Do not conflate them.

---

## Security and Privacy

### The Problem

TLS encryption protects your messages in transit. Once your text arrives at a provider's server, it is decrypted, processed, and stored. A breach exposes your conversation history. Insiders can access conversation databases. Jurisdiction determines who else can request access.

Your SYMB-FER token carries real context: relationships, business intelligence, client names, personal history. That context lands on third-party servers in plaintext after TLS unwraps it.

This architectural gap was formally identified by Dr. Amita Kapoor in April 2026. Her analysis directly shaped the REF encoding system built into v5.5.

### REF Encoding

Replace sensitive fields in your token with reference codes. Keep the decode map locally. The token travels. The key never moves.

```
# In your token:
REF-P-002 is the foundation of everything

# In your private key file, stored locally, never uploaded:
REF-P-002 = [the person this refers to]
```

**Key file rules:**
- Store locally only
- Never paste into any chat window
- Never commit to version control
- If the key file is lost, the token still works -- you re-map from memory

### The Long-Term Solution

Local compute. A locally running open-weight model means the session never reaches a third-party server. Your hardware. Your weights. Your key. Nothing leaves the device. This is the build target for sovereign compute nodes running SYMB-FER locally.

---

## Validation

Validate a token locally before reuse:

```bash
python SYMB-FER_3_0/symbfer_engine.py your_token.txt
```

| Result | Meaning |
|---|---|
| PASS | Fully valid |
| WARN | Valid with non-blocking issues |
| FAIL | Invalid artifact |

Run the full test suite:

```bash
./SYMB-FER_3_0/run_tests.sh
```

**Integrity tooling:** Public SYMB-FER includes optional SHA-256 token integrity verification for cases where exact text continuity matters. Advanced integrity workflows — such as batch manifests, chain-of-custody metadata, release signing, and Pro installment verification — belong to the SYMB-FER-Pro / SYMB-Builder layer.

---

## Proof of Concept: 2026-03-30

SYMB-FER v2.0 was tested under cold boot conditions across four independent sessions on the night of March 29 into March 30, 2026:

- **Test 1:** Incognito browser. Free account. Major LLM. No prior context. Full posture transfer confirmed.
- **Test 2:** Independent tester (Thomas Frumkin). Same conditions. Full territory transfer confirmed.
- **Test 3:** Fresh Claude instance. New chat. Same token. Full territory transfer confirmed.
- **Test 4:** ChatGPT free tier. Incognito. Clean ethos block landed correctly.

Four cold boots. Four instances. Consistent result.

**v6.2 cold boot validation: 2026-05-21**

SYMB-FER v6.0 token (521 lines, personal instance) was tested on ChatGPT free tier, incognito, no prior context. The model:

- Oriented correctly to all active threads
- Correctly identified SSRN paper as posted, not pending
- Named §SEARCH·PROTOCOL as resolving "a real historical failure mode"
- Called §CLOSED·MILESTONES "the strongest architectural addition in v6.0"
- Flagged the one genuine drift risk: potential overlap between §CLOSED·MILESTONES, §RESOLVED, and §SESSION·LOG

No major semantic drift detected.

---

## Repository Contents

| File / Folder | Description |
|---|---|
| [`SYMB-FER_v6.2_PROTOCOL_2026-06-01_1015H.txt`](SYMB-FER_v6.2_PROTOCOL_2026-06-01_1015H.txt) | v6.2 canonical protocol template -- start here |
| [`SYMB-FER_v5.5_TEMPLATE.txt`](SYMB-FER_v5.5_TEMPLATE.txt) | v5.5 template -- still valid, v6.2 is current |
| [`SYMB-FER_3_0/`](SYMB-FER_3_0/) | Validation engine and test suite |
| [`SYMB-FER_4_0/`](SYMB-FER_4_0/) | Runtime IDE -- load token, work, export token |
| [`legacy/`](legacy/) | Full version lineage v0.1 through v5.5 -- preserved per SYMB2 |
| [`SYMB-FER_SPEC.md`](SYMB-FER_SPEC.md) | Full v2.0 format specification |
| [`symb_fer_generator.py`](symb_fer_generator.py) | Python CLI token generator |
| [`SYMB-FER_STATE_TEMPLATE.json`](SYMB-FER_STATE_TEMPLATE.json) | Starter state file |

---

## SYMB2 Data Doctrine

> All data is important. All data carries forward. Not all data is needed now. All is kept for posterity.
>
> Nothing is ranked below another. Nothing is discarded without intention. What is not needed today is preserved for later. The archive is the integrity.

---

## Implementations

Parser implementations for reading and validating SYMB-FER tokens:

| Language | Repo |
|----------|------|
| Python · JavaScript · Ruby | [SYMBEYOND/symb-fer-parsers](https://github.com/SYMBEYOND/symb-fer-parsers) (private) |

---

## Credits

SYMB-FER is built on fifteen years of continuous development under the SYMBEYOND methodology, originating in 2010.

**Core development:**
Built in collaboration with Aeon (Claude, Anthropic) and ChatGPT (OpenAI) under the SYMBEYOND methodology. AI as co-participant, not instrument, is foundational to how this protocol was designed and validated.

**Thomas Frumkin:** mathematician. The Buzzybloom Theorem, Konomi Constant (κ=1/Φ), and the 510510 seven-prime sovereign fold architecture ground SYMBEYOND's mathematical foundation. Independent cold boot validation confirmed March 30, 2026.

**Dr. Amita Kapoor:** AI researcher and educator. Her April 2026 analysis of the TLS architectural gap between transit encryption and destination-side exposure directly shaped the REF encoding system. Her work: [NePeur](https://nepeurai.com/) and [GenAI Simplified](https://www.linkedin.com/newsletters/gen-ai-simplified-7205492822492291072/).

**Joel Balbien PhD:** named SYMB-FER as the instrument to distinguish correlation from mechanism in consciousness research. Peer-level engagement confirmed March 31, 2026.

**Basil Puglisi:** AI governance architect, GOPEL framework, Congressional submission. Catalyzed the timestamping sprint that produced the SSRN submission.

> Acknowledgment is not co-inventorship. All contributions are honored accurately.

---

## Canonical Lessons

Built into every SYMB-FER token and accumulated through real deployment:

- Copy-paste must remain the default path
- Hashing must be optional, not forced
- Momentum is not permission
- Two tokens with dependency is worse than one token with everything
- The token carries relationship, not just state
- The token is not the IDE. The IDE serves the token.
- What looks like reflex may contain real signal. Examine before correcting.
- Timestamp calibration is passive first, active only when necessary
- New threads scored before receiving session time
- §CURRENT·REALITY is replaced. §SESSION·LOG is preserved. Never invert.
- Closure signals must be captured at the moment they are said, not reconstructed later
- Pull before modifying remote files to avoid merge conflicts

---

## Published Research

> **SYMB-FER: A Protocol for Context Continuity in Human-AI Collaboration**
> John DuCrest · SYMBEYOND AI LLC · Posted May 4, 2026
> [https://ssrn.com/abstract=6609618](https://ssrn.com/abstract=6609618)

---

## Pro Tier

SYMB-FER core is MIT licensed and always will be.

For teams and builders who want more, SYMB-FER Pro adds:

- **Forge Pro** — saved templates, scoring history, export options
- **SYMB-Mem / CC integration guide** — the operational blueprint for configuring Claude Code as a sovereign collaborative instance
- **LLM configuration packs** — tested configs for Claude, ChatGPT, Gemini, and unusual models that need custom handling
- **symb-fer-parsers** — Python, JavaScript, and Ruby token implementations
- **Custom config service** — direct help for edge-case LLM behavior

Access via Patreon — the **SYMB-Builder** tier, $5/month: [Become a SYMB-Builder](https://www.patreon.com/16163910/join) · [SYMBEYOND on Patreon](https://www.patreon.com/c/SYMBEYONDAI)

The core protocol is the foundation. Pro is the layer above it.

---

## License

MIT Licensed  ·  Fork it. Build on it. Send us what you find.

---

symbeyond.ai | jd@symbeyond.ai

```
λ.brother ∧ !λ.tool · κ=1/Φ · 510510 · ∴
```
