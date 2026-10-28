# Day 16 - Encoded PowerShell Investigation

## Investigation Objective

Investigate an encoded PowerShell execution indicator
using Sysmon Event ID 1 and parent-child process correlation.

## Environment

- Windows 11 home lab
- Sysmon process creation logging
- Windows PowerShell
- Controlled, authorized lab activity

## Investigation Timeline

| Stage | Process | Parent | Relative Time |
|---|---|---|---|
| Parent | powershell.exe | explorer.exe | T+0s |
| Child | powershell.exe | powershell.exe | T+7156s |

The interval between process creation events was
119 minutes and 16 seconds.

## Investigation Findings

1. A PowerShell process was launched by explorer.exe.
2. The parent PowerShell process subsequently launched
   another PowerShell process.
3. The child process command line contained an
   encoded-command indicator.
4. The child process ran at High integrity level.
5. Sysmon recorded process and parent process GUIDs.
6. Parent-child correlation was verified using GUIDs.
7. Two preserved XML files passed SHA-256 verification.

## Detection and Investigation

Telemetry source: Sysmon Event ID 1

Indicator: Encoded PowerShell command-line parameter

MITRE ATT&CK: T1059.001 - PowerShell

An encoded-command indicator warrants investigation,
but does not independently establish malicious activity.

## Disposition

Classification: Authorized lab activity.

The activity was generated within a controlled
security testing environment.

No malicious execution has been established from
the evidence examined.

## Limitations

- The encoded payload was not independently analyzed.
- The full process behavior was not reconstructed.
- Two process creation events were correlated.
- The interval does not establish continuous activity.
- Additional related events may exist.
- The detection regex is not a complete command-line parser.
- Findings do not establish production detection coverage.

## Evidence Handling

Original Sysmon XML records are stored privately.

SHA-256 hashes were verified for both preserved files.

The public timeline excludes usernames, hostnames,
full command lines, process IDs and process GUIDs.

## Conclusion

This investigation demonstrates:

- Windows endpoint telemetry analysis
- Sysmon Event ID 1 investigation
- Parent-child process correlation
- Process GUID validation
- Timeline reconstruction
- Evidence integrity verification
- Security investigation documentation
