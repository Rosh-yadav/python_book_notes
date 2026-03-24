
# 🧠 What is he trying to teach?

He is teaching:

👉 **What are strings in Python**
👉 **How to use and manipulate text**
👉 **Important string methods (very useful in real work)**
👉 **Different ways to format strings (VERY IMPORTANT 🔥)**

---

# 🔹 1. What is a String?

👉 A **string = text (collection of characters)**

```python
"hello"
'world'
```

✔️ Written in quotes
✔️ Ordered (like list)

---

# 🔹 2. Creating Strings

```python
str()              # empty string
"hello world"
'hello world'
```

---

## Multiline string:

```python
"""This is
multiple lines"""
```

---

# 🔹 3. Cleaning Text (VERY COMMON 🔥)

## strip()

```python
input = "  hello  "
input.strip()   # "hello"
```

👉 Removes spaces from both sides

---

```python
input.lstrip()  # remove left
input.rstrip()  # remove right
```

---

# 🔹 4. Adding Spaces (Padding)

```python
name = "Barry"

name.ljust(10)       # "Barry     "
name.rjust(10, "*")  # "*****Barry"
```

---

# 🔹 5. Splitting Strings (VERY IMPORTANT 🔥)

```python
text = "Mary had a lamb"
text.split()
```

👉 Output:

```
['Mary', 'had', 'a', 'lamb']
```

---

```python
url = "a/b/c"
url.split('/')
```

👉 Output:

```
['a','b','c']
```

---

# 🔹 6. Joining Strings

```python
items = ['milk', 'bread']
" and ".join(items)
```

👉 Output:

```
"milk and bread"
```

---

# 🔹 7. Changing Case

```python
name = "bill"

name.upper()      # BILL
name.lower()      # bill
name.capitalize() # Bill
name.title()      # Bill
```

---

# 🔹 8. Checking String Content

```python
"abc123".isalnum()   # True
"abc".isalpha()      # True
"123".isnumeric()    # True
```

---

```python
"Hello".startswith("H")  # True
"Hello".endswith("o")    # True
```

---

# 🔥 9. String Formatting (MOST IMPORTANT PART)

This is the main thing he wants to teach.

---

## ❌ Old Style (Not recommended)

```python
"%s + %s = %s" % (1, 2, "Three")
```

---

## ✅ format() method

```python
"{} comes before {}".format("first", "second")
```

---

```python
"{1} after {0}".format("first", "second")
```

---

## ✅ Named values

```python
"{name} is good".format(name="Roshni")
```

---

# 🚀 10. f-strings (BEST & MODERN 🔥)

👉 Most important for interviews

```python
a = 1
b = 2

f"a is {a}, sum is {a+b}"
```

👉 Output:

```
"a is 1, sum is 3"
```

---

✔️ Easy
✔️ Clean
✔️ Recommended

---

# 🔹 11. Template Strings (Less used)

```python
from string import Template

t = Template("$name is here")
t.substitute(name="Roshni")
```

---

# 🎯 What he REALLY wants you to understand

👉 Strings are:
✔️ Used everywhere (logs, APIs, configs)

👉 You must know:

* split()
* join()
* strip()
* upper()/lower()
* **f-strings (VERY IMPORTANT)**

---

# 🔥 Real DevOps Example (important for you)

```python
name = "roshni"
env = "prod"

print(f"Deploying {name} app to {env} environment")
```

--

👉 *What are strings in Python?*

You say:

> "Strings in Python are immutable sequences of characters used to represent text. They support various operations like slicing, splitting, joining, and formatting using methods like format() and f-strings."

---

# 🚀 Super Simple Summary

✔️ String = text
✔️ `strip()` → remove spaces
✔️ `split()` → break into list
✔️ `join()` → combine
✔️ `upper()/lower()` → change case
✔️ **f-string → best formatting method**

---
