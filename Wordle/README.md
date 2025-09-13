# Wordle Game 
A fun little **Wordle** clone built in Python that runs in the terminal.  
Test your word-guessing skills in just 6 tries! Can you guess the 5-letter word?

## How It Works
- The program randomly selects a 5-letter word from a predefined list.
- You have **6 attempts** to guess the correct word.
- After each guess, the program gives you feedback:
  - ✅ Correct letters in the **correct position**
  - 🔁 Correct letters in the **wrong position**
- Simple and fun terminal experience!

## Project Structure
```bash
Wordle/
├── src/
│   ├── choose_and_geuss.py
│   ├── valid-wordle-words.txt  # List of valid 5-letter words                
│   └── Wordle_Run.py
└── README.md
```
## Running the Project

1. Navigate to the `src` directory.
2. Run the `Wordle_Run.py` file using Python.

```bash
cd src
python Wordle_Run.py
```
## Example
```bash
Write your guess:usage
👌 u is correct.
👀 e is correct but in wrong place.
Your score is 5

Write your guess: unfed
🥳 Congratulations!
Your geuss correced with 5 score.
```
---
<p align="center">👧 Author: <b>Mina Jazini</b></p>