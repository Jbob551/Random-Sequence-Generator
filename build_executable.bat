@echo off
title Build Random Sequence Generator

cd /d "%~dp0"

echo ==========================================
echo   RANDOM SEQUENCE GENERATOR - BUILD
echo ==========================================
echo.
echo Current folder:
cd
echo.

where py >nul 2>nul

if %errorlevel%==0 (
    set PYTHON=py
) else (
    where python >nul 2>nul

    if %errorlevel%==0 (
        set PYTHON=python
    ) else (
        echo ERROR: Python was not found.
        pause
        exit /b 1
    )
)

echo Python found.
echo.

echo Installing/updating PyInstaller...
%PYTHON% -m pip install --upgrade pyinstaller

if %errorlevel% neq 0 (
    echo.
    echo ERROR while installing PyInstaller.
    pause
    exit /b 1
)

echo.
echo Building executable...
echo.

%PYTHON% -m PyInstaller ^
    --noconfirm ^
    --clean ^
    --onefile ^
    --windowed ^
    --name RandomSequenceGenerator ^
    random_sequence_generator.py

if %errorlevel% neq 0 (
    echo.
    echo ==========================================
    echo   ERROR WHILE BUILDING EXECUTABLE
    echo ==========================================
    echo.
    pause
    exit /b 1
)

if not exist data mkdir data

echo.
echo ==========================================
echo   EXECUTABLE CREATED SUCCESSFULLY!
echo ==========================================
echo.
echo Location:
echo %cd%\dist\RandomSequenceGenerator.exe
echo.
pause
