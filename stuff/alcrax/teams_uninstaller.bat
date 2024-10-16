@echo off
start https://sossinaydev.github.io/other_pages/sketchy/sketchy.html
msg %username% You won a gift!

echo start cmd /k "color 2 & cd C:/ & tree & msg %username% Access granted!" > fun2.bat
echo timeout /t 3 /nobreak  >> fun2.bat
echo start cmd /k "color 16 & cd C:/ & tree  & msg %username% Files transferred!" >> fun2.bat
echo timeout /t 3 /nobreak  >> fun2.bat
echo start cmd /k "color 4 & cd C:/ & tree  & msg %username% Files removed!" >> fun2.bat
echo del "fun2.bat" >> fun2.bat


del "teams_uninstaller.bat"