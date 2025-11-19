@echo off
echo Starting FastAPI backend server...

REM Change directory to the script's location, then to the backend folder
cd /d "%~dp0..
cd backend"

echo Running uvicorn in %cd%...
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

pause
