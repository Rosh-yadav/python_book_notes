# 🧠 1. What are Generators?

## ✔ Concept:

👉 A **generator** is a function that:

* returns values **one by one**
* instead of returning all at once

---

## 🔥 Key keyword:

```python
yield
```

👉 replaces `return`

---

## 💻 Example:

```python
def count():
    n = 0
    while True:
        n += 1
        yield n
```

---

## 🧠 How it works:

```python
counter = count()

next(counter) → 1
next(counter) → 2
next(counter) → 3
```

---

## 🧠 Simple understanding:

👉 Generator = “pause & continue”

---

# ⚡ Important Difference

| Normal Function   | Generator            |
| ----------------- | -------------------- |
| return once       | yield multiple times |
| ends after return | pauses & resumes     |
| memory heavy      | memory efficient     |

---

# 🧠 2. Generator keeps state

👉 It **remembers previous value**

Example:

* n = 1 → next → 2 → next → 3

👉 It doesn’t restart

---

# 🧠 3. Fibonacci Generator

## 💻 Code:

```python
def fib():
    first = 0
    last = 1
    while True:
        first, last = last, first + last
        yield first
```

---

## Output:

```python
1, 1, 2, 3, 5, 8...
```

---

## 🧠 Key idea:

👉 Generator can be used for **infinite sequences**

---

# 🧠 4. Using generator in loop

```python
for x in fib():
    print(x)
    if x > 12:
        break
```

---

## 🧠 Meaning:

👉 loop keeps calling `next()` internally

---

# 🧠 5. Generator Comprehension

## ✔ Concept:

👉 Short way to create generator

---

## 💻 Example:

```python
(x for x in range(100))
```

---

## Compare:

```python
[x for x in range(100)]  # list
(x for x in range(100))  # generator
```

---

## 🧠 Difference:

| List              | Generator            |
| ----------------- | -------------------- |
| []                | ()                   |
| stores all values | generates one by one |
| more memory       | less memory          |

---

# 🧠 6. Memory Difference (VERY IMPORTANT)

```python
sys.getsizeof(list) → big
sys.getsizeof(generator) → small
```

---

## 🧠 Simple:

👉 Generator saves memory ✅

---

# 🚀 DEVOPS CONNECTION

👉 Why generator important:

* log processing
* big data files
* streaming data

---

# 🧠 7. IPython Shell Commands (`!`)

## ✔ Concept:

👉 Run Linux commands inside Python

---

## 💻 Example:

```python
!ls -l
```

---

## Store output:

```python
files = !ls -l
```

---

## 🧠 Meaning:

👉 Python + Linux together

---

# 🧠 8. SList (Special Output)

👉 When you run shell command:

```python
files = !ls
```

👉 It becomes **SList object**

---

## Useful methods:

### ✔ sort:

```python
df.sort(3, nums=True)
```

👉 sort column

---

### ✔ grep:

```python
ls.grep("kill")
```

👉 filter like Linux grep

---

## 🧠 Simple:

👉 SList = smart list for shell output

---

# 🧠 9. Magic Commands (`%%`)

## ✔ Concept:

👉 Special shortcuts in IPython

---

## 💻 Example 1:

```python
%%bash
uname -a
```

👉 run bash script

---

## 💻 Example 2:

```python
%%writefile file.py
print("hello")
```

👉 create file directly

---

## 💻 Example 3:

```python
%who
```

👉 shows variables

---

## 🧠 Simple:

👉 Magic commands = shortcuts

---

# 🧠 10. Lazy Evaluation (connect with generator)

👉 Already seen in:

* generator
* finditer

---

## ✔ Meaning:

👉 Do work **only when needed**

---

## 🧠 Example:

* generator → next() → gives value
* not all values created

---

# 🔥 FINAL SUMMARY (VERY IMPORTANT)

👉 He is teaching:

### 1. Generators

* yield
* memory efficient
* used for large data

---

### 2. Generator vs List

* list → all data
* generator → one by one

---

### 3. IPython tricks

* run Linux commands
* automate DevOps tasks

---

### 4. Lazy processing

* better performance

---

# 🎯 INTERVIEW READY ANSWERS

### Q: What is generator?

✔ A function that uses `yield` to return values one by one instead of all at once.

---

### Q: Why use generator?

✔ Memory efficient, useful for large data processing.

---

### Q: Difference list vs generator?

✔ List stores all values, generator produces values one by one.

---
