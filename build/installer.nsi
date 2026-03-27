; PresiboFlow Installer Script for NSIS
; Requires NSIS (Nullsoft Scriptable Install System)

!include "MUI2.nsh"

Name "PresiboFlow"
OutFile "PresiboFlow_Setup.exe"
InstallDir "$PROGRAMFILES\PresiboFlow"
RequestExecutionLevel admin

!define MUI_ABORTWARNING

; Pages
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

!insertmacro MUI_LANGUAGE "English"

Section "Install"
    SetOutPath "$INSTDIR"
    
    ; Copy build artifacts from 'dist/PresiboFlow'
    File /r "dist\PresiboFlow\*.*"
    
    ; Create shortcuts
    CreateShortcut "$DESKTOP\PresiboFlow.lnk" "$INSTDIR\PresiboFlow.exe"
    CreateDirectory "$SMPROGRAMS\PresiboFlow"
    CreateShortcut "$SMPROGRAMS\PresiboFlow\PresiboFlow.lnk" "$INSTDIR\PresiboFlow.exe"
    CreateShortcut "$SMPROGRAMS\PresiboFlow\Uninstall.lnk" "$INSTDIR\uninstall.exe"
    
    WriteUninstaller "$INSTDIR\uninstall.exe"
SectionEnd

Section "Uninstall"
    Delete "$DESKTOP\PresiboFlow.lnk"
    RMDir /r "$SMPROGRAMS\PresiboFlow"
    RMDir /r "$INSTDIR"
SectionEnd
