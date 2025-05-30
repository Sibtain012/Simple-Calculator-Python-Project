# 🧮 PYTHON CONSOLE CALCULATOR

A user-interactive calculator built using Python. Supports basic arithmetic operations and allows continuous calculations with previous results.

---

## 🚀 Built With

* Python 🐍
* ASCII Art logo (`art.py`)
* Terminal/Command Line

---

## 📚 Table of Contents

* [Overview](#overview)
* [Features](#features)
* [How It Works](#how-it-works)
* [How to Run](#how-to-run)
* [Example](#example)
* [Known Issues](#known-issues)

---

## 🧠 Overview

This Python script allows users to perform arithmetic operations (+, -, \*, /) on numbers interactively. After each calculation, users can choose to continue using the result or start over.

---

## ✨ Features

* Displays operation symbols to choose from.
* Performs addition, subtraction, multiplication, and division.
* Handles division by zero with a custom message.
* Allows the user to:

  * Continue calculations with the result.
  * Start a new calculation from scratch.
* Uses ASCII art from `art.py` for visual appeal.

---

## ⚙️ How It Works

1. **Display Logo**
   ASCII art logo is printed at the start using `from art import logo`.

2. **Define Operations**
   Functions are defined for each operation and stored in a dictionary.

3. **User Interaction**

   * Prompts for the first number.
   * Displays operation symbols.
   * Accepts the user's chosen operation and second number.
   * Executes the operation using function mapping.
   * Displays the result and asks whether to continue or restart.

4. **Recursion for Restart**
   If the user chooses to start over, `calculator()` is called recursively.

---

## 🧪 How to Run

```bash
# Ensure Python is installed
python --version

# Make sure these files exist in the same folder:
# - calculator.py (this code)
# - art.py (contains logo variable)

# Run the calculator
python calculator.py
```

---

## 💡 Example

```
What's the first number?: 10
+  
-  
*  
/  
Pick an operation: *
What's the next number?: 5
10.0 * 5.0 = 50.0
Type 'y' to continue calculating with 50.0, or type 'n' to start a new calculation: y
*  
/  
+  
-  
Pick an operation: /
What's the next number?: 0
50.0 / 0.0 = Infinite
```

---

## ⚠️ Known Issues

* ❌ No input validation. Non-numeric input will crash the program.
* ❌ Recursion on `calculator()` restarts can be inefficient for long sessions.

---
