# Day 15 - PowerShell Detection Regression Testing

## Project
PowerShell Threat Hunting & Detection Engineering

## Objective
Validate the detection logic developed during Days 13-14
against five controlled PowerShell process creation test cases.

## Environment
- Windows 11 home lab
- Windows PowerShell
- Sysmon process creation telemetry
- Experimental Sigma detection rules
- MITRE ATT&CK T1059.001

## Detection Logic
The detection requires two conditions:

1. The executable is powershell.exe or pwsh.exe.
2. The command line contains a recognized encoded-command flag.

The refined local test uses a regular expression requiring
the flag to appear at an argument-like boundary.

## Test Cases

| ID | Scenario | Expected | Result |
|---|---|---|---|
| T01 | Full -EncodedCommand parameter | Match | Pass |
| T02 | Normal PowerShell execution | No match | Pass |
| T03 | Non-PowerShell executable | No match | Pass |
| T04 | Abbreviated -enc parameter | Match | Pass |
| T05 | EncodedCommand embedded in benign text | No match | Pass |

## Regression Testing

Initial Day 15 regression: 4/5 passed.

The T05 case produced a false positive because a substring
search matched EncodedCommand within ordinary text.

After refining the local regex, all five tests passed.

Final local regex validation: 5/5 passed.

## Important Limitations
- Tests use a small, controlled dataset.
- The final regex has not been validated against production data.
- Quoting and additional parameter variants require testing.
- Sigma backend execution has not yet been confirmed.
- Encoded PowerShell execution is not automatically malicious.

## Evidence
- sanitized-results.csv

## Conclusion
This exercise demonstrated regression testing, false-positive
analysis, detection logic refinement, and documentation.

The project remains experimental and is not production-ready.
