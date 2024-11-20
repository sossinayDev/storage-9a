@echo off
start https://www.myinstants.com/media/sounds/virus-indian-song.mp3
@echo off
powershell -Command "(New-Object -ComObject WScript.Shell).SendKeys([char]173); Start-Sleep -Milliseconds 100; For ($i = 0; $i -lt 50; $i++) { (New-Object -ComObject WScript.Shell).SendKeys([char]175) }"
exit
