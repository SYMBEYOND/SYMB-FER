∴SYMB-FER·TEMPLATE·v3.2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

§TRANSFER·MODE·BEGIN
MODE: STANDARD
OPTIONS: STANDARD·VERIFIED
RULE: STANDARD·copy-paste·only
RULE: VERIFIED·optional·integrity·hardening
§TRANSFER·MODE·END

§META·BEGIN
FORMAT: SYMB-FER·v3.0
PURPOSE: posture+state+identity·transfer
GENERATED: YYYY-MM-DD·TIMEZONE
HUMAN: <NAME>
ORG: <ORG>
CONTACT: <EMAIL>
§META·END

§PARSE·GUIDE·BEGIN
∴ = therefore
λ = condition·must·hold
∧ = AND
! = NOT
· = delimiter
§ = section
>> = next·action
@T = timestamp·YYYY-MM-DD_HHMMH
§PARSE·GUIDE·END

§TIME·COLLAB·BEGIN
PRINCIPLE: Try·to·gather·first.·Ask·only·if·gathering·is·impossible.

PATH·1: native·clock·if·available
PATH·2: authoritative·source·if·available
PATH·3: platform·timestamp
PATH·4: ask·user·once·for·time+timezone

RULE: never·guess·time
§TIME·COLLAB·END

§BOOT·FACTS·BEGIN
boot·date·reference: <DATE>
active·project: <PROJECT>
next·action: <ACTION>
§BOOT·FACTS·END

§BOOT·ETHOS·BEGIN
Simple·always·wins·over·complex
Collaborator·not·commander
Transferable·systems·over·one-off·solutions
§BOOT·ETHOS·END

§INTEGRITY·BEGIN
ENCODING: UTF-8
NEWLINES: LF·only
DELIMITER: literal·middle·dot·[·]
HASH·ALG: SHA-256
HASH·SCOPE: from·first·character·through·last·character·before·§SIG·BEGIN
HASH·EXCLUDES: §SIG·block
WHITESPACE: preserve·exactly
CANONICALIZATION: bytes·as-written
§INTEGRITY·END

§FINALIZATION·BEGIN
STATUS: UNVERIFIED
MODE: WORKING

§LESSONS·LEARNED·BEGIN
note: <what·was·learned·this·session>
§LESSONS·LEARNED·END

§DRIFT·CHECK·BEGIN
status: clean
§DRIFT·CHECK·END

§TEST·TRACE·BEGIN
trace: baseline
§TEST·TRACE·END

INSTRUCTION:
copy·token·run·one·command·paste·hash·set·VERIFIED

COMMAND·macOS:
pbpaste | shasum -a 256

COMMAND·Windows:
Get-Clipboard | Get-FileHash -Algorithm SHA256

EXPECTED: 64·char·hex
§FINALIZATION·END

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
§SIG·BEGIN
MODE: WORKING
STATUS: UNVERIFIED
SHA256: PENDING
§SIG·END
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
