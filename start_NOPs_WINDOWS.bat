@echo off
set HOUDINI_INSTALL_ROOT=C:\Program Files\Side Effects Software
@REM !NO SPACES BETWEEN = and PATH!
setlocal enabledelayedexpansion

set SCRIPT_DIR=%~dp0
set NOPS=%SCRIPT_DIR%/houdini
set HOUDINI_PACKAGE_DIR=%NOPS%\packages
set HOUDINI_USER_PREF_DIR=%SCRIPT_DIR%\temp_user_pref_dir\__HVER__

REM Set the initial highest version number to 0
set "highestVersion=0"
REM Loop through all the directories in the specified path
for /d %%d in ("!HOUDINI_INSTALL_ROOT!\Houdini 21.*") do (
    REM Get the version number from the last *.num in directory name
    set "version=%%~nxd"
    @REM echo !version!
    REM Remove the "Houdini 21.0." prefix
    set "version=!version:Houdini 21.0.=!"
    REM Compare the version number with the current highest version
    if !version! gtr !highestVersion! (
        set "highestVersion=!version!"
    )
)
REM if highestVersion is still 0, then no Houdini 21.0.* directory was found
if !highestVersion! equ 0 (
    echo No C:\Program Files\Side Effects Software\Houdini 21.0* directories found
    echo Either install h21 or change first line in start_NOPs.bat to the correct the install *ROOT*
    pause
    exit /b
)
echo Launching highest version: 21.0.!highestVersion!
REM Start Houdini with the highest version
start "" "C:\Program Files\Side Effects Software\Houdini 21.0.!highestVersion!\bin\houdini.exe"
