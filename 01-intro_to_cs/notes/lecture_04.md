# Realtime

To convert base-10 to binary, within a loop, you evaluate if the value is odd or
even. If it's odd, you stick a 1 in the leftmost slot, and if even, you stick
a 0. You then floor divide the value and proceed to the next iteration.

```python
>>> value = 1507
>>> result = ""
>>> while value > 0:
...     if value % 2 == 1:
...         result = "1" + result
...     else:
...         result = "0" + result
...     value = value // 2
...
>>> result
'10111100011'
```

# MIT 6.100L – Lecture 4 Notes: Loop Nuances, Guess-and-Check, and Binary

## 🔁 Recap on Loops

### While Loops

- Repeats as long as a **condition is true**
- Risk: **infinite loops** if condition never becomes false

### For Loops

- Iterates over a **sequence** (numbers, strings, etc.)
- Cleaner for **definite iteration** (known number of steps)

---

## 🛑 Breaking Out Early: `break` Statement

### Purpose

- Exit the innermost enclosing loop immediately
- Useful when a solution is found before exhausting a loop

### Example

```python
for i in range(5, 11, 2):
    if condition:
        break  # exits the loop
```

---

## 🧮 Counting Evens (For Loop Practice)

### Pattern

```python
even_count = 0
for i in range(10):
    if i % 2 == 0:
        even_count += 1
```

---

## 🔡 Iterating Over Strings

### Option 1: By Index

```python
for i in range(len(s)):
    char = s[i]
```

### Option 2: Directly

```python
for char in s:
    if char in "iu":
        print("Found i or u")
```

---

## 🤖 Cheerleader Program

### Breakdown

- Spell out word letter by letter with “Give me a …”
- Repeat word based on user enthusiasm level
- Used:
  - Character iteration
  - Conditional logic for "a" vs "an"
  - Loop for repetition

---

## 🔍 Counting Unique Letters in String

### Pattern

```python
seen = ""
for char in s:
    if char not in seen:
        seen += char
print(len(seen))
```

- Avoids duplicates by checking a "seen" string

---

## 🔁 Guess-and-Check Algorithm

### Concept

- Systematically try potential solutions
- Stop if one is correct or search space is exhausted

### Pattern

```python
guess = 0
while guess**2 < x:
    guess += 1
if guess**2 == x:
    print("Perfect square")
else:
    print("Not a perfect square")
```

---

## ❗ Negative Input Handling

```python
if x < 0:
    neg_flag = True
    x = abs(x)
```

- Use flags (`True`/`False`) to handle special logic after main loop

---

## ✅ For Loop Version of Guess-and-Check

### Cube Root Example

```python
for guess in range(abs(x)+1):
    if guess**3 == abs(x):
        break
```

### Add Sign Back for Negative Input

```python
if x < 0:
    guess = -guess
```

---

## 📊 Word Problem as Code

### Problem

- Alyssa, Ben, Cindy sold 10 tickets
- Ben = Alyssa - 2
- Cindy = 2 × Alyssa

### Code Sketch

```python
for alyssa in range(11):
    ben = alyssa - 2
    cindy = 2 * alyssa
    if alyssa + ben + cindy == 10:
        print(alyssa, ben, cindy)
```

---

## ⚠ Loop Efficiency

- Use **nested loops** only when necessary
- When possible, reduce to **single loop** using algebra

---

## 🧮 Binary Numbers (Preview for Approximation)

### Motivation

- Why does `0.1 * 10 == 1` work but `sum([0.1]*10) == 1` fails?

### Reason

- **Floating-point error**: caused by binary approximation of decimals

### Binary Representation

- Computers store numbers in **base 2**
- Only 0s and 1s — tied to physical hardware logic (e.g., voltage levels)
- Example:
  - `1507 = 2^10 + 2^8 + ... + 2^0` → `10111100011`

### Conversion Pattern

- Repeatedly divide by 2, prepend remainder to result

```python
x = 1507
result = ""
while x > 0:
    result = str(x % 2) + result
    x = x // 2
```

---

## ✅ Summary

- Loops can be exited early with `break`
- Strings can be iterated directly in `for` loops
- Use **Boolean flags** to track state within loops
- Guess-and-check solves problems by exhaustive search
- For loops + algebra = fast enumeration
- Binary representation of numbers explains floating-point quirks

Next up: **Approximation algorithms**
