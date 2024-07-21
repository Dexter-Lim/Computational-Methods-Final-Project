@echo off
setlocal

REM Check if virtual environment is desired
set "USE_VENV="
set /P USE_VENV="Do you want to use a virtual environment? (Y/N): "

if /I "%USE_VENV%"=="Y" (
    REM Create virtual environment
    python -m venv venv

    REM Activate virtual environment
    call venv\Scripts\activate
) else (
    echo Installing globally without virtual environment.
)

REM Install requirements
echo Installing requirements...
pip install -r requirements.txt

echo.
echo Installation complete.

REM Option to uninstall packages
set "UNINSTALL_PACKAGES="
set /P UNINSTALL_PACKAGES="Do you want to uninstall the packages? (Y/N): "

if /I "%UNINSTALL_PACKAGES%"=="Y" (
    echo Uninstalling packages...
    for /F "delims=" %%i in (requirements.txt) do pip uninstall -y %%i
    echo Packages uninstalled.
) else (
    echo Packages were not uninstalled.
)

echo.
echo Done.
endlocal
pause