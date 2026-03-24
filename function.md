
# 🧠 What is he trying to teach?

He is teaching:

👉 **What is a function**
👉 **Why we use it**
👉 **How to define and use it**
👉 **Types of arguments**
👉 **Return values**

---

# 🔹 1. What is a Function?

👉 A **function = reusable block of code**

Instead of writing same code again and again:
✔️ Write once
✔️ Use many times

---

# 🔥 Real Example

Without function ❌:

```python
print("Hello Roshni")
print("Hello Roshni")
print("Hello Roshni")
```

With function ✅:

```python
def greet():
    print("Hello Roshni")

greet()
greet()
greet()
```

---

# 🔹 2. Function Structure (VERY IMPORTANT)

```python
def function_name(parameters):
    # code
```

---

Example:

```python
def my_function():
    print("Hello")
```

---

# 🔹 3. Docstring (Best Practice ⭐)

```python
def my_function():
    """
    This function prints hello
    """
```

👉 Used for:
✔️ Documentation
✔️ Readability
✔️ Interviews love this

---

# 🔹 4. Parameters (Inputs)

## ✅ Positional Arguments

```python
def positioned(first, second):
    print(first, second)

positioned(1, 2)
```

👉 Order matters!

---

## ✅ Keyword Arguments

```python
def keywords(first=1, second=2):
    print(first, second)
```

---

Call it:

```python
keywords()                 # default values
keywords(3, 4)            # override
keywords(second=10, first=5)  # order doesn't matter
```

---

# 🔥 Important Rule

👉 Once you use keyword arguments:
✔️ All next arguments must also be keyword

---

# 🔹 5. Return Values (VERY IMPORTANT 🔥)

## ❌ No return

```python
def no_return():
    pass
```

👉 Output:

```python
None
```

---

## ✅ With return

```python
def return_one():
    return 1
```

👉 Output:

```python
1
```

---

👉 Key point:

✔️ `return` sends value back
✔️ Without it → `None`

---

# 🎯 What he REALLY wants you to understand

👉 Functions help you:
✔️ Avoid repetition
✔️ Write clean code
✔️ Make code reusable

---

# 🔥 Real DevOps Example (VERY IMPORTANT FOR YOU)

```python
def deploy(env):
    print(f"Deploying to {env}")

deploy("dev")
deploy("prod")
```

---

# 💡 Interview Answer (VERY IMPORTANT)

If asked:

👉 *What is a function in Python?*

You say:

> "A function in Python is a reusable block of code defined using the def keyword. It can take inputs as parameters and optionally return a value using the return statement."

---

# 🚀 Super Simple Summary

✔️ Function = reusable code
✔️ `def` → define
✔️ Parameters → input
✔️ `return` → output
✔️ Default args → flexible

---

# ⚠️ Common Beginner Mistake

```python
def add(a, b):
    print(a + b)
```

👉 This does NOT return value!

Correct:

```python
def add(a, b):
    return a + b
```

---


