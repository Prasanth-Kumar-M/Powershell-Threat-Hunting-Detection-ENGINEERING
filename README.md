# PowerShell Threat Hunting & Detection Engineering

## Project Overview

A four-day cybersecurity homelab project focused on investigating PowerShell execution behavior, developing detection logic, validating controlled test cases, and tuning Sigma detection rules.

The project demonstrates a practical SOC and detection engineering workflow, from identifying potentially suspicious behavior to testing and improving detection logic.

## Project Workflow

| Day | Focus |
|---|---|
| Day 11 | PowerShell threat hunting and investigation |
| Day 12 | Detection development and validation |
| Day 13 | Initial Sigma detection rule |
| Day 14 | Rule tuning, testing, and evaluation |

## Technologies

- Windows PowerShell
- Windows process creation telemetry
- Sysmon
- Sigma detection rules
- MITRE ATT&CK T1059.001
- PowerShell scripting
- CSV-based test validation
- SHA-256 evidence integrity verification

## Day 14 — Detection Validation

The Day 14 local validation suite produced **5/5 passing test cases**, including positive and negative test scenarios.

These results demonstrate agreement with the expected outcomes for the five controlled tests. They do not establish detection accuracy across real-world environments.

## Detection Engineering Approach

1. Investigate process execution behavior.
2. Identify relevant detection indicators.
3. Develop initial detection logic.
4. Test against controlled examples.
5. Tune the rule and review false-positive considerations.
6. Document results and limitations.

## Evidence Handling

Public artifacts are reviewed for sensitive information before publication. Original evidence is retained privately.

## Limitations

This is a controlled homelab project. Detection results require additional validation against broader telemetry, legitimate administrative activity, and diverse adversary behaviors before production use.

## Project Status

Days 13–14: Public artifacts uploaded; repository organization in progress.

Days 11–12: Pending publication.
