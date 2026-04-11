### 3. ⚠️ Handling errors (exceptions)

---

# 3️⃣ ⚠️ Exceptions (Most Important Concept)

👉 Sometimes programs crash due to errors.

Example:

```python
print(5/0)
```

💥 Error:

```
ZeroDivisionError
```

---

## ✅ Solution: try-except

```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

👉 Meaning:

* Try running code
* If error happens → handle it nicely

---

## 🔁 Real Example (Calculator)

Without handling:

```python
answer = int(a) / int(b)
```

If user enters `0` → 💥 crash

---

### ✔️ With handling:

```python
try:
    answer = int(a) / int(b)
except ZeroDivisionError:
    print("You can't divide by 0!")
else:
    print(answer)
```

---

### 💡 Flow:

| Block    | Meaning             |
| -------- | ------------------- |
| `try`    | Try this code       |
| `except` | If error happens    |
| `else`   | If everything works |

---

# 4️⃣ File Errors

If file doesn’t exist:

```python
with open('abc.txt')
```

💥 Error:

```
FileNotFoundError
```

---

### ✔️ Fix:

```python
try:
    with open('abc.txt') as f:
        data = f.read()
except FileNotFoundError:
    print("File not found")
```


