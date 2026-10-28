import csv
import re
from pathlib import Path
import yaml

folder = Path(__file__).resolve().parent
rule = yaml.safe_load(
    (folder / "day17-boundary-aware-rule.yml").read_text(
        encoding="utf-8-sig"
    )
)

selection = rule["detection"]["selection_command"]
pattern = selection["CommandLine|re|i"]

image = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
notepad = r"C:\Windows\System32\notepad.exe"

tests = [
    ("T01", image, "powershell.exe -EncodedCommand SQBFAFgA", True),
    ("T02", image, "powershell.exe -Command Get-Date", False),
    ("T03", notepad, "notepad.exe -EncodedCommand SQBFAFgA", False),
    ("T04", image, "powershell.exe -enc SQBFAFgA", True),
    ("T05", image, 'powershell.exe -Command Write-Output "example-EncodedCommand"', False),
    ("T06", image, 'powershell.exe -Command Write-Output "-enc example"', False),
    ("T07", image, "powershell.exe -ENC SQBFAFgA", True),
    ("T08", image, "powershell.exe -Command Write-Output prefix-enc", False),
    ("T09", image, "powershell.exe\t-EncodedCommand SQBFAFgA", True),
]

rows = []

for test_id, exe, command, expected in tests:
    image_match = exe.lower().endswith(
        ("\\powershell.exe", "\\pwsh.exe")
    )
    command_match = bool(re.search(pattern, command, re.IGNORECASE))
    actual = image_match and command_match

    rows.append({
        "TestId": test_id,
        "Expected": expected,
        "Actual": actual,
        "Passed": actual == expected
    })

with (folder / "expanded-test-results.csv").open(
    "w", newline="", encoding="utf-8"
) as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

for row in rows:
    print(
        row["TestId"],
        "Expected:", row["Expected"],
        "Actual:", row["Actual"],
        "Passed:", row["Passed"]
    )

passed = sum(row["Passed"] for row in rows)
print(f"\nExpanded regex validation: {passed}/{len(rows)} passed")
print("Note: Local regex simulation, not Splunk execution.")

