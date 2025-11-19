@echo off
setlocal
echo ==========================================================
echo           React Frontend Sunucusunu Baslatma
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

echo Frontend klasorune geciliyor...
cd frontend
echo Mevcut klasor: %CD%
echo.

echo Gelistirme sunucusu baslatiliyor...
echo Komut: npm run dev
echo.

npm run dev

echo.
echo Sunucu calisirken loglar bu ekranda gorunecektir.
echo Kapatmak icin CTRL+C tusuna basip pencereyi kapatin.
echo.
pause
