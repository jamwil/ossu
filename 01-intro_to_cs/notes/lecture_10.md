# MIT 6.100L – Lecture 10 Notes: Lists and Mutability

## 📦 Tuples Recap
- Tuples are **immutable** sequences.
- Operations similar to strings: slicing, indexing, etc.
- Cannot be changed once created.

---

## 🧰 Lists Review

### Properties
- Mutable sequence of objects.
- Can contain mixed types: numbers, strings, other lists, etc.
- List syntax: `[]`

### Basic Operations
- `len(L)`, `L[i]`, `L[a:b]`, `L + L2`, `max(L)`, `for e in L:`

---

## 🔄 Mutability and Memory

### Key Concept
- Lists can be **changed in place** via indexing.
- Syntax:
```python
L[3] = 10  # Replaces the element at index 3
```

### Memory Behavior
- Mutating a list affects the original object.
- No new object is created unless explicitly assigned.

---

## ➕ List Append

### Usage
```python
L.append(x)  # Adds x to the end of L
```

### Behavior
- Appends element directly to original list (mutates).
- Returns `None`.

### Common Error
```python
L = L.append(x)  # ❌ L becomes None
```

---

## 🧠 Dot Notation

- Used to call methods on objects.
```python
L.append(5)
```
- Left of the dot: object
- Right: method (behavior of the object)

---

## 🛠 Example: Build List
```python
def make_ordered_list(n):
    result = []
    for i in range(n + 1):
        result.append(i)
    return result
```

---

## ❌ Removing Elements from List

```python
def remove_lm(L, e):
    result = []
    for i in L:
        if i != e:
            result.append(i)
    return result
```

---

## 🔄 String to List

```python
list("abc")           # ['a', 'b', 'c']
s.split(" ")          # Splits string into words
```

## 🔁 List to String

```python
"_".join(["a", "b"])  # 'a_b'
```

> All elements must be strings to join.

---

## 🔃 List Mutation Methods

- `L.append(x)` – Add one item
- `L.sort()` – Sorts in place
- `L.reverse()` – Reverses in place
- `sorted(L)` – Returns new sorted list (non-mutating)

---

## ⚠ Sorting Gotchas

- `L.sort()` mutates and returns `None`
- `sorted(L)` returns new list, original unchanged
- Mixed types in list → `TypeError`

---

## 🧪 In-Place List Mutation

```python
def square_list(L):
    for i in range(len(L)):
        L[i] = L[i] ** 2
```

- Mutates list in-place, returns `None`

---

## 🌀 List Iteration Pitfalls

### Safe:
```python
for i in range(len(L)):
    L.append(i)
```

### Unsafe:
```python
for e in L:
    L.append(i)  # May cause infinite loop
```

---

## 📌 Extend vs Concatenation

```python
L1.extend([0, 6])  # Mutates L1
L3 = L1 + L2       # Returns new list
```

---

## 🧠 Example: Doubling List
```python
for e in L:
    L = L + L  # Doubles L on each iteration
```

- Binds new object to L each time.
- Original object iterated via `e`, not affected.

---

## 🧹 Clearing a List

```python
L.clear()  # Mutates original list to be empty
```

vs

```python
L = []     # Creates a new empty list
```

Use `id(L)` to verify identity (memory address).

---

## ✅ Summary

- Tuples are immutable, lists are mutable.
- List methods like `append`, `sort`, and `reverse` **mutate**.
- `sorted`, `+`, and `join` return **new objects**.
- Avoid assigning results of mutating methods.
- Understand memory and object identity to avoid pitfalls.