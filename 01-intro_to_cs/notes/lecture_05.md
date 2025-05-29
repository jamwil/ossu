# MIT 6.100L – Lecture 5 Notes: Floating Point, Binary Fractions, and Approximation Algorithms

## 🔢 Motivation: Why Floating Point Matters
- Simple example: summing `0.1` ten times does **not** equal `1.0` due to **floating-point representation errors**.
- In memory, 0.1 is stored **approximately**, leading to cumulative inaccuracies.

---

## 🔄 Binary Conversion Recap

### Integer to Binary
1. While `num > 0`:
   - Prepend `str(num % 2)` to result.
   - Set `num = num // 2`.

### Negative Integers
- Convert absolute value first.
- Add `'-'` prefix after conversion.

---

## 🧮 Decimal Fractions to Binary

### Key Idea
- Multiply decimal by increasing powers of 2 until result is an integer.

### Steps
1. Multiply the decimal by `2^p` until `x * (2^p)` is an integer.
2. Convert result to binary using the integer algorithm.
3. Shift binary point left by `p`.

### Example: 0.625
- Multiply by `2^3 = 8` → 0.625 × 8 = 5
- Binary of 5 = `101`
- Move decimal left 3 places → `0.101`

### Caveat
- Some decimals (like `0.1`) require large `p` values or can't be represented exactly → leads to **precision issues**

---

## 🧠 How Numbers Are Stored in Memory

### Floating Point Format
- Stored as two components:
  - **Significant digits (mantissa)**
  - **Exponent** (power of 2)
- Example:
  - `125 × 2^-2` → Convert 125 to binary and shift decimal point accordingly

### Implications
- Computers have limited **bit precision** (e.g. 32-bit, 64-bit)
- Numbers like `0.1` can't be represented exactly → **truncation error**

---

## ❗ Comparing Floats Safely

### DO NOT:
```python
if x == 1.0:
```

### DO:
```python
if abs(x - 1.0) < epsilon:
```

- Always compare floats using **epsilon-based** approximations

---

## 🧮 Approximation Algorithm

### Purpose
- Estimate square roots (or other values) **without needing exact matches**
- More flexible than guess-and-check

### Pattern
```python
x = 36
epsilon = 0.01
increment = 0.0001
guess = 0.0

while abs(guess**2 - x) >= epsilon:
    guess += increment
```

- Stops when `guess^2` is "close enough" to `x`

### Tuning Parameters
- **epsilon**: How close is "close enough"
- **increment**: Step size between guesses

### Trade-offs
- Smaller increment = more accuracy, but slower
- Larger epsilon = faster, but less accurate

---

## ⚠ Pitfalls

### Overshooting the Answer
- Program may **skip over** the correct value if guess^2 jumps past x
- Result: loop never exits

### Solution
Add an **additional condition**:
```python
while abs(guess**2 - x) >= epsilon and guess**2 <= x:
```

---

## 🐢 Performance Considerations

- Reducing increment → slower runtime (more guesses)
- Example:
  - increment = 0.0001 → ~2.3 million guesses
  - increment = 0.00001 → ~23 million guesses

---

## ✅ Summary

- Floating-point numbers are **approximate** due to how they're stored.
- Convert decimals to binary by scaling and shifting.
- Use **epsilon-based** comparisons for floats.
- Approximation algorithms work by incrementally checking closeness.
- **Trade-off**: Accuracy vs. Speed (via `epsilon` and `increment`)
- Be mindful of **overshooting** and add loop guards to avoid infinite loops.

Next lecture: **Faster approximation methods like bisection search**