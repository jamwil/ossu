# MIT 6.100L – Lecture 9 Notes: Lambda Functions, Tuples, and Lists

## 🔧 Lambda Functions

### Purpose
- Create **anonymous functions** (no name).
- Useful for short, one-time-use logic.

### Syntax
```python
lambda param: expression
```

### Example
```python
lambda x: x % 2 == 0
```

### Comparison
```python
# Regular function
def is_even(x):
    return x % 2 == 0

# Lambda equivalent
lambda x: x % 2 == 0
```

---

## 🔁 Using Lambdas with Higher-Order Functions

- Functions can be passed as arguments.
- Lambdas are convenient when the function is **short** and used only once.

### Example with `apply`
```python
apply(lambda x: x == 5, 10)
```

---

## 🧠 Nested Lambda Example

### Function `do_twice`
```python
def do_twice(n, fn):
    return fn(fn(n))
```

### Usage
```python
do_twice(3, lambda x: x**2)
# fn(n) = 3**2 = 9
# fn(9) = 81 → returns 81
```

### Key Concepts
- Each lambda call creates a **new environment**.
- Execution happens inside-out, respecting scope and bindings.

---

## 📦 Tuples

### Properties
- Ordered, indexable **sequence of objects**
- Immutable
- Defined using **parentheses `()`**

### Examples
```python
empty = ()
single = (4,)
mixed = (2, "mit", 3)
```

### Access
- `t[0]` for first element
- `len(t)` for number of elements
- `t + t2` to concatenate
- `t[1:3]` for slicing

### Nested Tuples
- Tuples can contain other tuples
```python
seq = (2, "a", 4, (1, 2))
len(seq)  # 4
seq[3][0]  # 1
```

---

## 🔁 Tuple Iteration

```python
for e in seq:
    print(e)
```

- Iterates over values, not indices.

---

## 🔄 Tuple Assignment Trick

```python
x, y = y, x
```

- Swaps values efficiently using tuple unpacking.

---

## 🔁 Multiple Returns with Tuples

### Example
```python
def quotient_and_remainder(x, y):
    return (x // y, x % y)

q, r = quotient_and_remainder(10, 3)
```

- Functions can return **one tuple**, which contains multiple values.

---

## 🌟 Variable Argument Functions with `*args`

### Syntax
```python
def mean(*args):
    total = 0
    for val in args:
        total += val
    return total / len(args)
```

### Usage
```python
mean(1, 2, 3, 4, 5, 6)
mean(6, 0, 9)
```

---

## 📋 Lists

### Properties
- Ordered, indexable **sequence**
- Defined using **square brackets `[]`**
- Mutable (next lecture)

### Examples
```python
empty_list = []
numbers = [8, 3, 5]
strings = ["a", "b", "def", "g"]
```

---

## 🔁 List Iteration

```python
for i in numbers:
    print(i)
```

### Summing Elements
```python
def list_sum(l):
    total = 0
    for i in l:
        total += i
    return total
```

---

## 🧠 Loop Tips

- Add comments near loops to track what variables represent.
```python
# s is "a", then "b", then "c"...
for s in string:
    ...
```

- Helps avoid confusion when iterating over non-numeric data.

---

## ✅ Summary

- **Lambda functions** enable concise, one-time logic.
- **Tuples** are immutable sequences; can return multiple values.
- **Tuple unpacking** allows elegant assignment and returns.
- **`*args`** allows variable number of inputs to functions.
- **Lists** are mutable sequences (covered in more detail next lecture).
- Iterate directly over elements for clean, readable code.