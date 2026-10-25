# Day 11 — PowerShell Process Baseline

## Objective

Establish a baseline of PowerShell-related process creation
activity using Sysmon Event ID 1.

## Environment

- Windows laboratory
- Sysmon process creation telemetry
- PowerShell investigation

## Methodology

Five existing Sysmon Event ID 1 records were examined.

The Image and ParentImage fields were extracted to identify
process lineage.

## Findings

| Process relationship | Observed events |
|---|---:|
| powershell.exe -> Notepad.exe | 4 |
| powershell.exe -> powershell.exe | 1 |
| Total | 5 |

These records were observed on October 25, 2026.

## Analyst Assessment

PowerShell was observed launching Notepad and another
PowerShell process.

These relationships are not inherently malicious.

Additional command-line, user, timing and contextual
analysis would be required to establish intent.

## Limitations

- Five selected records were examined.
- This is not a comprehensive process baseline.
- No detection accuracy or false-positive rate was measured.
- No malicious activity is established by these records.

## Evidence Handling

Original event data remains in the private laboratory.

The public CSV includes only selected, sanitized fields.

## Files

- sanitized-results.csv — Process lineage observations
