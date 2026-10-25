# Day 14 - PowerShell Detection Rule Tuning

## Objective
Improve a PowerShell encoded-command detection through
controlled testing and rule tuning.

## Detection
- Data source: Sysmon Event ID 1
- Technique: MITRE ATT&CK T1059.001
- Detection type: Process creation command-line analysis

## Baseline
Five synthetic test cases were evaluated.

- Passed: 3
- Failed: 2

## Identified Weaknesses
- T04: Abbreviated -enc parameter was missed.
- T05: A command containing the indicator as ordinary
  text was incorrectly detected.

## Tuning
The detection logic was refined to distinguish
PowerShell command-line parameters from ordinary text
and recognize the tested abbreviated parameter.

## Results
After tuning, all five controlled test cases passed.

| Test | Expected | Actual | Result |
|------|----------|--------|--------|
| T01 | True | True | Pass |
| T02 | False | False | Pass |
| T03 | False | False | Pass |
| T04 | True | True | Pass |
| T05 | False | False | Pass |

## Limitations
- Testing used five synthetic scenarios.
- Production telemetry has not been validated.
- Additional parameter variants and benign cases need testing.
- An encoded command is not automatically malicious.

## Conclusion
The exercise demonstrates an iterative detection
engineering workflow: test, identify gaps, tune,
retest, and document limitations.
