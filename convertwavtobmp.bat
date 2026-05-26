@echo off
: loop
set /p filename="Enter the file name:"
python Utils/generate_beatmap.py "%filename%"
goto loop
