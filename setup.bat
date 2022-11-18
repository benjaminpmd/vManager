:: This batch file install automatically the python environement used for the project
:: don't print commands
ECHO OFF

ECHO ====================================================================
ECHO This script requiere Python 3, venv, pip and tkinter. 
ECHO Make sure their are installed.
ECHO ====================================================================
ECHO 
ECHO Setting up server environment, it may take some time (~1min)...
python -m venv venv

ECHO Activating server environment...

CALL venv\Scripts\activate.bat
ECHO Installing librairies...
pip install -r requierements.txt
CALL venv\Scripts\deactivate.bat
ECHO ====================================================================
ECHO To run the files, remember to activate python venv
ECHO using 'venv\Scripts\activate.bat'
ECHO ====================================================================