# Day 16 - PowerShell Threat Investigation

## Objective

Investigate an encoded-command indicator using
real Sysmon process creation telemetry.

## Key Results

- Sysmon Event ID 1 examined
- Parent-child relationship confirmed
- Process GUID correlation verified
- High integrity execution observed
- Encoded-command indicator identified
- Two evidence hashes verified

## Investigation Outcome

Authorized lab activity.

The available evidence does not establish
malicious execution.

## Public Artifacts

- investigation-report.md
- sanitized-timeline.csv

## Evidence

Original XML files and evidence hashes are retained
privately and are not included in this repository.

## Next Phase

Day 17 - Sigma detection quality review and
remaining detection coverage assessment.
