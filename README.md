# Autonomous Chess Robot
This repository contains all of the python files necessary to run the Raspberry Pi integration between stockfish, imaging hardware, and board manipulation hardware. The files are linked such that once installed in the home directory on the Pi, initialize-sequence.py is the only file needed to be executed on startup. main.py calls the necessary functions to calibrate the robot, poll the chess engine, and execute moves.

## Files and Descriptions
* [initialize-sequence.py](/initialize-sequence.py) - Calls all other neccessary files in order
* [gui.py](/gui.py) - Front end of the controll software DEBUG ONLY
* [calibrate.py](/calibrate.py) - Finds the chessboard square corner coordinates
* [execute.py](/execute.py) - Uses board coordinates and a chess board images to determine moves
* [interface.py](/interface.py) - Interfaces with the chess engine to input and receive moves

## Acknowledgements
* **James Steven**
  * Contracts
  * README
  * Hardware
* **Luke Koury**
  * gui.py
