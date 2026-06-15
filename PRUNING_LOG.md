# PRUNING_LOG.md

Pruning is not deletion.

Pruning is compression with memory.

This file records meaningful removals, deprecations, merges, archival decisions, or superseded directions in SYMB-FER.

The goal is to keep active continuity lean without losing the reason something was removed.

## Rule

Remove what no longer serves the active system.

Preserve why it was removed.

Prefer reversible decisions.

If a decision is not reversible, say so plainly.

## What should be logged

Log meaningful pruning such as:

- deprecated docs
- merged sections
- removed examples
- superseded plans
- abandoned directions
- public wording changes that affect interpretation
- changes that future maintainers may question later

Do not log tiny typo fixes, whitespace cleanup, or obvious duplicate noise unless the reason matters.

## Privacy boundary

Do not store secrets or sensitive private data in this file.

Do not include:

- passwords
- API keys
- seed phrases
- recovery codes
- SSH keys
- private keys
- OAuth tokens
- financial secrets
- medical details
- legal-sensitive details
- family-sensitive context
- private repo links
- private customer/client details

Public pruning logs must remain safe to share.

Git history may preserve the old text or file.

This log preserves the reason.

## Entry template

```md
## YYYY-MM-DD — Short title

STATUS: PRUNED | MERGED | ARCHIVED | DEPRECATED | SUPERSEDED
TYPE:
DECISION:
REASON:
PRESERVED WHERE:
REVERSIBILITY: YES | PARTIAL | NO
OPERATOR:
NOTES:
```

## 2026-06-15 — Add pruning-with-memory rule

STATUS: ADDED
TYPE: continuity rule
DECISION: Added this pruning log pattern to SYMB-FER.
REASON: SYMB-FER should support lean active context without losing decision history.
PRESERVED WHERE: PRUNING_LOG.md, README.md, REPO_BOOT.md
REVERSIBILITY: YES
OPERATOR: John DuCrest
NOTES: Initial implementation. Documentation-only. No protocol behavior change.
