# Learning Python

A hands-on repository for learning Python from the ground up. Each topic is explored through small, runnable lab files organized into numbered exercise folders under `src/`.

## Repository Structure

The project is organized into exercise folders, one per topic. Every folder lives inside `src/`.

```
src/
├── ex_01_Python_Basics
├── ex_02_Keywords_Identifier_Variables
├── ex_03_Literals_Variables
├── ex_04_Operators
├── ex_05_Condition_Loops
├── ex_06_Switch_Match
├── ex_07_Loops
├── ex_08_Functions
├── ex_09_Functions_Scopes
├── ex_10_Decortors
├── ex_11_TypeConversion
├── ex_12_Lambda_Function
├── ex_13_List
├── ex_14_Tuple
├── ex_15_Set
├── ex_16_Map_Filters_List
├── ex_17_Dict
├── ex_18_OOps_Python
├── ex_19_Exceptions
├── ex_20_Modules_OS
├── ex_21_Package_vs_DIR
├── ex_22_Collections
└── ex_23_File_IO
```

## Completed So Far

Below is a summary of the topics covered in the repository up to now.

### ex_01 — Python Basics

- **Lab001_Python_Hello.py** — The classic "Hello World!" program, the entry point into Python.
- **Lab002_Comment.py** — How comments work. Lines starting with `#` are ignored by the interpreter and are used to document code.
- **Lab003_print.py** — Deep dive into the `print()` function:
  - Passing multiple comma-separated arguments.
  - Customizing output with `sep` (separator) and `end` (line ending).
  - Mixing different data types in a single `print()` call.
  - Note that `print` is case-sensitive.

### ex_02 — Keywords, Identifiers & Variables

- **Lab004_Keyword.py** — Keywords are reserved words in Python that cannot be used as identifiers. Uses the `keyword` module's `kwlist` to list all of them.
- **Lab005_Variable_Part1.py** — Assigning values to variables and understanding that Python is a **dynamically typed** language (a variable can be reassigned to a different type).
- **Lab006_Identifier.py** — Variables are identifiers and their values are literals. Covers valid identifier naming, including the underscore `_` convention and why names like `123abc` are not allowed.
- **Lab007_Variables_Names.py** — Exploring the built-in `type()` function across `str`, `float`, `bool`, and `complex` types (including `.real` and `.imag`).
- **Lab008_Dynamically_typed.py** — Demonstrates dynamic typing: the same variable changes type across `int` → `str` → `bool`.
- **Lab009_Identifier_Rule.py** — Long, descriptive identifier names with underscores are valid and readable.
- **Lab010_maths.py** — Basic arithmetic with variables (`+`, `-`).
- **Lab011_IQ_BODMAS.py** — Operator precedence and the **BODMAS** rule (Brackets, Order, Division, Multiplication, Addition, Subtraction).
- **Lab012_Multiple_Variables.py** — Placeholder for assigning to multiple variables in one statement.
- **Lab013_Multiple_Prints.py** — Printing multiple values using multiple arguments.
- **Lab014_Math_Functions.py** — Using built-in helper functions `max()` and `min()` which accept an unlimited number of arguments.
- **Lab015_IQ.py** — Python has no implicit string/number concatenation (`"Hello" + 15` fails). You must explicitly convert with `str()` first.

## How to Run

Each lab is a standalone Python script. From the repository root, run any file with:

```bash
python src/ex_01_Python_Basics/Lab001_Python_Hello.py
```

## Prerequisites

- Python 3.9 or later (see `pyproject.toml`).
