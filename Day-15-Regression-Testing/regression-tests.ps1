param(
    [string]$TestPath = "$PSScriptRoot\synthetic-test-cases.csv"
)

$ErrorActionPreference = "Stop"

$tests = @(Import-Csv -Path $TestPath)

$pattern = '(?i)(?:^|\s)-(?:EncodedCommand|enc)(?=\s|$)'

$results = foreach ($test in $tests) {

    $imageMatch = $test.Image -match '(?i)\\(powershell|pwsh)\.exe$'

    $commandMatch = $test.CommandLine -match $pattern

    $actual = [bool]($imageMatch -and $commandMatch)

    $expected = [System.Convert]::ToBoolean($test.Expected)

    [PSCustomObject]@{
        TestId = $test.TestId
        Expected = $expected
        Actual = $actual
        Passed = ($actual -eq $expected)
    }
}

$results | Format-Table -AutoSize

$passed = @($results | Where-Object { $_.Passed }).Count
$total = $results.Count

Write-Host "Regression validation: $passed/$total passed"

$results | Export-Csv `
    -Path "$PSScriptRoot\reproducible-test-results.csv" `
    -NoTypeInformation

if ($passed -ne $total) {
    exit 1
}
