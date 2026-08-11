<#
Run this on the machine where the skills actually live (NOT the Infosys
laptop) — the one with C:\Claude Cowork\skills\...

Bundles two Claude Code skills into a single zip on the Desktop:
  claude-skills-bundle.zip
    |- prompty/            (copied from $SourcePrompty below)
    |- sync-up/             (copied from $SourceSyncUp below)
    |- INSTALL-PROMPT.md    (must sit next to this script -- ships as-is)

Copy the zip to the Infosys laptop, unzip it, and hand the contents of
INSTALL-PROMPT.md to Claude Code there as a single prompt.
#>

$ErrorActionPreference = "Stop"

$SourcePrompty = "C:\Claude Cowork\skills\prompty"
$SourceSyncUp  = "C:\Claude Cowork\skills\sync-up"
$PromptFile    = Join-Path $PSScriptRoot "INSTALL-PROMPT.md"
$Staging       = Join-Path $env:TEMP "claude-skills-bundle-$(Get-Random)"
$ZipPath       = Join-Path ([Environment]::GetFolderPath("Desktop")) "claude-skills-bundle.zip"

if (-not (Test-Path $PromptFile)) {
    throw "INSTALL-PROMPT.md not found next to this script at $PromptFile -- keep both files together and re-run."
}

foreach ($src in @($SourcePrompty, $SourceSyncUp)) {
    if (-not (Test-Path $src)) {
        throw "Can't find $src -- edit the path at the top of this script and re-run."
    }
    if (-not (Test-Path (Join-Path $src "SKILL.md"))) {
        Write-Warning "$src has no SKILL.md at its top level -- double-check this is the right folder."
    }
}

New-Item -ItemType Directory -Path $Staging | Out-Null
Copy-Item -Path $SourcePrompty -Destination (Join-Path $Staging "prompty") -Recurse
Copy-Item -Path $SourceSyncUp  -Destination (Join-Path $Staging "sync-up") -Recurse
Copy-Item -Path $PromptFile    -Destination (Join-Path $Staging "INSTALL-PROMPT.md")

if (Test-Path $ZipPath) { Remove-Item $ZipPath -Force }
Compress-Archive -Path (Join-Path $Staging "*") -DestinationPath $ZipPath

Remove-Item $Staging -Recurse -Force

Write-Host "Bundle ready: $ZipPath"
Write-Host "Move this zip to your Infosys laptop, unzip it, then paste INSTALL-PROMPT.md's contents to Claude Code there."
