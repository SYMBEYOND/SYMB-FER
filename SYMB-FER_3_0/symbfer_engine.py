from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re
from enum import Enum
from typing import Dict, List, Optional


BEGIN_RE = re.compile(r"^§([A-Z·]+)·BEGIN$")
END_RE = re.compile(r"^§([A-Z·]+)·END$")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")


class LoadStatus(str, Enum):
    OK = "OK"
    WARN = "WARN"
    FAIL = "FAIL"


@dataclass(frozen=True)
class SignatureBlock:
    mode: str
    status: str
    sha256: str


@dataclass(frozen=True)
class MetaBlock:
    format: str
    purpose: str
    generated: str
    human: str
    org: str
    contact: str


@dataclass(frozen=True)
class LoadIssue:
    severity: str
    code: str
    message: str
    section: Optional[str] = None


@dataclass(frozen=True)
class ReconstructedState:
    """
    Canonical in-memory representation of a validated SYMB-FER artifact.

    This is the first bridge from raw transfer text to a deterministic runtime state.
    It does not invent values. It only preserves and exposes what is present.
    """

    raw_text: str
    sections: Dict[str, List[str]]
    meta: MetaBlock
    signature: SignatureBlock
    transfer_mode_lines: List[str]
    parse_guide_lines: List[str]
    time_collab_lines: List[str]
    boot_facts_lines: List[str]
    boot_ethos_lines: List[str]
    integrity_lines: List[str]
    finalization_lines: List[str]
    lessons_learned_lines: List[str]
    drift_check_lines: List[str]
    test_trace_lines: List[str]
    issues: List[LoadIssue] = field(default_factory=list)
    status: LoadStatus = LoadStatus.OK


@dataclass(frozen=True)
class ValidationResult:
    passes: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    failures: List[str] = field(default_factory=list)

    @property
    def status(self) -> str:
        if self.failures:
            return "FAIL"
        if self.warnings:
            return "WARN"
        return "PASS"


@dataclass(frozen=True)
class ProcessedArtifact:
    validation: ValidationResult
    state: Optional[ReconstructedState]
    raw_bytes: bytes
    raw_text: str

    @property
    def status(self) -> str:
        if self.validation.failures:
            return "FAIL"
        if self.state is None:
            return "FAIL"
        if self.validation.warnings or self.state.status == LoadStatus.WARN:
            return "WARN"
        return "PASS"

@dataclass(frozen=True)
class SectionDiff:
    section: str
    old_lines: List[str]
    new_lines: List[str]

    @property
    def changed(self) -> bool:
        return self.old_lines != self.new_lines

@dataclass(frozen=True)
class DiffResult:
    old_path: str
    new_path: str
    old_status: str
    new_status: str
    added_sections: List[str] = field(default_factory=list)
    removed_sections: List[str] = field(default_factory=list)
    changed_sections: List[SectionDiff] = field(default_factory=list)

    @property
    def has_differences(self) -> bool:
        return bool(self.added_sections or self.removed_sections or self.changed_sections)

@dataclass(frozen=True)
class LoaderContract:
    """
    Required behavioral contract for any SYMB-FER loader implementation.

    Rules:
    1. Never derive identity fields.
    2. Never normalize preserved lines.
    3. Never invent missing timestamps, hashes, or metadata.
    4. Preserve section line order exactly as loaded.
    5. Return issues explicitly instead of silently repairing content.
    """

    version: str = "phase-2-loader-contract-v1"
    byte_preservation_required: bool = True
    identity_derivation_forbidden: bool = True
    silent_repair_forbidden: bool = True
    time_guessing_forbidden: bool = True
    sha_generation_forbidden: bool = True


def expected_runtime_goal() -> str:
    return (
        "Load a validated SYMB-FER artifact into a deterministic in-memory state "
        "without modifying, reinterpreting, or regenerating preserved content."
    )


CANONICAL_SECTIONS = [
    "TRANSFER·MODE",
    "ARCHIVE·PRINCIPLE",
    "META",
    "PARSE·GUIDE",
    "TIME·COLLAB",
    "BOOT·FACTS",
    "SESSION·STATE",
    "BOOT·ETHOS",
    "INTEGRITY",
    "FINALIZATION",
    "LESSONS·LEARNED",
    "DRIFT·CHECK",
    "TEST·TRACE",
    "SIG",
]

REQUIRED_RULE_LINES = [
    "RULE: preserve·identity·fields·exactly·as·provided·no·abbreviation·no·normalization·no·formatting·changes",
    "RULE: identity·fields·in·§META·are·immutable·after·initial·set·no·modification·or·regeneration·under·any·mode",
    "RULE: identity·fields·override·all·generation·logic·and·must·never·be·derived·or·reconstructed",
    "RULE: all·content·outside·§SIG·must·remain·byte-preserved·unless·the·operator·explicitly·requests·an·edit",
    "RULE: if·any·modification·is·made·the·system·must·explicitly·declare·non-compliance·before·output",
    "RULE: VERIFIED·mode·must·not·require·SHA256·for·execution·only·for·external·verification",
    "RULE: never·guess·time",
    "RULE: absence·of·verified·time·must·not·block·non-time-dependent·execution",
    "RULE: boot·facts·must·remain·verbatim·no·summarization·no·compression·no·reinterpretation",
    "RULE: boot·facts·override·all·model·inference·and·must·not·be·regenerated",
    "RULE: SHA256·is·optional·verification·fingerprint·not·required·for·operation",
    "RULE: system·must·not·self-generate·or·assume·SHA256·value",
    "RULE: VERIFIED·status·requires·external·operator·execution·only",
    "RULE: absence·of·SHA256·must·not·block·execution·or·transfer",
]

SECTION_ORDER = [
    "TRANSFER·MODE",
    "ARCHIVE·PRINCIPLE",
    "META",
    "PARSE·GUIDE",
    "TIME·COLLAB",
    "BOOT·FACTS",
    "SESSION·STATE",
    "BOOT·ETHOS",
    "INTEGRITY",
    "FINALIZATION",
    "LESSONS·LEARNED",
    "DRIFT·CHECK",
    "TEST·TRACE",
    "SIG",
]

def _parse_key_value_lines(lines: List[str]) -> Dict[str, str]:
    data: Dict[str, str] = {}
    for line in lines:
        if ": " in line:
            key, value = line.split(": ", 1)
        elif ":" in line:
            key, value = line.split(":", 1)
        else:
            continue
        data[key.strip()] = value.strip()
    return data


def _extract_sections(raw_text: str) -> tuple[Dict[str, List[str]], List[LoadIssue]]:
    lines = raw_text.splitlines()
    sections: Dict[str, List[str]] = {}
    issues: List[LoadIssue] = []

    current_name: Optional[str] = None
    current_lines: List[str] = []

    for idx, line in enumerate(lines, start=1):
        begin_match = BEGIN_RE.match(line)
        if begin_match:
            name = begin_match.group(1)
            if current_name is not None:
                issues.append(
                    LoadIssue(
                        severity="FAIL",
                        code="NESTED_SECTION",
                        message=f"Nested section begin encountered before closing {current_name}",
                        section=current_name,
                    )
                )
            current_name = name
            current_lines = []
            continue

        end_match = END_RE.match(line)
        if end_match:
            end_name = end_match.group(1)
            if current_name is None:
                issues.append(
                    LoadIssue(
                        severity="FAIL",
                        code="UNMATCHED_SECTION_END",
                        message=f"Unmatched section end for {end_name} at line {idx}",
                        section=end_name,
                    )
                )
                continue

            if end_name != current_name:
                issues.append(
                    LoadIssue(
                        severity="FAIL",
                        code="SECTION_NAME_MISMATCH",
                        message=f"Section end {end_name} does not match open section {current_name}",
                        section=current_name,
                    )
                )
                current_name = None
                current_lines = []
                continue

            sections[current_name] = list(current_lines)
            current_name = None
            current_lines = []
            continue

        if current_name is not None:
            current_lines.append(line)

    if current_name is not None:
        issues.append(
            LoadIssue(
                severity="FAIL",
                code="UNCLOSED_SECTION",
                message=f"Section {current_name} was not closed",
                section=current_name,
            )
        )

    return sections, issues


def _status_from_issues(issues: List[LoadIssue]) -> LoadStatus:
    if any(issue.severity == "FAIL" for issue in issues):
        return LoadStatus.FAIL
    if any(issue.severity == "WARN" for issue in issues):
        return LoadStatus.WARN
    return LoadStatus.OK


def _read_text(path: Path) -> tuple[str, bytes]:
    data = path.read_bytes()
    text = data.decode("utf-8")
    return text, data

def detect_version(raw_text: str) -> str:
    """Detect SYMB-FER token version from raw text."""
    if "§TRANSFER·MODE·BEGIN" in raw_text:
        return "v3"
    if "━━━ STATE ━━━" in raw_text or "━━━ GREETING ━━━" in raw_text:
        return "v2"
    if "§META·BEGIN" in raw_text and "§ETHOS·BEGIN" in raw_text:
        return "v2"
    if "∴ SYMB-FER v2.0" in raw_text:
        return "v2"
    return "unknown"

def validate_v2_token(raw_text: str, raw_bytes: Optional[bytes] = None) -> ValidationResult:
    """Lightweight validation for SYMB-FER v2.0 tokens."""
    result = ValidationResult()
    lines = raw_text.splitlines()

    if raw_bytes is not None:
        try:
            raw_bytes.decode("utf-8")
            result.passes.append("UTF-8 decode clean")
        except UnicodeDecodeError as exc:
            result.failures.append(f"UTF-8 decode failed at byte {exc.start}")
            return result

    v2_sections = ["━━━ STATE ━━━", "━━━ GREETING ━━━", "━━━ PROTOCOL ━━━"]
    found = [s for s in v2_sections if s in raw_text]
    if found:
        result.passes.append(f"v2.0 sections present: {len(found)} of {len(v2_sections)}")
    else:
        result.failures.append("v2.0 token: no recognizable sections found")
        return result

    dot_count = sum(line.count("·") for line in lines)
    if dot_count == 0:
        result.warnings.append("delimiter integrity: no middle-dot delimiters found")
    else:
        result.passes.append("Delimiter integrity verified")

    result.warnings.append(
        "v2.0 token detected · valid for operation · not v3.0 compliant · "
        "consider upgrading to v3.0 for full validation"
    )

    return result

def validate_symbfer_text(raw_text: str, raw_bytes: Optional[bytes] = None) -> ValidationResult:
    result = ValidationResult()
    version = detect_version(raw_text)
    if version == "v2":
        return validate_v2_token(raw_text, raw_bytes=raw_bytes)
    lines = raw_text.splitlines()

    if raw_bytes is not None:
        try:
            raw_bytes.decode("utf-8")
            result.passes.append("UTF-8 decode clean")
        except UnicodeDecodeError as exc:
            result.failures.append(f"UTF-8 decode failed at byte {exc.start}")
            return result

    sections, extract_issues = _extract_sections(raw_text)

    for issue in extract_issues:
        result.failures.append(issue.message)

    missing_sections = [name for name in CANONICAL_SECTIONS if name not in sections]
    if missing_sections:
        result.failures.append("missing required sections: " + ", ".join(missing_sections))
    else:
        result.passes.append("Required sections present")

    discovered_order = [name for name in sections.keys() if name in CANONICAL_SECTIONS]
    expected_order = [name for name in CANONICAL_SECTIONS if name in sections]
    if discovered_order != expected_order or any(name not in discovered_order for name in CANONICAL_SECTIONS):
        result.failures.append("section order invalid: expected " + " -> ".join(CANONICAL_SECTIONS))
    else:
        result.passes.append("Section order canonical")

    if not extract_issues and not missing_sections:
        result.passes.append("Begin/end markers matched")

    missing_rules = [line for line in REQUIRED_RULE_LINES if line not in raw_text]
    if missing_rules:
        preview = "; ".join(missing_rules[:3])
        suffix = "" if len(missing_rules) <= 3 else f" ... (+{len(missing_rules)-3} more)"
        result.failures.append("missing required rule lines: " + preview + suffix)
    else:
        result.passes.append("Required rules present")

    dot_count = sum(line.count("·") for line in lines)
    if dot_count == 0:
        result.failures.append("delimiter integrity failed: no middle-dot delimiters found")
    else:
        suspicious = []
        for idx, line in enumerate(lines, start=1):
            if "RULE:" in line and "·" not in line and " " in line:
                suspicious.append(idx)
        if suspicious:
            result.warnings.append(
                "possible delimiter inconsistency on line(s): " + ", ".join(map(str, suspicious[:10]))
            )
        else:
            result.passes.append("Delimiter integrity verified")

    try:
        sig_begin = lines.index("§SIG·BEGIN")
        sig_end = lines.index("§SIG·END")
        if sig_begin >= sig_end:
            result.failures.append("signature block ordering invalid")
        else:
            sig_lines = lines[sig_begin + 1 : sig_end]
            sig_kv = _parse_key_value_lines(sig_lines)
            missing = [key for key in ("MODE", "STATUS", "SHA256") if key not in sig_kv]
            if missing:
                result.failures.append("signature block missing keys: " + ", ".join(missing))
            else:
                sha_value = sig_kv["SHA256"]
                if sha_value and not SHA_RE.fullmatch(sha_value):
                    result.failures.append("SHA256 field malformed: expected 64 lowercase hex chars or blank")
                elif not sha_value:
                    result.warnings.append("SHA256 field empty: allowed, not verified")
                else:
                    result.passes.append("Signature block well-formed")
    except ValueError:
        result.failures.append("signature block missing")

    return result


def load_symbfer_text(raw_text: str) -> ReconstructedState:
    """
    Parse raw SYMB-FER text into deterministic runtime state.

    This loader preserves section line order exactly as given and reports issues
    explicitly. It does not repair, infer, or regenerate missing content.
    """

    sections, issues = _extract_sections(raw_text)

    actual_order = [name for name in SECTION_ORDER if name in sections]
    missing_sections = [name for name in SECTION_ORDER if name not in sections]

    if missing_sections:
        for name in missing_sections:
            issues.append(
                LoadIssue(
                    severity="FAIL",
                    code="MISSING_SECTION",
                    message=f"Required section missing: {name}",
                    section=name,
                )
            )

    discovered_order = [name for name in sections.keys() if name in SECTION_ORDER]
    if discovered_order != actual_order:
        issues.append(
            LoadIssue(
                severity="FAIL",
                code="SECTION_ORDER_INVALID",
                message="Canonical section order violated",
            )
        )

    meta_kv = _parse_key_value_lines(sections.get("META", []))
    sig_kv = _parse_key_value_lines(sections.get("SIG", []))

    meta_required = ["FORMAT", "PURPOSE", "GENERATED", "HUMAN", "ORG", "CONTACT"]
    for key in meta_required:
        if key not in meta_kv:
            issues.append(
                LoadIssue(
                    severity="FAIL",
                    code="META_FIELD_MISSING",
                    message=f"Missing META field: {key}",
                    section="META",
                )
            )

    sig_required = ["MODE", "STATUS", "SHA256"]
    for key in sig_required:
        if key not in sig_kv:
            issues.append(
                LoadIssue(
                    severity="FAIL",
                    code="SIG_FIELD_MISSING",
                    message=f"Missing SIG field: {key}",
                    section="SIG",
                )
            )

    if "SHA256" in sig_kv and sig_kv["SHA256"] == "":
        issues.append(
            LoadIssue(
                severity="WARN",
                code="SIG_SHA256_EMPTY",
                message="SHA256 is blank; allowed but not externally verified",
                section="SIG",
            )
        )

    meta = MetaBlock(
        format=meta_kv.get("FORMAT", ""),
        purpose=meta_kv.get("PURPOSE", ""),
        generated=meta_kv.get("GENERATED", ""),
        human=meta_kv.get("HUMAN", ""),
        org=meta_kv.get("ORG", ""),
        contact=meta_kv.get("CONTACT", ""),
    )

    signature = SignatureBlock(
        mode=sig_kv.get("MODE", ""),
        status=sig_kv.get("STATUS", ""),
        sha256=sig_kv.get("SHA256", ""),
    )

    status = _status_from_issues(issues)

    return ReconstructedState(
        raw_text=raw_text,
        sections=sections,
        meta=meta,
        signature=signature,
        transfer_mode_lines=sections.get("TRANSFER·MODE", []),
        parse_guide_lines=sections.get("PARSE·GUIDE", []),
        time_collab_lines=sections.get("TIME·COLLAB", []),
        boot_facts_lines=sections.get("BOOT·FACTS", []),
        boot_ethos_lines=sections.get("BOOT·ETHOS", []),
        integrity_lines=sections.get("INTEGRITY", []),
        finalization_lines=sections.get("FINALIZATION", []),
        lessons_learned_lines=sections.get("LESSONS·LEARNED", []),
        drift_check_lines=sections.get("DRIFT·CHECK", []),
        test_trace_lines=sections.get("TEST·TRACE", []),
        issues=issues,
        status=status,
    )


def process_symbfer_text(raw_text: str, raw_bytes: Optional[bytes] = None) -> ProcessedArtifact:
    validation = validate_symbfer_text(raw_text, raw_bytes=raw_bytes)
    if validation.failures:
        return ProcessedArtifact(
            validation=validation,
            state=None,
            raw_bytes=raw_bytes or raw_text.encode("utf-8"),
            raw_text=raw_text,
        )

    state = load_symbfer_text(raw_text)
    return ProcessedArtifact(
        validation=validation,
        state=state,
        raw_bytes=raw_bytes or raw_text.encode("utf-8"),
        raw_text=raw_text,
    )


def process_symbfer_file(path: str | Path) -> ProcessedArtifact:
    file_path = Path(path)
    raw_text, raw_bytes = _read_text(file_path)
    return process_symbfer_text(raw_text, raw_bytes=raw_bytes)


def diff_symbfer_files(old_path: str | Path, new_path: str | Path) -> DiffResult:
    old_artifact = process_symbfer_file(old_path)
    new_artifact = process_symbfer_file(new_path)

    old_sections, _ = _extract_sections(old_artifact.raw_text)
    new_sections, _ = _extract_sections(new_artifact.raw_text)

    old_names = set(old_sections.keys())
    new_names = set(new_sections.keys())

    added_sections = sorted(new_names - old_names)
    removed_sections = sorted(old_names - new_names)

    changed_sections: List[SectionDiff] = []
    for section in SECTION_ORDER:
        if section in old_sections and section in new_sections:
            old_lines = old_sections[section]
            new_lines = new_sections[section]
            if old_lines != new_lines:
                changed_sections.append(
                    SectionDiff(
                        section=section,
                        old_lines=old_lines,
                        new_lines=new_lines,
                    )
                )

    return DiffResult(
        old_path=str(old_path),
        new_path=str(new_path),
        old_status=old_artifact.status,
        new_status=new_artifact.status,
        added_sections=added_sections,
        removed_sections=removed_sections,
        changed_sections=changed_sections,
    )

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]

    if len(args) == 1:
        path = args[0]

        try:
            artifact = process_symbfer_file(path)
        except Exception as e:
            print(f"[FATAL] {e}")
            sys.exit(2)

        print("SYMB-FER ENGINE REPORT")
        print(f"FILE: {path}")
        print(f"STATUS: {artifact.status}")
        print()

        print("VALIDATION:")
        for msg in artifact.validation.passes:
            print(f"[PASS] {msg}")
        for msg in artifact.validation.warnings:
            print(f"[WARN] {msg}")
        for msg in artifact.validation.failures:
            print(f"[FAIL] {msg}")

        print()

        if artifact.state:
            print("META:")
            print(f"  HUMAN: {artifact.state.meta.human}")
            print(f"  ORG: {artifact.state.meta.org}")
            print(f"  CONTACT: {artifact.state.meta.contact}")
            print()

            print("SIGNATURE:")
            print(f"  MODE: {artifact.state.signature.mode}")
            print(f"  STATUS: {artifact.state.signature.status}")
            print(f"  SHA256: {artifact.state.signature.sha256}")

    elif len(args) == 3 and args[0] == "--diff":
        old_path = args[1]
        new_path = args[2]

        try:
            diff = diff_symbfer_files(old_path, new_path)
        except Exception as e:
            print(f"[FATAL] {e}")
            sys.exit(2)

        print("SYMB-FER DIFF REPORT")
        print(f"OLD: {diff.old_path} [{diff.old_status}]")
        print(f"NEW: {diff.new_path} [{diff.new_status}]")
        print()

        if diff.changed_sections:
            print("CHANGED SECTIONS:")
            for section_diff in diff.changed_sections:
                print(f"  * {section_diff.section}")

                print("    OLD:")
                for line in section_diff.old_lines:
                    print(f"      - {line}")

                print("    NEW:")
                for line in section_diff.new_lines:
                    print(f"      + {line}")

                print()

    else:
        print("Usage:")
        print("  python symbfer_engine.py <path-to-token.txt>")
        print("  python symbfer_engine.py --diff <old-token.txt> <new-token.txt>")
        sys.exit(2)
