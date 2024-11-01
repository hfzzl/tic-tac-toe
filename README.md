# Tic-Tac-Toe Game

This is a simple command-line implementation of the classic Tic-Tac-Toe game. Players take turns to place their marks ('X' or 'O') on a 3x3 grid until one player wins or the game ends in a tie.

## How to Play

1. Players take turns entering a number between 1 and 9 corresponding to the position on the Tic-Tac-Toe board:

   ```
    1 | 2 | 3
   ---------
    4 | 5 | 6
   ---------
    7 | 8 | 9
   ```

2. The game checks for a win condition after each move. A player wins if they mark three positions in a row (horizontally, vertically, or diagonally).

3. If the board is full and no player has won, the game ends in a tie.

4. Players can choose to play again after a game concludes.

## Features

- Simple command-line interface
- Validates player input
- Detects wins and ties
- Option to restart the game

## Requirements

No external libraries are required. The game is implemented in Python and can be run in any environment that supports Python.

