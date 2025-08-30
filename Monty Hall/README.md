# Monty Hall Simulation
This program simulates the Monty Hall problem and calculates the winning percentage based on whether the player decides to switch their initial door choice or stay.
## Project Structure
```
Monty Hall/
│
├── src/
│   ├── Monty_Hall.py - The main game class
│
├── README.md - This file
```
## Requirements
- Python 3.1+

## Running the Project

1. Navigate to the `src` directory.
2. Run the `Monty_Hall.py` file using Python.

```bash
cd src
python Monty_Hall.py
```


## Example Output
```python
if __name__ == "__main__":
    monty_hall(100, True)   # Simulate 100 rounds with switching
    monty_hall(100, False)  # Simulate 100 rounds without switching
```
## Description
The simulation randomly assigns a car and goats behind three doors each round. The host reveals a goat door that the player did not pick. The player either switches to the remaining unopened door or stays with their original choice based on switch_decision. The program calculates and prints the win percentage over the given number of rounds.

---
<p align="center">👧 Author: <b>Mina Jazini</b></p>