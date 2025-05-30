# MIT 6.100L – Lecture 6 Notes: Bisection Search and Root-Finding Algorithms

## 📌 Review: Approximation Algorithm

### Problems
- Slow for large numbers due to small increments.
- Risk of **infinite loops** if the guess overshoots the acceptable range (`±epsilon`).
- Trade-off between **accuracy** and **performance**.

### Fix
- Add a sanity check using bounds to avoid infinite loops:
```python
while abs(guess**2 - x) >= epsilon and guess**2 <= x:
```

---

## 📚 Motivation for Bisection Search

### Key Insight
- If we know a value is between `low` and `high`, we can **halve** the search space at every step using feedback.

### Requirements
1. **Ordered search space** (e.g., numeric or alphabetic order).
2. **Feedback** on guesses (too high / too low / correct).

---

## 📖 Book Example

- Guess the page number of a hidden bill in a 448-page book.
- Feedback: too high or too low.
- Each guess halves the number of pages to check → **logarithmic search**.

---

## 🔎 Bisection Search Algorithm for Square Roots

### Use Case
- Find square root of `x` such that `guess^2 ≈ x` within `epsilon`.

### Code Sketch
```python
low = 0
high = x
guess = (high + low) / 2.0

while abs(guess**2 - x) >= epsilon:
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0
```

### Runtime
- **Logarithmic**: Reduces the problem size by half each iteration.
- Huge speedup vs. approximation (e.g., 30 vs. 23 million iterations).

---

## ❗ Edge Case: 0 < x < 1

### Issue
- Initial `high = x`, `low = 0` leads to infinite loop because sqrt(x) > x.
- Fix: Swap bounds
```python
if x < 1:
    low = x
    high = 1
```

---

## 🧪 Cube Root with Bisection (Exercise)

### Similar Structure
```python
low = 0
high = cube
guess = (high + low) / 2.0

while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0
```

---

## ⚡ Newton-Raphson Method

### Purpose
- Efficient root finding for **polynomial functions**.
- Applies to functions like `x^2 - k` to solve `x^2 = k`.

### Update Rule
```python
guess = guess - (f(guess) / f'(guess))
```

### For square root of `k`:
- `f(x) = x^2 - k`
- `f'(x) = 2x`
```python
guess = guess - ((guess**2 - k) / (2 * guess))
```

### Efficiency
- Much faster than approximation or bisection.
- Only ~4-10 iterations to converge in typical use cases.

---

## 📊 Comparison of Algorithms

| Algorithm         | Use Case                    | Speed       | Requirements                            |
|------------------|-----------------------------|-------------|-----------------------------------------|
| Approximation     | General problems            | Slow        | No ordering or feedback needed          |
| Bisection Search  | Ordered, searchable values  | Fast        | Requires ordering & comparison feedback |
| Newton-Raphson    | Polynomial roots            | Very fast   | Requires derivative                     |

---

## 🧩 Intro to Abstraction and Decomposition

### Decomposition
- Break complex code into **independent, reusable parts**.
- Each part handles a subtask and can be developed/tested separately.

### Abstraction
- Hide internal details of implementation.
- Users interact with a **clean interface** (e.g., function inputs/outputs).

### Example
```python
pi = 3.14159
r = 2.2
area = pi * r**2
```

---

## ✅ Summary

- Bisection search cuts the problem space in half every iteration → **logarithmic time**.
- Effective for approximating square roots and cube roots with bounds and feedback.
- Newton-Raphson method uses calculus to rapidly improve guesses.
- These methods differ in speed, accuracy, and applicability.
- Concepts of **decomposition and abstraction** prepare us to build modular, maintainable code.

Next lecture: **Functions and modular design**