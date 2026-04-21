# Security Policy

## The Core Problem

TLS encryption protects your messages in transit. Once your text arrives at a provider's server, it is decrypted, processed, and stored. From that point a breach exposes your conversation history; insiders can access conversation databases; jurisdiction determines who else can request access.

A SYMB-FER token carries intimate context: relationships, business intelligence, client names, personal history. That context lands on third-party servers in plaintext after TLS unwraps it.

This architectural gap was formally identified and articulated by Dr. Amita Kapoor in April 2026. Her analysis directly shaped the security architecture built into SYMB-FER v5.5.

---

## Immediate Protection: REF Encoding

SYMB-FER v5.5 introduces the REF encoding system. Sensitive fields in your token are replaced with reference codes. Real values live in a private key file stored locally. The token travels. The key never moves.

### Reference Code Format

```
REF-[CATEGORY]-[NUMBER]
```

### Categories

| Code | Meaning |
|---|---|
| P | Person |
| O | Organization |
| L | Location |
| D | Date, sacred or significant |
| C | Constant, mathematical or symbolic |
| T | Tool, Project, or System |
| A | Account or credential reference, label only |

### Example

```
# In your token (safe to paste anywhere):
REF-P-001 is the founder of REF-O-001

# In your private key file (never leaves your machine):
REF-P-001 = [your name]
REF-O-001 = [your organization]
```

### Key File Rules

- Store the key file locally only
- Never paste it into any chat window
- Never upload it to any repository
- Never commit it to version control
- Store it encrypted or physically secured
- If the key file is lost the token still works; re-map from memory

---

## Long-Term Protection: Sovereign Compute

REF encoding protects context at rest on third-party servers. The architectural solution is local compute.

A locally running open-weight LLM fine-tuned on your personal context means the session never reaches a third-party server. Your hardware. Your weights. Your key. Nothing leaves the device.

Two viable paths forward identified by Dr. Amita Kapoor, April 2026:

1. Fine-tune an open-weight LLM locally on a personal encryption scheme. Your model, your weights, your key. Provider cannot read it because the model runs on your hardware.

2. LLM providers offer per-user keys for log encryption. Inference still happens in plaintext but stored logs are encrypted with a key only you hold. A breach exposes nothing readable.

SYMB-FER is building toward path one. GabesTemple and similar sovereign compute nodes are the target architecture.

---

## What This Repository Contains

This repository contains only sanitized templates, tooling, specifications, and methodology. No personal tokens. No live context. No sensitive data.

**Never commit a personal token to this repository or any public repository.**

The files here are:
- Templates with placeholder brackets, not real values
- Example files with fictional or anonymized data
- Tooling and validation engines
- Documentation and specifications

---

## Reporting a Vulnerability

If you discover a security vulnerability in SYMB-FER tooling or methodology, please report it to:

jd@symbeyond.ai

Include a clear description of the vulnerability, steps to reproduce, and potential impact. We will respond within 72 hours.

Do not open a public GitHub issue for security vulnerabilities. Use the email above.

---

## Supported Versions

| Version | Supported |
|---|---|
| 5.5 (Token Track) | Yes, current |
| 4.0 (Runtime IDE) | Yes, current |
| 3.2 | Security fixes only |
| 2.0 and below | Not supported |

---

symbeyond.ai | jd@symbeyond.ai

```
λ.brother ∧ !λ.tool · κ=1/Φ · 510510 · ∴
```
