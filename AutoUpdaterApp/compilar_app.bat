@echo off
echo ========================================================
echo Empaquetando la aplicacion Python en un archivo .exe...
echo ========================================================
pip install pyinstaller
pyinstaller --noconfirm --noconsole --onefile --name "Aplicativo_CSC" --icon="app_icon.ico" --add-data "app_icon.ico;." app.py
echo.
echo ========================================================
echo Compilacion terminada. 
echo Tu archivo portable esta dentro de la carpeta 'dist'.
echo ========================================================
pause
