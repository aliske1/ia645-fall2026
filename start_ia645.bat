@echo off
echo Starting IA 645 course environment...
echo Once you see the Jupyter output, open your browser to http://localhost:8888
echo.
docker run -p 8888:8888 -v "%~dp0:/course" ia645-base
pause
