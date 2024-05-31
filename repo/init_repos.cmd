@ECHO OFF

PUSHD %~dp0

REM SegRap2023
git clone https://github.com/HiLab-git/SegRap2023
REM SegRap2023: task 1, 3rd place
REM SegRap2023: task 2, 4th place
git clone https://github.com/Kaixiang-Yang/SegRap23
REM SegRap2023: task 1, 6th place
git clone https://github.com/Astarakee/segrap2023

REM hecktor2022
git clone https://github.com/voreille/hecktor/tree/hecktor2022

POPD

ECHO Done!
ECHO.

PAUSE
