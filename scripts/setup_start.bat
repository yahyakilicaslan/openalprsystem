@echo off
setlocal
title Evo Teknoloji Plaka Tanima Sistemi Kurulum Sihirbazi

:CHECK_ADMIN
echo Checking for administrative privileges...
openfiles >nul 2>&1
if %errorlevel% neq 0 (
    echo    This script needs to be run as Administrator.
    echo    Requesting administrative privileges...
    powershell -Command "Start-Process '%0' -Verb RunAs"
    exit /b
)
echo    Administrative privileges confirmed.
echo.

echo ==========================================================
echo # Evo Teknoloji Plaka Tanima Sistemi Kurulumuna Hos Geldiniz #
echo ==========================================================
echo Bu sihirbaz, sistem icin gerekli olan tum bilesenleri
echo (Python, Node.js, MongoDB) kuracak ve uygulamayi
echo calismaya hazir hale getirecektir.
echo.
pause
echo.

set "SCRIPT_DIR=%~dp0"

:INSTALL_CHOCO
echo ----------------------------------------------------------
echo Adim 1: Paket Yoneticisi (Chocolatey) Kontrolu
echo ----------------------------------------------------------
where choco >nul 2>&1
if %errorlevel% neq 0 (
    echo Chocolatey bulunamadi, yukleniyor...
    powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
    set PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin
) else (
    echo Chocolatey zaten kurulu.
)
echo.

:INSTALL_DEPS
echo ----------------------------------------------------------
echo Adim 2: Ana Bagimliliklarin Kurulumu (Python, Node.js, MongoDB)
echo ----------------------------------------------------------
choco install -y python --version=3.10
choco install -y nodejs-lts
choco install -y mongodb-community
echo Ana bagimliliklarin kurulumu tamamlandi.
echo.
pause
echo.

:INSTALL_PROJECT_DEPS
echo ----------------------------------------------------------
echo Adim 3: Proje Bagimliliklarinin Kurulumu
echo ----------------------------------------------------------
call "%SCRIPT_DIR%install_dependencies.bat"
if %errorlevel% neq 0 (
    echo HATA: Proje bagimliliklari kurulurken bir sorun olustu.
    pause
    exit /b 1
)
echo Proje bagimliliklarinin kurulumu tamamlandi.
echo.
pause
echo.

:START_SERVERS
echo ----------------------------------------------------------
echo Adim 4: Sunucularin Baslatilmasi
echo ----------------------------------------------------------
echo Backend ve Frontend sunuculari yeni pencerelerde baslatilacak.
echo Lutfen pencerelerin acilmasini bekleyin.
echo.
start "Backend Sunucusu" cmd /c "%SCRIPT_DIR%run_backend.bat"
start "Frontend Sunucusu" cmd /c "%SCRIPT_DIR%run_frontend.bat"

:FINISH
echo ==========================================================
echo # Kurulum Basariyla Tamamlandi!                          #
echo ==========================================================
echo.
echo - Backend sunucusu bir pencerede calisiyor.
echo - Frontend sunucusu bir pencerede calisiyor.
echo.
echo Uygulamaya erismek icin web tarayicinizda asagidaki adresi acin:
echo http://localhost:5173
echo.
pause
exit /b
