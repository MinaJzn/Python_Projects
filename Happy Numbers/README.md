# Happy Number
In this python project, you'll be diving into the world of "happy" numbers. A number is considered "happy" if by following a specific sequence, it results in 1. The sequence is as follows: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. These numbers for which this process ends in 1 are happy numbers.

For example, 19 is a happy number. Here's why:

- 1² + 9² = 82
- 8² + 2² = 68
- 6² + 8² = 100
- 1² + 0² + 0² = 1

As you can see, we eventually reached 1, which makes 19 a "happy" number. This project tasks you with creating a program that can accurately determine whether any given positive integer is a happy number or not.

## Project Structure

```
Happy Numbers/
│
├── src/
│   ├── Happy_Num.py - The main game class
│
├── README.md - This file
```

## Requirements
- Python 3.1+


## Running the Project
1. Navigate to the `src` directory.
2. Run the `Happy_Num.py` file using Python.

```bash
cd src
python play_game.py
```

## Example Output
```python
Yeah!
"7" is Happy Number!

Oops...
"45" is not Happy Number!
```
## Function Example
```python
Happy_Number(19)  # Yeah! Happy Number
Happy_Number(2)   # Oops... Not Happy Number
```
---
<p align="center">👧 Author: <b>Mina Jazini</b></p>
