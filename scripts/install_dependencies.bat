@echo off
setlocal
echo ==========================================================
echo           Proje Bagimliliklarini Yukleme
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

echo ----------------------------------------------------------
echo Python (Backend) bagimliliklari yukleniyor...
echo Hedef dosya: backend\requirements.txt
echo ----------------------------------------------------------
pip install -r backend\requirements.txt
if %errorlevel% neq 0 (
    echo.
    echo HATA: Python bagimliliklari yuklenemedi!
    echo Lutfen Python ve pip'in dogru kuruldugundan emin olun.
    pause
    exit /b 1
)
echo Python bagimliliklari basariyla yuklendi.
echo.

echo ----------------------------------------------------------
echo Node.js (Frontend) bagimliliklari yukleniyor...
echo Hedef klasor: frontend
echo ----------------------------------------------------------
cd frontend
npm install
if %errorlevel% neq 0 (
    echo.
    echo HATA: Node.js bagimliliklari yuklenemedi!
    echo Lutfen Node.js ve npm'in dogru kuruldugundan emin olun.
    pause
    exit /b 1
)
cd ..
echo Node.js bagimliliklari basariyla yuklendi.
echo.

echo ==========================================================
echo Tum bagimliliklar basariyla kuruldu.
echo ==========================================================
pause
