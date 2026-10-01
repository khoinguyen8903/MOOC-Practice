$cli = "C:\Users\lengo\AppData\Roaming\Code\User\globalStorage\moocfi.test-my-code\cli\tmc-langs-cli-x86_64-pc-windows-msvc-0.39.4.exe"
$baseDir = "D:\TMCProjects\tmcdata\mooc-java-programming-i"

$configContent = Get-Content (Join-Path $baseDir "course_config.toml")
$partExercises = @()

$currentPath = ""
foreach ($line in $configContent) {
    if ($line -match '^\[exercises\."(part04-[^"]+)"\]$') {
        $currentPath = $matches[1]
    } elseif ($line -match '^id = (\d+)$' -and $currentPath -ne "") {
        $partExercises += @{ id = $matches[1]; path = $currentPath }
        $currentPath = ""
    }
}

foreach ($ex in $partExercises) {
    Write-Host "Submitting $($ex.path) (ID: $($ex.id))..."
    $fullPath = Join-Path $baseDir $ex.path
    $output = & $cli tmc --client-name vscode_plugin --client-version 1.0.0 submit --dont-block --submission-path $fullPath --exercise-id $ex.id
    if ($output -match '"status":"(ok|processing)"' -or $output -match '"show_submission_url"') {
        Write-Host " - Submission sent."
    } else {
        Write-Host " - Result: $output"
    }
    Start-Sleep -Seconds 2 # delay to prevent 503
}
Write-Host "All submissions for part 4 processed."
