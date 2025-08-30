# Monty Hall Simulation Interactive Dashboard
## Description
This implementation solves the famous Monty Hall problem, presenting an interactive dashboard where you can simulate numerous iterations of the game and visibly note the win percentages in both scenarios, i.e., switching and not switching the chosen door.

## Project Structure
```bash
Monty Hall/
└── Dashboard of monty hall/
    ├── images/
    │   └── Monty Hall.png  
    │ 
    ├── Dashboard.py
    ├── Monty_Hall.py
    ├── README.md
    └── requirement.txt

```
### Prerequisites

- Python 3.6 or later
- Streamlit

To install necessary packages, run `pip install -r requirements.txt.`

## Usage
To start the Streamlit dashboard, run:

`streamlit run Dashboard of monty hall/Dashboard.py`


## Results
On running the Streamlit application, you will see an input field where you can specify the number of games to simulate. The app will then perform a simulation for each game, both where the contestant switches doors and where they don't. Lastly, the dashboard will display the win percentages dynamically as two separate line charts - showing how the likelihood of winning changes based on your decision to switch or not to switch doors.

---
<p align="center">👧 Author: <b>Mina Jazini</b></p>