@echo off
setlocal

REM Check for administrator rights
openfiles >nul 2>&1
if %errorlevel% neq 0 (
    echo Requesting administrative privileges...
    powershell -Command "Start-Process '%0' -Verb RunAs"
    exit /b
)

echo #############################################################
echo # Evo Teknoloji Plaka Tanima Sistemi Kurulum Sihirbazi     #
echo #############################################################
echo.

REM Check for Chocolatey
where choco >nul 2>&1
if %errorlevel% neq 0 (
    echo Chocolatey bulunamadi, yukleniyor...
    powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
    set PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin
)

REM Install dependencies with Chocolatey
choco install -y python nodejs mongodb-community

echo.
echo #############################################################
echo # Bagimliliklar kuruldu, projenin kurulumuna baslaniyor... #
echo #############################################################
echo.

call install_dependencies.bat

echo.
echo #############################################################
echo # Kurulum tamamlandi! Sunucular baslatiliyor...           #
echo #############################################################
echo.

start "Backend" cmd /c run_backend.bat
start "Frontend" cmd /c run_frontend.bat

echo.
echo Kurulum tamamlandi ve sunucular baslatildi.
pause
