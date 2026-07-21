@echo off
REM ============================================
REM Script para rodar o projeto Django.
REM Ativa o ambiente virtual e sobe o servidor
REM ============================================

echo Ativando ambiente virtual...
call venv\Scripts\activate.bat

if errorlevel 1 (
    echo ERRO: nao foi possivel ativar o venv.
    echo Verifique se a pasta venv existe nesta pasta.
    pause
    exit /b 1
)
echo VIRTUAL_ENV = %VIRTUAL_ENV%
dir venv\Scripts\python.exe

echo.
echo Ambiente virtual ativado com sucesso!
echo Subindo o servidor Django...
echo.

where python
python -c "import sys; print(sys.executable)"



python manage.py startapp 'nome_do_app'

pause
