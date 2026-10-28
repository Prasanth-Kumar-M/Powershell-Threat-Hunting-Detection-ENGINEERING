from pathlib import Path
import re
import yaml

folder = Path(__file__).resolve().parent

rule = yaml.safe_load(
    (folder / "day17-boundary-aware-rule.yml").read_text(
        encoding="utf-8-sig"
    )
)

pattern = rule["detection"]["selection_command"]["CommandLine|re|i"]

command = 'powershell.exe -Command Write-Output "hello -enc example"'

actual = bool(re.search(pattern, command, re.IGNORECASE))
expected = False

print("Test: T10 - Quoted string containing -enc")
print("Expected:", expected)
print("Actual:", actual)
print("Passed:", actual == expected)

if actual:
    print("Finding: Potential false positive - indicator inside quoted text")
