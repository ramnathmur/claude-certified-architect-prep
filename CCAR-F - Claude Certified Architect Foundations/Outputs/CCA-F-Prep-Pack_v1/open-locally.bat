@echo off
REM Serves this folder at http://localhost:8000 so browsers treat it as a real site.
REM Only needed if your answers are not saving between sessions -- some browsers
REM restrict local storage for pages opened directly from disk.

cd /d "%~dp0"

where python >nul 2>nul
if errorlevel 1 goto nopython

echo.
echo   Serving the prep pack at http://localhost:8000
echo   Open that address in your browser, then click README.html
echo.
echo   Leave this window open while you study. Close it when you are done.
echo.

start "" "http://localhost:8000/README.html"
python -m http.server 8000
goto end

:nopython
echo.
echo   Python was not found on this machine, so this shortcut cannot run.
echo.
echo   You do not need it: just double-click README.html to open the pack.
echo   Only use this script if your answers are not saving between sessions.
echo.
pause

:end
