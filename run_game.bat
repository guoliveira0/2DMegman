@echo off
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo Ambiente virtual nao encontrado. Criando...
    where python >nul 2>&1
    if not errorlevel 1 (
        python -m venv ".venv"
    ) else (
        py -3 -m venv ".venv"
    )
    if errorlevel 1 (
        echo Nao foi possivel criar o ambiente virtual.
        pause
        exit /b 1
    )

    echo Instalando dependencias...
    ".venv\Scripts\python.exe" -m pip install -r "requirements.txt"
    if errorlevel 1 (
        echo Nao foi possivel instalar as dependencias.
        pause
        exit /b 1
    )
)

".venv\Scripts\python.exe" "GameWindow.py"
if errorlevel 1 pause
