@echo off
echo Installing dependencies...

REM Get the script's directory and move to the root project directory
set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%.."

echo.
echo Installing Python dependencies from backend/requirements.txt...
pip install -r backend/requirements.txt
if %errorlevel% neq 0 (
    echo Python dependencies installation failed!
    pause
    exit /b 1
)
echo Python dependencies installed successfully.
echo.

echo Installing frontend dependencies from the frontend folder...
cd frontend
npm install
if %errorlevel% neq 0 (
    echo Frontend dependencies installation failed!
    pause
    exit /b 1
)
cd ..
echo Frontend dependencies installed successfully.
echo.

pause
