# Day 17 - Sigma Detection Quality Validation

## Objective

Validate a boundary-aware Sigma rule for detecting
encoded PowerShell command-line indicators.

## Detection Development

- Day 13: Initial Sigma rule
- Day 14: Added abbreviated encoded-command indicator
- Day 15: Five controlled regression cases passed
- Day 17: Added boundary-aware regex matching

## Validation Results

| Validation | Result |
|---|---|
| pySigma parsing | Passed |
| Splunk backend conversion | Passed |
| Generated SPL queries | 1 |
| Original regression tests | 5/5 |
| Expanded local regex tests | 9/9 |
| Additional quoted-string test | Failed as expected |
| Combined local test results | 9/10 |
| Splunk runtime execution | Not tested |

## Identified Detection Limitation

Test T10 contained a PowerShell command that printed
the quoted text "hello -enc example".

Expected detection: False
Actual detection: True

The boundary-aware regex recognized an encoded-command
indicator inside quoted text, producing a false positive.

## Technical Interpretation

The current detection identifies argument-like strings.
It does not fully parse Windows command-line quoting.

Additional parsing, contextual exclusions, and
backend-specific testing are required before
production deployment.

## Scope and Limitations

- All regression cases were synthetic.
- Local regex simulation was performed using Python.
- Sigma parsing was validated using pySigma.
- Sigma-to-Splunk conversion succeeded.
- Generated SPL was not executed against indexed events.
- No production detection accuracy is claimed.

## Conclusion

The project demonstrates iterative detection engineering:
develop, test, investigate false positives, document
limitations, and prepare for further validation.

Status: Experimental - further validation required.
