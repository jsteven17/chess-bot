# Autonomous Chess Robot
This repository contains all of the python files necessary to run the Raspberry Pi integration between stockfish, imaging hardware, and board manipulation hardware. The files are linked such that once installed in the home directory on the Pi, initialize-sequence.py is the only file needed to be executed on startup. main.py calls the necessary functions to calibrate the robot, poll the chess engine, and execute moves.

## Files and Descriptions
* initialize-sequence.py - calls all other neccessary files in order
* gui.py - front end of the controll software DEBUG ONLY
* calibrate.py - finds the chessboard square corner coordinates

## Authors
* James Steven
* Luke Koury
