@echo off
REM Uso: git_push.bat "Mensaje del commit"

IF "%~1"=="" (
    echo Debes ingresar un mensaje de commit.
    exit /b 1
)

git add .
git commit -m "%~1"
git push