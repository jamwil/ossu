# MIT 6.100L – Lecture 3 Notes: Iteration and Loops

## 🔁 Control Flow Recap

### Conditionals (Branching)
- `if`, `elif`, `else` define branching logic based on Boolean conditions.
- **Indentation** is mandatory and defines code blocks.
- Only the first true condition block in a chain of `if` / `elif` / `else` is executed.

---

## 🔄 Iteration (Loops)

### Why Use Loops?
- To repeat a block of code multiple times.
- Useful when the number of repetitions is unknown in advance or determined by a condition.

---

## 🌀 While Loops

### Syntax
```python
while condition:
    # indented block
```

### Behavior
- Evaluate the `condition`.
- If `True`: execute the block, then re-evaluate condition.
- If `False`: exit loop.

### Common Pitfall
- If loop condition never becomes false, the loop runs **forever** (infinite loop).
- Always ensure loop makes **progress** toward termination.

### Example
```python
where = input("Go left or right? ")
while where == "right":
    where = input("You're still in the forest. Go left or right? ")
print("You got out of the Lost Forest.")
```

---

## 🔢 Looping with Numbers

### Decrement Example
```python
n = int(input("How many times? "))
while n > 0:
    print("x")
    n = n - 1
```

---

## ⚠ Infinite Loop Handling
- Use `Ctrl+C` or kernel stop to manually break infinite loops.
- Common mistake: forgetting to update loop variable.

---

## 🧮 Counting with Loops

### Use a Counter
```python
count = 0
while some_condition:
    count += 1
```

---

## 🧠 While Loop Patterns

```python
i = 1
while i <= x:
    factorial *= i
    i += 1
```

---

## 🔁 For Loops

### When to Use
- When you know **in advance** how many times to loop.
- Cleaner and less error-prone than `while` for definite iteration.

### Syntax
```python
for var in sequence:
    # indented block
```

### Example
```python
for n in range(5):
    print(n)
# prints 0 through 4
```

---

## 📈 Range Function

### Forms
- `range(stop)`
- `range(start, stop)`
- `range(start, stop, step)`

### Behavior
- **Start** is inclusive.
- **Stop** is exclusive.
- **Step** is increment or decrement.

### Example
```python
for i in range(1, 5):
    print(i)  # 1, 2, 3, 4
```

```python
for i in range(5, 0, -1):
    print(i)  # 5, 4, 3, 2, 1
```

---

## ➕ Accumulation Pattern

### Running Sum Example
```python
mysum = 0
for i in range(10):
    mysum += i
print(mysum)  # 45
```

---

## 🔁 Factorial Example

### While Loop Version
```python
i = 1
factorial = 1
while i <= x:
    factorial *= i
    i += 1
```

### For Loop Version
```python
factorial = 1
for i in range(1, x+1):
    factorial *= i
```

---

## ✅ Summary

| Loop Type | Use Case |
|-----------|----------|
| `while`   | Repeat **while** condition is `True`; used when number of iterations is unknown |
| `for`     | Iterate over a **known** sequence of values; concise and readable |

- Use `range()` for number sequences.
- Use `+=`, `*=` for running totals or products.
- Avoid infinite loops by ensuring exit conditions change.

Next Lecture: **More practice with loops and introduction to functions**