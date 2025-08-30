# Tic Tac Toe
A simple Tic Tac Toe game where you play against the computer in the console using Python.

## Features

- Play as X or O

- Computer chooses random available cells

- Game detects:

    - Player win

    - Computer win

    - Valid input checking

- Clean and readable console output

## Preview
```mathematica
?     ?     ?
?     ?     ?
?     ?     ?

Choose your symbol (X or O): X
Computer choice is O

Write your Row (0-2): 1  
Write your Column (0-2): 1

?     ?     ?
?     X     ?
?     ?     ?

Computer played at (2, 0)

?     ?     ?
?     X     ?
O     ?     ?

```

## Project Structure
```
Tic Tac Toa/
│
├── src/
│   ├── Tic_Tac_Toa.py - The main game class
│
├── README.md - This file
```

## Requirements

- Python 3.1+

## Running the Project

1. Navigate to the `src` directory.
2. Run the `Tic_Tac_Toa.py` file using Python.

```bash
cd src
python Tic_Tac_Toa.py
```

## How It Works
- You choose your symbol (X or O)

- Each turn:

    - You select a cell by entering row & column (0-2)

    - Computer randomly picks an available cell

- The game checks for a winner after every move

---
<p align="center">👧 Author: <b>Mina Jazini</b></p>