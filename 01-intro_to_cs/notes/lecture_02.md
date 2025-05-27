# MIT 6.100L – Lecture 2 Notes: Strings, I/O, and Conditionals

## 📦 Review from Lecture 1
- **Objects** have types, determining valid operations.
- **Variables** are names bound to values (objects).
- **Expressions** combine objects using operators or commands and evaluate to a value.
- **Memory model**: assignment creates a new object, not modifies old ones.

---

## 🔤 Strings in Python

### String Basics
- A **string** is a sequence of characters enclosed in quotes (`"..."` or `'...'`).
- Strings are **case-sensitive**.
- Common operations:
  - **Concatenation**: `"me" + "self"` → `"meself"`
  - **Repetition**: `"ha" * 3` → `"hahaha"`

### String Indexing and Slicing
- Indexing: `s[i]` accesses character at index `i`, where indexing starts at **0**
  - Negative indices: `s[-1]` is last character
- Slicing: `s[start:stop:step]` returns substring
  - Omitting step implies `step = 1`
  - Stop is **exclusive**
  - Example: `s[1:4:2]` → characters at indices 1 and 3

### Common String Functions
- `len(s)`: returns length of string
- Strings are **immutable**: they cannot be changed in place

---

## 🖨 Output in Python

### `print()` Function
- Explicitly outputs to the console
- Multiple objects separated by commas → printed with space between
- For string concatenation with other types, cast using `str()` or use **f-strings**

### f-Strings
- Format: `f"Text {expression} more text"`
- Expressions inside `{}` are evaluated and inserted into the string
- No need to cast explicitly

---

## ⌨ Input in Python

### `input()` Function
- Pauses and waits for user input
- Always returns a **string**
- Use `int()`, `float()` to cast input to numbers
```python
x = int(input("Enter a number: "))
```

---

## 🔁 Conditionals

### Equality and Relational Operators
- `==`: equal
- `!=`: not equal
- `<`, `<=`, `>`, `>=`: relational comparisons
- Work with numbers, strings, etc.

### Boolean Operators
- `and`: both conditions must be true
- `or`: at least one condition must be true
- `not`: logical negation

### Conditionals Syntax
```python
if condition:
    # block

if condition:
    # block
else:
    # alternative block

if condition1:
    # block1
elif condition2:
    # block2
else:
    # fallback block
```

### Nesting and Structure
- Code inside `if`, `elif`, `else` is indented (Python uses indentation to define blocks)
- `elif` prevents multiple branches from running (first match wins)
- Use `else` for a fallback
- Avoid using multiple `if`s unless all conditions should be independently checked

---

## 🛠 Example: Number Guessing
```python
secret = 5
guess = int(input("Guess the number: "))

if guess > secret:
    print("Too high")
elif guess == secret:
    print("Correct!")
else:
    print("Too low")
```

---

## ✅ Summary
- Strings are sequences of characters; use slicing/indexing to manipulate them.
- `print()` and `input()` allow for user interaction.
- Casting input is important when working with numbers.
- Use conditionals to branch program logic based on Boolean expressions.
- Practice writing programs that take input, make decisions, and produce meaningful output.

Next lecture: **Loops and Repetition**