@echo off
setlocal
set "ROOT=%~dp0"
cd /d "%ROOT%"

rem Only start a server if nothing is already listening on 8743.
netstat -ano | findstr ":8743" | findstr "LISTENING" >nul
if errorlevel 1 (
    start "CCA Prep Server - keep this window open" /min cmd /c "python -m http.server 8743"
    timeout /t 2 /nobreak >nul
)

start "" "http://localhost:8743/index.html"
