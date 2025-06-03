# MIT 6.100L – Lecture 8 Notes: Functions Continued, Scope, and Higher-Order Functions

## 🧱 Recap: Function Basics

- Functions abstract behavior and enable code reuse.
- `return` ends function execution and outputs a value.
- If no `return`, Python returns `None` (of type `NoneType`).

---

## 🔄 `return` vs `print`

| Feature       | `return`                              | `print`                             |
|---------------|----------------------------------------|-------------------------------------|
| Use           | Pass value back to caller              | Output to console                   |
| Where used    | Only inside functions                  | Anywhere in program                 |
| Return value  | Stops function and sends value         | Returns `None`                      |

- Always prefer `return` for reusable logic.
- Use `print` mainly for debugging or user-facing messages.

---

## ✅ Tracing Function Calls

- Functions must be **called** to run.
- Wrap a call in `print()` to see the result.
- Without `return`, wrapping will show `None`.

### Example
```python
def add(x, y):
    return x + y

print(add(2, 3))  # prints 5
```

---

## ⚠ Common Bug: Forgotten `return`

```python
def is_triangular(n):
    total = 0
    for i in range(1, n+1):
        total += i
        if total == n:
            return True
        if total > n:
            break
    return False
```

---

## 📈 Bisection Root as Function

```python
def bisection_root(x):
    epsilon = 0.01
    low = 0
    high = x
    guess = (high + low) / 2

    while abs(guess**2 - x) >= epsilon:
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (high + low) / 2

    return guess
```

---

## 🧮 Brute Force Search Example

### Task
Count integers `i` such that `sqrt(i)` is within `±epsilon` of some `n`.

### Strategy
```python
def count_close_roots(n, epsilon):
    count = 0
    for i in range(int(n**3)):
        sqrt = bisection_root(i)
        if abs(sqrt - n) <= epsilon:
            count += 1
    return count
```

---

## 🧠 Function Scope & Environments

- Every function call creates a **new environment**.
- Variables defined inside a function **do not leak** to outer scopes.
- Even variables with the same name are **distinct** across scopes.

### Example
```python
def f(x):
    x += 1
    return x

x = 3
z = f(x)  # z = 4, x still = 3
```

---

## ❗ Python Scoping Rules

- Variables can be read from outer scopes.
- **Assignment** in inner scopes creates new local variables.
- To assign to outer variable, use `global` (not recommended).

---

## 🧪 Scope Pitfalls

```python
x = 5

def h(y):
    x += 1  # ❌ Error: x is referenced before assignment
```

- Causes `UnboundLocalError`
- Python assumes you're assigning to `x`, so it must be declared locally first

---

## 🧰 Functions as First-Class Objects

- Functions are objects and can be:
  - Assigned to variables
  - Passed as arguments
  - Returned from other functions

### Example
```python
def is_even(n):
    return n % 2 == 0

my_func = is_even
print(my_func(4))  # True
```

---

## 🔁 Higher-Order Functions

### Definition
- A function that takes another function as an argument or returns one.

### Example: Generic Apply
```python
def apply(criteria, n):
    count = 0
    for i in range(n + 1):
        if criteria(i):
            count += 1
    return count

def is_even(x):
    return x % 2 == 0

print(apply(is_even, 10))  # 6 (even numbers between 0 and 10)
```

---

## ✅ Summary

- Understand difference between `print` and `return`
- Each function call creates a **new isolated environment**
- Use functions to encapsulate logic, and reuse
- Functions are first-class citizens: pass, assign, return them
- Scoping errors often come from unintended assignment in inner scopes
- Higher-order functions unlock abstract, powerful design patterns

Next: **Iteration and loops**