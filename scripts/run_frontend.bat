@echo off
echo Starting React frontend development server...

REM Change directory to the script's location, then to the frontend folder
cd /d "%~dp0..
cd frontend"

echo Running npm run dev in %cd%...
npm run dev

pause
