<h1 align="center">🐍 Python Practice</h1>
<p align="center"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/Beginner_Friendly-22C55E?style=for-the-badge&logo=checkmarx&logoColor=white" /> <a href="https://github.com/abhinaba-chanda/python-practice/actions/workflows/test.yml"><img src="https://github.com/abhinaba-chanda/python-practice/actions/workflows/test.yml/badge.svg" alt="tests" /></a></p>

<p align="center">A collection of beginner Python programs I wrote while learning the basics: input/output, conditions, loops, functions, random numbers and saving data to files.</p>

## 📂 Programs

| Program | What it does | Concepts practiced |
|---|---|---|
| [`calculator.py`](calculator.py) | Add, subtract, multiply and divide two numbers, with a divide-by-zero check | functions, `if/elif`, user input |
| [`guess_number.py`](guess_number.py) | The computer picks 1–100 and gives "higher/lower" hints until you guess it | `random`, `while` loops, counters |
| [`fizzbuzz.py`](fizzbuzz.py) | Prints 1–100, replacing multiples of 3/5 with Fizz/Buzz | loops, modulo `%`, string logic |
| [`todo.py`](todo.py) | A command-line to-do list that remembers tasks between runs | lists, dictionaries, JSON files |
| [`temperature_converter.py`](temperature_converter.py) | Converts Celsius to Fahrenheit and back | functions, float maths, `round` |
| [`vowel_counter.py`](vowel_counter.py) | Counts the vowels in a sentence, and how many of each | strings, loops, dictionaries |
| [`leap_year.py`](leap_year.py) | Checks if a year is a leap year (2000 yes, 1900 no) | boolean logic, modulo `%` |
| [`grade_calculator.py`](grade_calculator.py) | Averages marks out of 100 and gives a letter grade | lists, `if/elif`, raising errors |
| [`word_frequency.py`](word_frequency.py) | Finds the most common words in some text | dictionaries, sorting with `key=` |

## ▶️ How to run

```bash
git clone https://github.com/abhinaba-chanda/python-practice.git
cd python-practice
python calculator.py
```

Requires Python 3.8+. No extra libraries needed.

## ✅ Tests

Every exercise with functions has a test in [`tests/`](tests). They run on every push with GitHub Actions.

```bash
pip install pytest
python -m pytest
```

## 🧠 What I learned
- Breaking a problem into small functions
- Validating user input and handling edge cases
- Storing data in JSON so it survives after the program closes
- Writing tests with `pytest` so I know my functions really work

## 🚀 Next ideas
- [ ] Add a scientific mode to the calculator
- [ ] Add difficulty levels to the guessing game
- [ ] Give the to-do app due dates and priorities

---
<p align="center">Made with 💙 by <a href="https://github.com/abhinaba-chanda">Abhinaba</a></p>
