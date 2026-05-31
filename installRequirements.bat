@echo off
title Installing TracyPrinter Requirements

cd /d "%~dp0"

echo Upgrading pip...
python -m pip install --upgrade pip

echo.

echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

echo.

echo Installation complete!

echo This batch file will close in 10 seconds...
timeout /t 10