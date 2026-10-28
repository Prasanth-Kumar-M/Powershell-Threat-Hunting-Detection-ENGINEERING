# PowerShell Threat Hunting & Detection Engineering

### From Windows Telemetry to Sigma Detection Validation

**Project Status:** Completed Experimental V1 | Further SIEM Validation Planned

## 1. Project Overview

This project demonstrates an end-to-end PowerShell threat hunting and detection engineering workflow using a Windows cybersecurity home lab.

The objective was to investigate PowerShell process execution, develop detection logic for encoded PowerShell commands, validate detections against controlled scenarios, identify false positives, and improve rule reliability through iterative testing.

The project combines SOC investigation techniques, Windows endpoint telemetry, detection engineering, Sigma rules, Python-based validation, and evidence integrity verification.

**Key learning:** A detection rule is not reliable simply because it generates an alert. Its behavior must be tested, investigated, and documented.

## 2. Lab Environment and Technologies

| Technology | Purpose |
|---|---|
| VirtualBox | Virtualized cybersecurity lab |
| Windows 11 | Monitored endpoint |
| Windows Server 2022 | Existing Active Directory lab environment |
| Sysmon Event ID 1 | Process creation telemetry |
| PowerShell Event ID 4104 | Script Block Logging investigation |
| Windows Security Event ID 4688 | Additional process creation telemetry |
| PowerShell | Investigation and detection scripting |
| Python | Automated regression testing |
| Sigma | Portable detection rule development |
| pySigma | Sigma YAML parsing and validation |
| Splunk backend | Conversion of Sigma rules into SPL |
| MITRE ATT&CK | Detection technique mapping |

**MITRE ATT&CK:** T1059.001 — PowerShell

## 3. Detection Engineering Workflow

**Collect → Investigate → Detect → Test → Tune → Validate → Document**

The project followed eight stages:

| Day | Focus | Outcome |
|---|---|---|
| 11 | PowerShell Process Baseline | Investigated parent-child process relationships |
| 12 | Encoded PowerShell Investigation | Verified an encoded-command indicator in real Sysmon telemetry |
| 13 | Sigma Rule Development | Created an experimental detection rule |
| 14 | Detection Rule Tuning | Extended detection coverage and validated five controlled scenarios |
| 15 | Regression Testing | Refined local matching logic and passed 5/5 tests |
| 16 | SOC Threat Investigation | Confirmed process lineage using Sysmon Process GUIDs |
| 17 | Sigma Quality Validation | Parsed Sigma, generated SPL, and identified a quoted-string false positive |
| 18 | Final Project Review | Organized public artifacts, documentation, and release preparation |

## 4. Detection Development

### Initial Detection

The original rule identified PowerShell process creation events containing the full `-EncodedCommand` argument.

The rule used two conditions:

1. The process executable must be `powershell.exe` or `pwsh.exe`.
2. The command line must contain the selected encoded-command indicator.

### Detection Tuning

Additional testing revealed two important limitations:

- Shortened encoded-command parameters could be missed.
- Plain substring matching could flag benign command text.

The rule was subsequently extended to cover the tested `-enc` abbreviation and refined using argument-boundary-aware regular expressions.

The improved matching logic was incorporated into an experimental Sigma rule.

**Limitation:** The regex is not a complete Windows command-line parser.

## 5. Detection Validation Results

### Day 15 - Regression Testing

Five controlled synthetic cases were used to evaluate the revised local detection logic.

| Test | Scenario | Result |
|---|---|---|
| T01 | Full `-EncodedCommand` argument | Passed |
| T02 | Normal PowerShell execution | Passed |
| T03 | Non-PowerShell executable | Passed |
| T04 | Abbreviated `-enc` argument | Passed |
| T05 | Indicator embedded in benign text | Passed |

**Result: 5/5 controlled tests passed.**

### Day 17 - Expanded Detection Validation

The testing scope was expanded to include case variations, whitespace handling, and quoted-string scenarios.

| Validation | Result |
|---|---|
| Initial expanded regex tests | 9/9 passed |
| Additional quoted-string test (T10) | Failed |
| Combined test results | 9/10 passed |
| pySigma YAML parsing | Successful |
| Splunk SPL conversion | Successful |
| Generated SPL queries | 1 |
| Live Splunk execution | Not performed |

**Identified false positive:**

The detection matched an encoded-command-like argument inside ordinary quoted text:

`powershell.exe -Command Write-Output "hello -enc example"`

Although this command prints benign text, the regex recognized `-enc` as a matching indicator.

This demonstrates why detection validation must include negative test cases and why command-line context matters.

**The results represent controlled testing, not production detection accuracy.**

## 6. SOC Investigation - Sysmon Process Correlation

A controlled encoded PowerShell execution was investigated using actual Sysmon Event ID 1 telemetry.

### Observed Process Chain

`explorer.exe → powershell.exe → powershell.exe`

### Investigation Findings

- Confirmed PowerShell parent-child execution.
- Verified the parent-child relationship using Sysmon Process GUIDs.
- Identified an encoded-command indicator in the child process command line.
- Observed High integrity execution.
- Reconstructed the process creation timeline.
- Confirmed that the two events were approximately 119 minutes apart.
- Preserved two original XML evidence records and verified both SHA-256 hashes.

### Investigation Disposition

**Authorized laboratory activity.**

The observed encoded-command indicator was part of controlled testing. The evidence examined did not establish malicious execution.

The investigation demonstrated how a SOC analyst can distinguish a detection indicator from a confirmed security incident.

## 7. Evidence Integrity and Handling

Original Sysmon event XML files were preserved privately.

SHA-256 hashing was used to establish and verify the integrity of the preserved evidence.

Public documentation excludes private usernames, hostnames, internal IP addresses, raw event logs, and complete sensitive command-line content.

Synthetic validation results are distinguished from real Sysmon telemetry.

## 8. Project Repository Structure

```text
PowerShell-Threat-Hunting/
├── README.md
├── Day11-PowerShell-Baseline/
├── Day12-Encoded-PowerShell/
├── Day13-Sigma-Rule/
├── Day-14-Rule-Tuning/
├── Day15-Regression-Testing/
├── Day16-Threat-Investigation/
└── Day17-Detection-Validation/
```

Each folder contains the corresponding investigation, detection, validation, or documentation artifacts.

## 9. Skills Demonstrated

- SOC Alert Investigation
- Threat Hunting
- Windows Endpoint Telemetry
- Sysmon Process Analysis
- Parent-Child Process Correlation
- Detection Engineering
- Sigma Rule Development
- PowerShell Scripting
- Python Regression Testing
- False-Positive Analysis
- MITRE ATT&CK Mapping
- Evidence Integrity Verification
- Technical Investigation Reporting

## 10. Known Limitations

The project is an experimental home-lab implementation.

- The generated SPL was not executed against indexed Splunk telemetry.
- Production detection accuracy has not been measured.
- The detection does not fully understand quoted command-line arguments.
- Additional encoded-command parameter variations require testing.
- Legitimate administrative automation may produce detection matches.
- Broader endpoint coverage and operational alert triage remain future work.

## 11. Future Enhancements

- Deploy Splunk and ingest Sysmon telemetry.
- Execute and validate the generated SPL against indexed events.
- Expand command-line parsing and negative testing.
- Correlate process events with PowerShell Script Block Logging.
- Add alert investigation and triage workflows.
- Integrate the detection with an automated SOC investigation pipeline.

## 12. Final Takeaway

This project strengthened my understanding of how detection engineering connects security monitoring, threat hunting, investigation, rule development, testing, and evidence handling.

The biggest lesson was that **detection engineering is not about making every test pass. It is about understanding why detections succeed, why they fail, and how to improve them without overstating their reliability.**

---

**Project Type:** Independent Cybersecurity Home Lab

**Focus:** SOC Operations | Threat Hunting | Detection Engineering | Incident Response

**Project Status:** Experimental V1 completed - production and live SIEM validation remain future work.
