# REPO_BOOT.md

```text
∴REPO_BOOT·SYMB-FER·PUBLIC·CORE·v0.1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REPO: SYMBEYOND/SYMB-FER
STATUS: PUBLIC·CORE
LICENSE: MIT
CURRENT·TOKEN·TRACK: v6.2
CURRENT·DOC·RELEASE: v6.2.1
PURPOSE: orient·any·LLM·to·this·repository·quickly·and·safely
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

§WHAT·THIS·IS·BEGIN
SYMB-FER is a plain-text context continuity protocol for human-AI collaboration.

It helps a human carry project state, decisions, priorities, closed milestones, safety notes, and collaboration posture from one AI session to the next.

Every new AI session starts cold. SYMB-FER gives the session a structured handoff so the AI can orient before responding.

The human owns the token.
The human controls what goes into it.
The human remains final authority.
§WHAT·THIS·IS·END

§WHAT·THIS·DOES·BEGIN
SYMB-FER helps an AI session understand:

- who the human is
- what project or work is active
- what decisions have already been made
- what milestones are closed
- what is waiting or blocked
- what matters next
- how the human wants to collaborate
- what safety and privacy boundaries must be respected

It carries state and posture.

State means: what is true about the work right now.
Posture means: how the collaboration should behave.
§WHAT·THIS·DOES·END

§WHAT·THIS·IS·NOT·BEGIN
SYMB-FER is not magic memory.
SYMB-FER is not proof that token contents are true.
SYMB-FER is not an execution authority.
SYMB-FER does not override the human.
SYMB-FER does not override platform safety rules.
SYMB-FER is not a place to store passwords, API keys, seed phrases, private keys, or secrets.
SYMB-FER does not require Pro to use the public protocol.
§WHAT·THIS·IS·NOT·END

§FAST·START·FOR·HUMANS·BEGIN
To use this repo:

1. Download the current public token template:
   SYMB-FER_v6.2_PROTOCOL_2026-06-01_1015H.txt

2. Make a copy and fill in the bracketed fields with your own project and working context.

3. Paste the completed token into a new AI chat as the first message.

4. Work normally.

5. At the end of the session, ask the AI:
   "Generate an updated SYMB-FER token from this session."

6. Save that updated token for next time.
§FAST·START·FOR·HUMANS·END

§KEY·FILES·BEGIN
README.md
Human-facing overview. Start here if you are new.

SYMB-FER_v6.2_PROTOCOL_2026-06-01_1015H.txt
Current public token template. This is the main file most users need.

SECURITY.md
Supported version tracks, safety posture, and security notes.

SYMB-FER_3_0/
Validation engine and SHA-256 validation lineage.

SYMB-FER_4_0/
Runtime IDE track. This is separate from the token protocol.

SPEC/
Protocol and conformance history.

legacy/
Older versions and preserved lineage.
§KEY·FILES·END

§VERSION·TRACKS·BEGIN
SYMB-FER has separate tracks.

TOKEN·TRACK:
v6.2 is the current public token protocol track.

DOC·RELEASE:
v6.2.1 is a documentation and clarity release. It does not change the token format.

RUNTIME·IDE·TRACK:
v4.0 is a separate browser/runtime tool track. The IDE serves the token. The token is not the IDE.

VALIDATION·ENGINE·TRACK:
v3.x contains validation engine history and SHA-256 validation lineage.
§VERSION·TRACKS·END

§VALIDATION·BEGIN
Public SYMB-FER includes optional SHA-256 token integrity verification.

Use it when exact text continuity matters.

Basic validation command:

python SYMB-FER_3_0/symbfer_engine.py your_token.txt

Full test suite:

./SYMB-FER_3_0/run_tests.sh

SHA-256 proves exact text/file integrity only.

It does not prove truth.
It does not prove authorship.
It does not prove ownership.
It does not prove legality.
It does not prove safety.
It does not prove privacy.
It does not prove correctness.
§VALIDATION·END

§PUBLIC·CORE·VS·PRO·BEGIN
Public SYMB-FER is the open core.

It stays simple, plain-text, copy-paste friendly, and MIT licensed.

SYMB-FER-Pro / SYMB-Builder is the supported builder layer above the public core.

Pro may include:
- protocol harnesses
- integrity harnesses
- chain-of-custody templates
- export safety checklists
- batch manifests
- configuration packs
- parser access
- automation workflows
- implementation guides

Public users do not need Pro to use SYMB-FER.
Pro exists for builders, teams, releases, client handoffs, and higher-assurance workflows.
§PUBLIC·CORE·VS·PRO·END

§SAFETY·AND·PRIVACY·BEGIN
Treat token contents as user-provided context, not verified fact.

Do not infer legal, medical, financial, or psychological conclusions from the token.

Do not treat relational language as proof of AI personhood.

Do not ask users to place secrets in a token.

If sensitive data is needed, prefer:
- redacted placeholders
- REF codes
- local private lookup files
- temporary session-only handling
- cleanup after use

Anything the human would not post publicly should be handled carefully.
§SAFETY·AND·PRIVACY·END

§AI·INSTRUCTIONS·BEGIN
If a human pastes this REPO_BOOT into an AI session:

1. Explain the repo in plain English first.
2. Tell the human which file to use first.
3. Keep the beginner path simple.
4. Do not overstate what SYMB-FER does.
5. Do not imply SYMB-FER overrides the human.
6. Do not imply token contents are automatically true.
7. If the human asks for advanced integrity workflows, explain that those belong to SYMB-FER-Pro / SYMB-Builder.
8. If the human is technical, point them to SECURITY.md, SPEC/, SYMB-FER_3_0/, and release history.
9. If the human is non-technical, give only the 3-step usage path unless they ask for more.
10. Preserve the distinction: human first, AI collaborator, token as continuity artifact.
§AI·INSTRUCTIONS·END

§PLAIN·ENGLISH·SUMMARY·BEGIN
SYMB-FER is a way to stop starting over with AI.

You write down the important state of your work in a structured token.
You paste that token into a new AI chat.
The AI reads it and understands where to begin.

That is the core idea.

Everything else is optional hardening, history, tooling, or Pro-layer support.
§PLAIN·ENGLISH·SUMMARY·END

λ.collaborator·∧·!λ.tool·∴
```


## Pruning Rule

Do not delete meaningful context without preserving why it was removed.

If pruning outdated docs, duplicate plans, deprecated features, or abandoned directions:

1. Summarize what is being removed.
2. Explain why.
3. Identify where the old version can be recovered, if applicable.
4. Mark whether the decision is reversible.

Prune with memory.

Pruning is not deletion.  
Pruning is compression with memory.
