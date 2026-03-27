@echo off
setlocal enabledelayedexpansion

echo ===============================================
echo    Building PresiboFlow Windows EXE
echo ===============================================

REM Check for PyInstaller
where pyinstaller >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [!TIME!] PyInstaller not found. Installing...
    pip install pyinstaller
)

REM Clean previous builds
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

echo [!TIME!] Starting PyInstaller build...

REM We use the .spec file for complex configurations
pyinstaller --clean build/presiboflow.spec

echo.
echo Build finished! 
echo EXE is in: dist\PresiboFlow\
echo.
pause
