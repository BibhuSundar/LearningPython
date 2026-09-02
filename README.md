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

### ex_03 — Literals & Variables

- **Lab016_Literals.py** — Assigns a literal integer to a variable and shows that an unreferenced expression like `age + 1` has no effect without reassignment.
- **Lab017_Multi_Comment.py** — Using triple-quoted strings as multi-line comments alongside `#` single-line comments.
- **Lab018_Multi_Comments.py** — Combining inline `#` comments with multi-line triple-quoted blocks alongside executable code.
- **Lab019_Data_Type.py** — Placeholder file for data types.
- **Lab020_BuiltIn_Functions.py** — Built-in `pow()` for exponentiation and `abs()` for absolute value.
- **Lab021_UserInput.py** — Reading input with `input()`, which always returns a `str`.
- **Lab022_User_Input_Sum_Of_Two_numbers.py** — Two user inputs converted to `float`, then addition, multiplication, division, and subtraction performed on them.
- **Lab023_Strings.py** — String basics: single/double quotes, `len()`, and the `.upper()` / `.lower()` methods.
- **Lab024_Strings_Conversion.py** — Type conversion between strings and integers using `int()`.
- **Lab025_Strings.py** — String concatenation with `+`, converting numbers via `str()`, and building a full name from parts.
- **Lab026_Literals.py** — Python literal types: decimal, binary (`0b`), octal (`0o`), hex (`0x`), float, string, boolean, and complex.
- **Lab027_Escape_Char.py** — Escape characters inside strings: `\n` (newline), `\t` (tab), and `\b` (backspace).
- **Lab028_String_Double_Single_Diff.py** — Raw strings (`r""`) to prevent escape-sequence interpretation in file paths; single vs. double quotes.
- **Lab029_Task1.py** — Takes three user inputs as floats and performs subtraction, addition, multiplication, and division across all three.
- **Lab030_Task2.py** — Takes two integer inputs and computes the quotient with floor division (`//`) and the remainder with modulo (`%`).

### ex_04 — Operators

- **Lab031_Arth_Op.py** — Basic arithmetic operators `+`, `-`, `/`, `*`.
- **Lab031_Arth_Operators.py** — All seven arithmetic operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`) with variables.
- **Lab031_UnaryOperator.py** — Unary plus (`+65`), unary minus (`-65`), and incrementing a variable by `1`.
- **Lab032_Comparision_Op.py** — Comparison operators `==`, `!=`, `>`, `<`.
- **Lab033_Logic_Operator.py** — Logical operators `and`, `or`, `not`.
- **Lab034_Operators_P2.py** — The exponentiation operator `**`.
- **Lab035_Operators_P4.py** — Floor division `//` (integer quotient) vs. true division `/` (float).
- **Lab036_Operators_Comparsion.py** — The equality operator `==`.
- **Lab037_Operators_Logical.py** — `not` on booleans and comparisons `>`, `<`, `==`, `>=`.
- **Lab038_Operators_Example.py** — `or` and `and` with explicit `True`/`False` values.
- **Lab039_Operators_P8.py** — The inequality operator `!=`.
- **Lab040_Operators_P9.py** — `divmod()`, multiple-assignment unpacking, compound assignment (`+=`, `-=`, `*=`) and the fact that Python has no `++`/`--`.
- **Lab040_Ternary_Operator.py** — The ternary (inline `if`/`else`) operator.
- **Lab040_User_Input_Ternary_Operators.py** — Ternary operator combined with `int(input(...))` to check a user's age.
- **Lab041_Memership_Operator.py** — Membership operators `in` / `not in` with strings.
- **Lab042_Identity_Operaor.py** — Identity operator `is`, checking whether two `[1, 2, 3]` lists are the same object.
- **Lab042_Math.py** — The `math` module: `math.pi`, `math.pow()`, `math.sin()`, `math.cos()`, `math.tan()`.

### ex_05 — Condition Loops

- **Lab043_IF_Condition.py** — Reads an age and uses `if`/`else` to decide club eligibility (age >= 21).
- **Lab043_IF_Condition_Optimized.py** — Optimized version: strips input and validates age range (1–130) with nested `if`/`else`.
- **Lab044_ELSEIF.py** — Nested `if`/`else` (plus a ternary one-liner) to detect even/odd/negative numbers.
- **Lab044_Nested_IF_ELSEIF.py** — Simple `if`/`else` comparing a value against 10.
- **Lab045_If_Else_Condition.py** — Finds the maximum of two user-entered numbers with `if`/`else`.
- **Lab046_if_else_elif.py** — Placeholder file.
- **Lab047_Grade_Calc.py** — Converts a score into a letter grade (A/B/C/D/F) using validation plus nested `if`/`elif`/`else`.

### ex_06 — Switch Match

- **LabSwitch001.py** — Maps an integer day of the week (1–7) to its name using `match`/`case`, with the `_` wildcard for invalid input.
- **LabMatch002.py** — Selects a test type (API, UI, Performance, Security) using `match`/`case` on a string, with a fallback case (Python 3.10+ feature, see prerequisites).

### ex_07 — Loops

**For loops**
- **Lab048_Loop.py** — `range()` for loop printing 1–9, replacing repeated `print` statements.
- **Lab049_For_Loop.py** — Commented experiments with `range()` step values.
- **Lab050_For_Looops.py** — Two-argument `range(3, 5)` printing 3 and 4.
- **Lab051_IQ.py** — Commented `for`/`range` variations.
- **Lab052_IQ2.py** — Prints "Hello World!" 10 times with `range(10)`.
- **LabForReverse.py** — Reverse-range loop printing 10 → 2 in steps of `-2`.
- **LabForUsedRealLife.py** — Simulates running 5 test cases using an f-string inside a loop.

**While loops**
- **Lab053_While.py** — The initialization/condition/updation (ICU) pattern printing 0–10, then 0–9.
- **Lab056_Q.py** — Loops 0–9, printing only the value 6, otherwise "No O/P", with a trace table.
- **LabWhile.py** — Placeholder file.
- **LabWhile_Vs_For.py** — Placeholder file.

**Loop control & IQ**
- **Lab054_For_While_IQ.py** — Loops 0–9 replacing the value 5 with the word "Five".
- **Lab055_For_break.py** — Loops 0–9 and `break`s out entirely when the counter reaches 5.
- **Lab057_Pass_Break.py** — Uses `pass` as a no-op to print only values 5 and 6.
- **Lab058_IQ_Even.py** — Prints all even numbers from 0 to 100 using `i % 2 == 0`.
- **Lab059_Odd_Number.py** — Prints odd numbers 0–9 by skipping evens with `continue`.
- **LabPass_Vs_Continue_059.py** — Contrasts `continue` (skips 3) with `pass` (no-op, prints everything).

## How to Run

Each lab is a standalone Python script. From the repository root, run any file with:

```bash
python src/ex_01_Python_Basics/Lab001_Python_Hello.py
```

## Prerequisites

- Python 3.13 or later (see `pyproject.toml`).
