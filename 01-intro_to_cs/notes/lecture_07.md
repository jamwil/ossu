# MIT 6.100L – Lecture 7 Notes: Functions and Modularity

## 🧱 Abstraction and Decomposition (Revisited)

### Abstraction
- Hide internal implementation details.
- Focus on **inputs and outputs**, not the internal workings.
- Example: a smartphone – user knows buttons and responses, not internal circuits.

### Decomposition
- Break down a complex system into manageable parts.
- Each part handles a specific task and communicates through a defined interface.
- Enables modular development and testing.

---

## 🔧 Functions in Programming

### Purpose
- Encapsulate useful tasks to be reused.
- Hide complexity; expose a clean interface.

### Built-in Examples
- `max(a, b)` – returns the greater of two values.
- `abs(x)` – returns absolute value.
- `len(s)` – returns length of string.

---

## 🛠 Writing Your Own Functions

### Anatomy of a Function
```
def function_name(parameters):
    """Docstring: inputs, purpose, output"""
    # Body (implementation)
    return value
```

### Key Components
- `def` – defines a function
- **Name** – meaningful, typically verb-like
- **Parameters** – input variables (can be zero or more)
- **Docstring** – describes inputs, functionality, output
- **Body** – code that performs the task
- **Return** – sends output back to caller

### Example
```
def is_even(i):
    """Returns True if i is even, False otherwise"""
    return i % 2 == 0
```

---

## 🧪 Calling Functions

### Mechanics
- Calling `is_even(3)` replaces the call with `False`.
- Function must be **defined before called**.
- Can be called multiple times with different inputs.

### Side Note
- If no `return`, Python returns `None` by default.

### Example Usage
```
print(is_even(3))  # prints False
print(is_even(4))  # prints True
```

---

## 🧠 Formal vs Actual Parameters

| Term            | Meaning                         |
|-----------------|----------------------------------|
| **Formal**      | Variable names in function def   |
| **Actual**      | Real values passed during call   |

- `def is_even(i):` – `i` is a formal parameter
- `is_even(3)` – `3` is the actual parameter

---

## 🔄 Functions as Black Boxes

- Once tested, the internals can be ignored.
- Encourages clarity and reuse.
- Think of them as **mini-programs**.

---

## 🛠 Practice: `div_by(n, d)`

### Specification
- Returns `True` if `d` divides `n` evenly.

### Example
```
def div_by(n, d):
    """Return True if d divides n evenly, else False"""
    return n % d == 0
```

---

## 🧠 Functions in Memory

- Functions are **objects**.
- `def is_even(i): ...` stores a reference to code under the name `is_even`.
- Code runs **only on function call**, not on definition.

---

## 🧩 Using Functions in Larger Programs

### Example: Odd/Even Printer
```
for i in range(1, 11):
    if is_even(i):
        print(i, "even")
    else:
        print(i, "odd")
```

- Easy to scale or modify.
- Improves readability and reusability.

---

## 🧪 Practice: `sum_odds(a, b)`

### Task
- Return the sum of odd numbers between and including `a` and `b`.

### Strategy
1. Loop from `a` to `b` (inclusive).
2. Check if each number is odd.
3. Accumulate if true.

### Example
```
def sum_odds(a, b):
    """Returns the sum of all odd integers from a to b inclusive."""
    sum_of_odds = 0
    for i in range(a, b+1):
        if i % 2 == 1:
            sum_of_odds += i
    return sum_of_odds
```

---

## ✅ Summary

- Functions enable **abstraction** and **modular design**.
- Defined once, used many times.
- Good functions include:
  - Clear name
  - Docstring/specification
  - Input parameters
  - Return values
- Improves code clarity, maintainability, and reuse.

Next up: **Functions without return values and function scope**