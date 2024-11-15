@echo off
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://www.myinstants.com/media/sounds/virus-indian-song.mp3', '%TEMP%\s.mp3')"
start wmplayer "%TEMP%\s.mp3"