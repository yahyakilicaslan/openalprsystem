@echo off
echo Installing Python dependencies...
pip install -r backend/requirements.txt
echo.
echo Python dependencies installed successfully.
echo.
echo Installing frontend dependencies...
cd frontend
npm install
cd ..
echo.
echo Frontend dependencies installed successfully.
pause
