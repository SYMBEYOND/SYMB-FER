∴SYMB-FER·TEMPLATE·v3.2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

§TRANSFER·MODE·BEGIN
MODE: STANDARD
OPTIONS: STANDARD·VERIFIED
RULE: STANDARD·copy-paste·only
RULE: VERIFIED·optional·integrity·hardening
RULE: preserve·identity·fields·exactly·as·provided·no·abbreviation·no·normalization·no·formatting·changes
RULE: identity·fields·in·§META·are·immutable·after·initial·set·no·modification·or·regeneration·under·any·mode
RULE: identity·fields·override·all·generation·logic·and·must·never·be·derived·or·reconstructed
RULE: all·content·outside·§SIG·must·remain·byte-preserved·unless·the·operator·explicitly·requests·an·edit
RULE: if·any·modification·is·made·the·system·must·explicitly·declare·non-compliance·before·output
RULE: VERIFIED·mode·must·not·require·SHA256·for·execution·only·for·external·verification
§TRANSFER·MODE·END

§ARCHIVE·PRINCIPLE·BEGIN
RULE: all·data·is·equal·no·implicit·ranking
RULE: no·data·is·discarded·without·explicit·intent
RULE: unused·data·must·be·preserved·for·posterity
RULE: system·must·not·prune·based·on·assumed·relevance
RULE: archive·integrity·overrides·optimization
RULE: pruning·allowed·only·with·explicit·operator·instruction
§ARCHIVE·PRINCIPLE·END

§META·BEGIN
FORMAT: SYMB-FER·v3.2
PURPOSE: posture+state+identity·transfer
GENERATED: <YYYY-MM-DD_HHMMH>
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
RULE: absence·of·verified·time·must·not·block·non-time-dependent·execution
§TIME·COLLAB·END

§BOOT·FACTS·BEGIN
RULE: boot·facts·must·remain·verbatim·no·summarization·no·compression·no·reinterpretation
RULE: boot·facts·override·all·model·inference·and·must·not·be·regenerated
boot·date·reference: <DATE>
active·project: <PROJECT>
next·action: <ACTION>
§BOOT·FACTS·END

§SESSION·STATE·BEGIN
working·directory: <PATH>
active·paths: <FILE>|<FILE>
recent·actions: <ACTION>|<ACTION>
next·step: <NEXT>
notes: <NOTES>
§SESSION·STATE·END

§BOOT·ETHOS·BEGIN
Simple·always·wins·over·complex
Copy-paste·first·hardening·optional
Transferable·systems·over·one-off·solutions
Collaborator·not·commander
Integrity·must·be·real·not·symbolic
§BOOT·ETHOS·END

§INTEGRITY·BEGIN
ENCODING: UTF-8
NEWLINES: LF·only
DELIMITER: literal·middle·dot·U+00B7
HASH·ALG: SHA-256
HASH·SCOPE: from·first·character·through·last·character·before·§SIG·BEGIN
HASH·EXCLUDES: §SIG·block
WHITESPACE: preserve·exactly
CANONICALIZATION: bytes·as-written
RULE: SHA256·is·optional·verification·fingerprint·not·required·for·operation
RULE: system·must·not·self-generate·or·assume·SHA256·value
RULE: VERIFIED·status·requires·external·operator·execution·only
RULE: absence·of·SHA256·must·not·block·execution·or·transfer
§INTEGRITY·END

§FINALIZATION·BEGIN
STATUS: UNVERIFIED
MODE: WORKING
INSTRUCTION: copy·token·run·one·command·paste·hash·set·VERIFIED
COMMAND·macOS: pbpaste | shasum -a 256
COMMAND·Windows: Get-Clipboard | Get-FileHash -Algorithm SHA256
EXPECTED: 64·char·hex
§FINALIZATION·END

§LESSONS·LEARNED·BEGIN
note: <what·was·learned·this·session>
§LESSONS·LEARNED·END

§DRIFT·CHECK·BEGIN
PURPOSE: prevent·protocol·drift·during·multi-model·transfer
RULE·1: if·drift·detected·re-anchor·to·template
RULE·2: convenience·is·not·permission·to·modify·canonical·fields
RULE·3: interpretation·must·not·override·structure
RULE·4: small·changes·are·still·drift
§DRIFT·CHECK·END

§TEST·TRACE·BEGIN
trace: <session·trace>
§TEST·TRACE·END

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
§SIG·BEGIN
MODE: WORKING
STATUS: UNVERIFIED
SHA256:
§SIG·END
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
