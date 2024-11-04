# Tic-Tac-Toe with Minimax Algorithm (from Harvard CS 50 course)

![GitHub License](https://img.shields.io/github/license/ffenix7/Tick-Tack-Toe)

## Running the Game
Clone the repository:
```bash
git clone https://github.com/ffenix7/tic-tac-toe
cd tick-tack-toe
```
Run the Python file:
```python
python runner.py
````


## Overview

This is an implementation of a Tic-Tac-Toe game in Python, where the player (either X or O) competes against an AI opponent. The AI uses the Minimax algorithm to make its moves, ensuring that it always plays optimally. The game takes place on a 3x3 grid, and the AI will analyze all possible future game states to determine the best move at any given time, making it a challenging opponent for the player.

## Features

- **Initial Game State:** A function that returns the initial empty Tic-Tac-Toe board.
- **Player Turn:** A function that determines whose turn it is based on the current state of the board.
- **Available Actions:** A function that returns all the possible moves a player can make.
- **Result Function:** A function that returns the state of the board after a valid move is made.
- **Winner Detection:** A function that checks if there is a winner.
- **Game Termination:** A function that checks if the game is over (either a player has won or the board is full).
- **Utility Function:** A function that assigns a value to a terminal board state: 
  - `1` if X wins, 
  - `-1` if O wins, 
  - `0` if it's a draw.
- **Minimax Algorithm:** A function that computes the optimal move for the current player using the Minimax algorithm.
- **Invalid Move Handling:** An exception is raised if an invalid move is attempted.

## How it Works

1. **Initial State:**
   - The board is a 3x3 grid initialized with `None` (representing an empty space).
   - X always starts first.

2. **Player Turn:**
   - The game alternates between players based on the current board state. If the number of X moves exceeds the number of O moves, it is O's turn; otherwise, it is X's turn.

3. **Valid Moves:**
   - The `actions()` function returns a list of all valid moves (coordinates of empty cells).

4. **Result of Moves:**
   - The `result()` function takes in the board and a move (a tuple of coordinates) and returns a new board state with the move applied.

5. **Winner Detection:**
   - The `winner()` function checks if any row, column, or diagonal contains the same symbol (either X or O), which would declare that player as the winner.

6. **Game End:**
   - The `terminal()` function checks if the game has ended, either by a win or a draw (no more available moves).

7. **Minimax Algorithm:**
   - The Minimax algorithm recursively evaluates possible future game states to determine the optimal move for the current player, assuming both players play optimally.

## Exception Handling

An `invalidAction` exception is raised if a player attempts to make an invalid move (i.e., selecting a cell that is already occupied).
