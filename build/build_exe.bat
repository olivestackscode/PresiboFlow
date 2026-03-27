@echo off
setlocal enabledelayedexpansion

echo ===============================================
echo    Building PresiboFlow Windows EXE
echo ===============================================

REM Always run from project root (one level up from /build)
cd /d "%~dp0"
cd ..

REM Check for PyInstaller using python module check
python -m PyInstaller --version >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [!TIME!] PyInstaller not found. Installing...
    python -m pip install pyinstaller
)

REM Clean previous builds
if exist build\build_temp rmdir /s /q build\build_temp
if exist dist rmdir /s /q dist

echo [!TIME!] Starting PyInstaller build from: %cd%

REM Run the build using python -m PyInstaller to be more reliable
python -m PyInstaller --clean --workpath build\build_temp build\presiboflow.spec

echo.
echo Build finished! 
echo Your EXE is located in: %cd%\dist\PresiboFlow\
echo.
echo.
echo Build finished! 
echo Your EXE is located in: %cd%\dist\PresiboFlow\
echo.
