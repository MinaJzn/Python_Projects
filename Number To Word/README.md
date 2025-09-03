# Number to Words Converter
This is a simple Python script that converts any integer number (from 0 up to 999,999,999,999) into its English words representation.
## Features
- Converts numbers like `42` to `Forty Two`

- Supports numbers up to 999 billion

- Clean and readable code

- No external libraries required

## How It Works
The script uses three key components:

1. UNDER_20: List of word representations for numbers less than 20

2. TENS: List of tens multiples (Twenty, Thirty, etc.)

3. ABOVE_100: Dictionary mapping of large number denominations like Hundred, Thousand, Million, Billion

The `num_to_word()` function handles:

- Numbers below 20 directly using the list

- Numbers between 20 and 99 by breaking into tens and units

- Numbers 100 and above recursively by finding the largest pivot (e.g., Thousand, Million)

## How to Use
```bash
cd src
python number_to_word.py
```

## Example
```bash
Enter a Number: 1234567
One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven
```

## Range Limitation
- The script only supports non-negative integers up to 999,999,999,999

- If the input number is out of range, it prints: `Number out of range`

---
<p align="center">👧 Author: <b>Mina Jazini</b></p>