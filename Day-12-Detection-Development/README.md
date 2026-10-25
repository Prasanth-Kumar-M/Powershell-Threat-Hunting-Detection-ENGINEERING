# Day 12 — PowerShell Detection Development

## Project overview

This lab documents the development and evidence-handling workflow for a PowerShell-focused detection investigation in a controlled Windows environment. It is part of the **PowerShell Threat Hunting & Detection Engineering** project (Days 11–14).

**Status:** Public documentation prepared; detection logic, event interpretation, and test outcomes require verification against retained lab evidence.

## Objective

- Examine Windows process-creation telemetry relevant to PowerShell execution.
- Develop and assess detection logic using observed or controlled test cases.
- Distinguish suspicious indicators from confirmed malicious activity.
- Preserve original evidence privately and publish only reviewed, sanitized findings.

## Environment and evidence

The exercise uses Windows lab telemetry. A private Day 12 evidence folder contains an evidence-hash CSV and a Sysmon XML evidence file, as observed in the local file listing. Original XML contents, event IDs, command lines, timestamps, and detection outcomes have **not** been independently verified for this public summary.

## Methodology

1. Collect and preserve relevant telemetry in the controlled lab.
2. Review process image, parent process, command line, and other available fields.
3. Define detection conditions and expected behavior for each test case.
4. Execute controlled positive and negative test cases, where available.
5. Compare actual observations with expectations and record limitations.
6. Sanitize any data selected for public release.

## Results

See [`sanitized-results.csv`](sanitized-results.csv) for a **blank reporting template**. No pass/fail outcome is asserted until test evidence is reviewed. The CSV is not a substitute for the original event records.

## Evidence handling

Original Sysmon XML and hash records are retained locally in `Private-Evidence/Day12` and are intentionally excluded from this public repository. Before publishing additional artifacts, remove or generalize user names, domain names, host names, private IP addresses, SIDs, credentials, and other sensitive details. Preserve original files unchanged and verify hashes when applicable.

## Limitations

- Presence of a PowerShell command or a matching detection condition alone does not establish malicious intent.
- This README does not claim detection accuracy, completeness, or production readiness.
- The original telemetry and exact test cases must be reviewed before reporting validated findings.

## Next steps

- Confirm the Day 12 detection logic and original test outcomes.
- Replace the CSV template rows with verified, sanitized results.
- Document false positives, false negatives, and any rule improvements.
- Link the final Day 12 findings to the Day 13 Sigma rule and Day 14 tuning work.
