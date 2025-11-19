@echo off
setlocal
echo ==========================================================
echo           FastAPI Backend Sunucusunu Baslatma
echo ==========================================================
echo.

REM Bu betigin bulundugu klasoru bul (scripts klasoru)
set "SCRIPT_DIR=%~dp0"
echo Betik klasoru: %SCRIPT_DIR%

REM Projenin ana klasorune git (scripts klasorunun bir ust dizini)
set "ROOT_DIR=%SCRIPT_DIR%.."
cd /d "%ROOT_DIR%"
echo Proje ana klasoru: %CD%
echo.

echo Uvicorn sunucusu projenin ana klasorunden baslatiliyor...
echo Bu, Python'un paketleri dogru bulmasi icin gereklidir.
echo Komut: python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
echo.

python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload

echo.
echo Sunucu calisirken loglar bu ekranda gorunecektir.
echo Kapatmak icin CTRL+C tusuna basip pencereyi kapatin.
echo.
pause
