# Day 12 — Encoded PowerShell Detection Validation

## Project Overview

This investigation validates a PowerShell command-line
indicator against an actual Sysmon process creation event
collected in an authorized Windows laboratory.

## Objective

Identify PowerShell execution involving the
-EncodedCommand or -enc command-line option.

## Data Source

- Sysmon Event ID 1 — Process Creation
- Windows PowerShell
- Controlled Windows laboratory

## Detection Method

A case-insensitive PowerShell regular expression was
evaluated against the CommandLine field of the event.

The validation checked for the presence of an encoded
PowerShell command-line option.

## Validation Results

| Test ID | Expected | Actual | Passed |
|---------|----------|--------|--------|
| D12-T01 | True | True | True |

The observed event matched the detection indicator.

## Analyst Assessment

The activity was generated within an authorized lab.
The presence of an encoded PowerShell command does not,
by itself, establish malicious intent.

Disposition: Authorized laboratory activity.

## Limitations

- One captured positive event was validated.
- False-positive and false-negative rates were not measured.
- No production SIEM alert was tested.
- Additional negative and variant tests are required.

## Evidence Handling

Original event XML and evidence hashes remain private.
Only sanitized findings are published.

## Files

- sanitized-results.csv — Validation result
