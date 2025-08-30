# Python Password Generator

This Python script provides multiple ways to generate secure and useful passwords, depending on your needs:

- Simple numeric PIN codes
- Memorable word-based passwords
- Strong random character passwords



## Features

-  Generate numeric PIN codes
-  Create memorable passwords using English words (uses the `nltk` corpus)
-  Generate complex passwords with letters, digits, and symbols


## Project Structure
```
Generate Password/
│
├── src/
│   ├── generate_pass.py - The main game class
│
├── README.md - This file
├── requirement.txt - This file
```
## Requirements

- Python 3.6+
- `nltk` package

You can install the required library using pip:

```bash
pip install nltk
```

**Note**: The script uses the words corpus from NLTK. If you haven't downloaded it before, you need to run:
```python
import nltk
nltk.download('words')
```

## Running the Project
1. Navigate to the `src` directory.
2. Run the `generate_pass.py` file using Python.

```bash
cd src
python generate_pass.py
```

**You will see output like:**

```kotlin
Testing pin code password!
49103825
Testing memorable password!
book-candle-night-fast-blue-apple-tree-mouse-dream-river
Testing random password!
5zF9@W1!
```

---
<p align="center">👧 Author: <b>Mina Jazini</b></p>