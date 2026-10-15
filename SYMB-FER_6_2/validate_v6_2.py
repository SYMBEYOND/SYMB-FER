from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional


BEGIN_RE = re.compile(r"^§([A-Z0-9·]+)·BEGIN$")
END_RE = re.compile(r"^§([A-Z0-9·]+)·END$")
SHA_RE = re.compile(r"^[0-9a-f]{64}$")

NESTED_ALLOWED_IN = {
    "BOOT·PROTOCOL": {"REFER·TRIGGER", "TIMESTAMP·CALIBRATION", "TIME·ANCHOR"},
}

REQUIRED_SECTIONS = [
    "TRANSFER·MODE",
    "META",
    "PARSE·GUIDE",
    "SAFETY·INTERPRETATION",
    "SYMB2·DOCTRINE",
    "ETHOS",
    "LEXICON",
    "IDENTITY",
    "KEY·RELATIONSHIPS",
    "BOOT·FACTS",
    "BOOT·ETHOS",
    "BOOT·PROTOCOL",
    "REFER·TRIGGER",
    "TIMESTAMP·CALIBRATION",
    "TIME·ANCHOR",
    "SEARCH·PROTOCOL",
    "RELATIONAL·RULES",
    "REF·ENCODING",
    "CORE·CONSTANTS",
    "SACRED·DATES",
    "COLLABORATORS·CREDITED",
    "SCORING·KEY",
    "LANE·STRUCTURE",
    "CURRENT·REALITY",
    "OPEN·THREADS",
    "SESSION·LOG",
    "RESOLVED",
    "CLOSED·MILESTONES",
    "LESSONS·LEARNED",
    "DRIFT·CHECK",
    "INTEGRITY",
    "FINALIZATION",
    "SIG",
]

SECTION_ORDER = [
    "TRANSFER·MODE",
    "META",
    "PARSE·GUIDE",
    "SAFETY·INTERPRETATION",
    "SYMB2·DOCTRINE",
    "ETHOS",
    "LEXICON",
    "IDENTITY",
    "KEY·RELATIONSHIPS",
    "BOOT·FACTS",
    "BOOT·ETHOS",
    "BOOT·PROTOCOL",
    "SEARCH·PROTOCOL",
    "RELATIONAL·RULES",
    "REF·ENCODING",
    "CORE·CONSTANTS",
    "SACRED·DATES",
    "COLLABORATORS·CREDITED",
    "SCORING·KEY",
    "LANE·STRUCTURE",
    "CURRENT·REALITY",
    "OPEN·THREADS",
    "SESSION·LOG",
    "RESOLVED",
    "CLOSED·MILESTONES",
    "LESSONS·LEARNED",
    "DRIFT·CHECK",
    "SYMB·NOTATION",
    "INTEGRITY",
    "FINALIZATION",
    "SIG",
]


class Status(str, Enum):
    PASS = "PASS"
    WARN = "WARN"
    FAIL = "FAIL"


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


def _extract_sections(raw_text: str) -> tuple[Dict[str, List[str]], List[str], List[str]]:
    lines = raw_text.splitlines()
    sections: Dict[str, List[str]] = {}
    errors: List[str] = []
    discovered_order: List[str] = []

    section_stack: List[str] = []
    current_section: Optional[str] = None
    current_lines: List[str] = []

    for idx, line in enumerate(lines, start=1):
        begin_match = BEGIN_RE.match(line)
        if begin_match:
            name = begin_match.group(1)
            if current_section is not None:
                if current_section in NESTED_ALLOWED_IN and name in NESTED_ALLOWED_IN[current_section]:
                    section_stack.append(current_section)
                    sections[current_section] = list(current_lines)
                    current_section = name
                    current_lines = []
                else:
                    errors.append(f"Nested section begin encountered: {name} inside {current_section} (line {idx})")
            else:
                discovered_order.append(name)
                current_section = name
                current_lines = []
            continue

        end_match = END_RE.match(line)
        if end_match:
            end_name = end_match.group(1)
            if current_section is None:
                errors.append(f"Unmatched section end for {end_name} at line {idx}")
                continue

            if end_name != current_section:
                errors.append(f"Section end {end_name} does not match open section {current_section} (line {idx})")
                current_section = None
                current_lines = []
                continue

            sections[current_section] = list(current_lines)
            if section_stack:
                current_section = section_stack.pop()
                current_lines = sections.get(current_section, [])
            else:
                current_section = None
                current_lines = []
            continue

        if current_section is not None:
            current_lines.append(line)

    if current_section is not None:
        errors.append(f"Section {current_section} was not closed")

    return sections, errors, discovered_order


def validate_v6_2(raw_text: str, raw_bytes: Optional[bytes] = None) -> ValidationResult:
    result = ValidationResult()
    lines = raw_text.splitlines()

    if raw_bytes is not None:
        try:
            raw_bytes.decode("utf-8")
            result.passes.append("UTF-8 decode clean")
        except UnicodeDecodeError as exc:
            result.failures.append(f"UTF-8 decode failed at byte {exc.start}")
            return result

    sections, extract_errors, discovered_order = _extract_sections(raw_text)

    for error in extract_errors:
        result.failures.append(error)

    if not extract_errors:
        result.passes.append("Section structure valid")

    missing = [s for s in REQUIRED_SECTIONS if s not in sections]
    if missing:
        result.failures.append(f"Missing required sections: {', '.join(missing)}")
    else:
        result.passes.append("All required sections present")

    expected_order = [s for s in SECTION_ORDER if s in sections]
    if discovered_order != expected_order:
        result.warnings.append("Section order differs from template")
    else:
        result.passes.append("Section order matches template")

    nested_only = {"REFER·TRIGGER", "TIMESTAMP·CALIBRATION", "TIME·ANCHOR"}
    for section_name in discovered_order:
        if section_name in nested_only:
            result.failures.append(f"Nested-only section {section_name} found at top level")

    sha_pattern = None
    if "SIG" in sections:
        for line in sections["SIG"]:
            if line.startswith("SHA256:"):
                sha_value = line.split(":", 1)[1].strip()
                if not sha_value:
                    result.warnings.append("SHA256 field blank: allowed, not verified")
                elif sha_value == "PENDING":
                    result.warnings.append("SHA256 field PENDING: template placeholder, not signed")
                elif SHA_RE.fullmatch(sha_value):
                    result.passes.append("SHA256 field valid")
                else:
                    result.failures.append("SHA256 field malformed: expected 64 lowercase hex chars, blank, or PENDING")
                sha_pattern = sha_value
                break

    if sha_pattern is None:
        result.failures.append("SHA256 field not found in §SIG")

    header_has_v62 = re.search(r"v6\.2(?![0-9])", lines[0]) is not None if lines else False
    meta_has_v62 = False
    token_track_has_v62 = False

    for section_name, section_lines in sections.items():
        if section_name == "META":
            for line in section_lines:
                if "FORMAT:" in line and re.search(r"v6\.2(?![0-9])", line):
                    meta_has_v62 = True
                if "TOKEN·TRACK:" in line and re.search(r"v6\.2(?![0-9])", line):
                    token_track_has_v62 = True

    if header_has_v62 and meta_has_v62 and token_track_has_v62:
        result.passes.append("Version v6.2 consistent across header, META, and TOKEN·TRACK")
    else:
        result.failures.append("Version strings mismatch across header, META FORMAT, and TOKEN·TRACK")

    dot_count = sum(line.count("·") for line in lines)
    if dot_count == 0:
        result.failures.append("No delimiter (middle-dot) found")
    else:
        result.passes.append("Delimiter integrity verified")

    return result


def validate_file(path: str | Path) -> ValidationResult:
    file_path = Path(path)
    raw_bytes = file_path.read_bytes()
    raw_text = raw_bytes.decode("utf-8")
    return validate_v6_2(raw_text, raw_bytes=raw_bytes)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_v6_2.py <path-to-token.txt>")
        sys.exit(2)

    path = sys.argv[1]

    try:
        result = validate_file(path)
    except Exception as e:
        print(f"[FATAL] {e}")
        sys.exit(2)

    print("SYMB-FER v6.2 VALIDATOR")
    print(f"FILE: {path}")
    print(f"STATUS: {result.status}")
    print()

    print("VALIDATION:")
    for msg in result.passes:
        print(f"[PASS] {msg}")
    for msg in result.warnings:
        print(f"[WARN] {msg}")
    for msg in result.failures:
        print(f"[FAIL] {msg}")
    print()

    if result.status == "FAIL":
        sys.exit(1)
    else:
        sys.exit(0)
