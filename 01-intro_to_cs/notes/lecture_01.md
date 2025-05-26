# Lecture 01 - Realtime

A computer only does what you tell it to do. An algorithm is a recipe and the
computer follows recipes.

Syntax validity is a low bar -- just that nouns and verbs are in the correct
configuration, but they may not be static semantically valid. A static type
checker checks for static semantic correctness.

Semantic errors are dynamic and mean that the program does not do what you are
expecting.

When we cast an object to a new type, we are creating a new object, not altering
the existing object (at least in Python).

We combine objects and operators into expressions. An expression evaluates to a
value.

Python evaluates expressions left to right (taking parentheses into account).
Math operators follow BEDMAS.

# MIT 6.100L – Lecture 1 Notes: Introduction to CS and Python

## 📚 Course Overview

### Course Focus

- **Conceptual Knowledge** – via lectures and exams
- **Programming Skill** – via finger exercises
- **Problem Solving Ability** – via problem sets

### Emphasis: **Computational Thinking**

- Thinking algorithmically and applying computation to problem-solving

---

## 🧠 Knowledge Types

### Declarative Knowledge

- Statements of fact
- Example: “The square root of x is y such that y² = x”
- Not executable by computers

### Imperative Knowledge

- A sequence of instructions or a recipe
- Core to programming and computer science

---

## 🔁 Algorithms

### Definition

A **finite, ordered set of steps** for solving a problem.

### Key Components

- **Sequence of steps**
- **Flow of control** (e.g. conditionals, loops)
- **Stopping condition**

### Example

- Newton’s method to approximate square roots:
  1. Start with a guess
  2. Check closeness to desired value
  3. Update guess
  4. Repeat until close enough

---

## 💻 Computers and Programs

### Early Computers

- **Fixed-program computers**: Could not store instructions (e.g. calculators)
- **Stored-program computers** (post-1940s): Could store and execute sequences
  of instructions

### Core Architecture

- **Memory**: Stores data
- **ALU (Arithmetic Logic Unit)**: Performs operations
- **Control Unit**: Executes instructions in sequence

---

## 🧾 Programming Language Concepts

### Syntax vs Semantics

| Term                 | Meaning                                              |
| -------------------- | ---------------------------------------------------- |
| **Syntax**           | Rules about structure (grammar)                      |
| **Static Semantics** | Rules about meaningful expressions (e.g. type rules) |
| **Semantics**        | Actual meaning of the expression                     |

### Primitives in Python

- **int** – Integer values
- **float** – Real numbers (with decimals)
- **bool** – `True` or `False` (case-sensitive)
- **NoneType** – Special type with only one value: `None`

### Type Inspection

```python
type(5)       # int
type(5.0)     # float
type(True)    # bool
```

---

## 🔄 Type Casting

- **`int(x)`** – Converts to integer (truncates floats)
- **`float(x)`** – Converts to float
- **`round(x)`** – Rounds to nearest int (still returns an int)

---

## ➕ Expressions and Operations

### Expression Evaluation

- Expressions evaluate to a **single value**
- That **value** (not the expression) is stored in memory

### Common Operators

| Symbol | Operation      | Notes                         |
| ------ | -------------- | ----------------------------- |
| `+`    | Addition       |                               |
| `-`    | Subtraction    |                               |
| `*`    | Multiplication |                               |
| `/`    | Division       | Always returns `float`        |
| `//`   | Floor Division | Truncates the fractional part |
| `%`    | Modulo         | Returns remainder             |
| `**`   | Exponentiation | `a ** b` = a to the power b   |

### Precedence

1. `**`
2. `*`, `/`, `//`, `%`
3. `+`, `-`

Use parentheses `()` to override.

---

## 🏷 Variables and Assignment

### What is a Variable?

- A **name** bound to a **value**
- Lets you reuse and refer to values in a program

### Assignment Operator: `=`

- **Not equality**
- Right-hand side is evaluated first, then result is **bound** to the name on
  the left

### Valid vs Invalid Examples

```python
x = 6         # Valid
6 = x         # Invalid (can't assign to literal)
xy = 3 + 4    # Valid
x * y = 3     # Invalid (can't assign to an expression)
```

---

## 🧹 Variable Rebinding

- Variables can be **reassigned**:

  ```python
  radius = 2.2
  radius = radius + 1  # Now radius is 3.2
  ```

- Reassignment doesn’t affect other variables:
  ```python
  area = pi * radius ** 2
  radius = 3.2
  # area still reflects the old radius unless recalculated
  ```

---

## ✍️ Code Style and Comments

### Comments

- Start with `#`
- Explain **intent** of code, not what each line does
- Prefer block comments over line-by-line

### Style Tips

- Use **descriptive variable names**
- Avoid single-letter names (`a`, `b`, `x`) unless in short-term loops
- Avoid magic numbers—assign meaningful names

---

## 🐞 Debugging with Python Tutor

- Visual tool to **step through** Python code line by line
- Shows **variable bindings** and execution order
- Great for understanding errors and execution flow

---

## 🔁 Swapping Variables – Example

### Incorrect:

```python
y = x
x = y  # Both x and y now have the same value
```

### Correct:

```python
temp = y
y = x
x = temp
```

---

## 📌 Summary of Key Ideas

- **Programs manipulate objects**
- **Objects have types** that define what operations are valid
- **Expressions** evaluate to a single value
- **Variables** are names bound to values
- The `=` sign is **assignment**, not equality
- Computers **execute instructions exactly as written**, line-by-line

---
