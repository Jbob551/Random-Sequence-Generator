@echo off
title Criar Sorteador_Mestrado.exe

cd /d "%~dp0"

echo ==========================================
echo   CRIADOR DO EXECUTAVEL - MESTRADO
echo ==========================================
echo.
echo Pasta atual:
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
        echo ERRO: Python nao foi encontrado.
        pause
        exit /b 1
    )
)

echo Python encontrado.
echo.

echo Instalando/atualizando PyInstaller...
%PYTHON% -m pip install --upgrade pyinstaller

if %errorlevel% neq 0 (
    echo.
    echo ERRO ao instalar o PyInstaller.
    pause
    exit /b 1
)

echo.
echo Criando o executavel...
echo.

%PYTHON% -m PyInstaller ^
    --noconfirm ^
    --clean ^
    --onefile ^
    --windowed ^
    --name Sorteador_Mestrado ^
    Sorteador_Mestrado.py

if %errorlevel% neq 0 (
    echo.
    echo ==========================================
    echo   ERRO AO CRIAR O EXECUTAVEL
    echo ==========================================
    echo.
    pause
    exit /b 1
)

if not exist dados mkdir dados

echo.
echo ==========================================
echo   EXECUTAVEL CRIADO COM SUCESSO!
echo ==========================================
echo.
echo Local:
echo %cd%\dist\Sorteador_Mestrado.exe
echo.
pause
