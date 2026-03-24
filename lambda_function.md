

# 🧠 What is he trying to teach?

This part teaches **3 main things**:

1️⃣ **Functions are objects**
2️⃣ **Lambda (anonymous functions)**
3️⃣ **Introduction to Regex (pattern matching)**

---

# 🔹 1. Functions are Objects (VERY IMPORTANT 🔥)

👉 This is a big concept:

> In Python, functions behave like normal data (like numbers or strings)

---

## Example:

```python
def double(x):
    return x * 2

def triple(x):
    return x * 3

functions = [double, triple]
```

👉 Now functions are stored in a list!

---

## Calling them:

```python
for f in functions:
    print(f(3))
```

👉 Output:

```
6
9
```

---

### 🎯 Key Idea:

✔️ You can:

* Store functions in variables
* Put them in lists
* Pass them to other functions

---

# 🔹 2. Lambda Functions (IMPORTANT 🔥)

👉 Lambda = **small one-line function**

---

## Normal function:

```python
def square(x):
    return x * x
```

---

## Lambda version:

```python
lambda x: x * x
```

---

👉 No name
👉 Short and quick

---

# 🔹 Example from your code

```python
items = [[0,'a',2], [5,'b',0], [2,'c',1]]
```

---

## Default sorting:

```python
sorted(items)
```

👉 Sorts by first value

---

## Using function:

```python
def second(item):
    return item[1]

sorted(items, key=second)
```

---

## Using lambda (BEST way 🔥):

```python
sorted(items, key=lambda item: item[1])
```

---

👉 Sort by:

* `item[1]` → second value
* `item[2]` → third value

---

# ⚠️ Important Rule

👉 Use lambda only for:
✔️ Small, simple logic

❌ Don’t use for complex code (hard to read)

---

# 🔹 3. Regex (Introduction Only)

👉 Regex = **pattern matching in text**

Used for:

* Logs analysis
* Input validation
* Searching patterns

---

## Simple example:

```python
import re

text = "my number is 123"
re.search(r"\d+", text)
```

👉 `\d+` = find numbers

---

## Why `r""`?

👉 Raw string avoids confusion with `\`

---

# 🎯 What he REALLY wants you to understand

## 🔥 Main Takeaways:

### 1️⃣ Functions are flexible

✔️ Can be passed around like data

---

### 2️⃣ Lambda = shortcut

✔️ Small quick functions

---

### 3️⃣ Regex = powerful text tool

✔️ Used in real-world (logs, validation)

---

# 🔥 Real DevOps Example (IMPORTANT)

```python
logs = ["error 500", "ok 200", "error 404"]

errors = list(filter(lambda x: "error" in x, logs))
print(errors)
```

👉 Output:

```
['error 500', 'error 404']
```

---

# 💡 Interview Answer (VERY IMPORTANT)

If asked:

👉 *What are lambda functions?*

You say:

> "Lambda functions are anonymous one-line functions in Python used for short operations, often passed as arguments to functions like map, filter, and sorted."

---
---

# 🧠 Think of this in ONE simple idea:

👉 **In Python, functions are just like variables (data)**

That’s it. Everything else comes from this.

---

# 🔹 1. Functions are like normal values

You already do this:

```python
x = 10
y = "hello"
```

👉 Now same thing with functions:

```python
def greet():
    print("Hello")

f = greet   # store function in variable
```

👉 Now:

```python
f()
```

✔️ Output:

```
Hello
```

👉 So:

> Function = value you can store and use

---

# 🔹 2. Put functions in a list (THIS IS THE MAIN IDEA)

```python
def double(x):
    return x * 2

def triple(x):
    return x * 3

functions = [double, triple]
```

👉 Now loop:

```python
for f in functions:
    print(f(3))
```

✔️ Output:

```
6
9
```

👉 Why this works?

Because:

> Each item in list = function
> `f(3)` = call that function

---

# 🔥 SUPER IMPORTANT UNDERSTANDING

👉 Normally:

```python
double(3)
```

👉 Here:

```python
f = double
f(3)
```

👉 SAME thing!

---

# 🔹 3. Why do we even do this?

👉 Because Python lets you **pass functions to other functions**

Example:

```python
sorted(data, key=some_function)
```

👉 You are saying:

> “Use this function to decide sorting”

---

# 🔹 4. Now Lambda (this is where confusion happens)

👉 Lambda = **quick small function without name**

---

## Normal way:

```python
def get_second(item):
    return item[1]
```

---

## Lambda way:

```python
lambda item: item[1]
```

👉 Same thing, just shorter

---

# 🔥 Real Example (IMPORTANT)

```python
items = [[0,'a',2], [5,'b',0], [2,'c',1]]
```

---

## Default sort:

```python
sorted(items)
```

👉 sorts by first value

---

## Sort by second value:

```python
sorted(items, key=lambda item: item[1])
```

👉 Meaning:

> "Use item[1] to decide order"

---

## Sort by third value:

```python
sorted(items, key=lambda item: item[2])
```

---

# 🎯 SIMPLE WAY TO REMEMBER

👉 This:

```python
lambda item: item[1]
```

Means:

> "Take item → return item[1]"

---

# 🔹 5. When to use lambda?

✔️ Small logic
✔️ One line
✔️ Inside functions like:

* `sorted()`
* `filter()`

---

❌ Don’t use for big logic

---

# 🔹 6. Regex (don’t overthink now)

👉 It’s just:

> "Search pattern in text"

Example:

```python
import re

text = "error 404"
re.search("error", text)
```

👉 Finds word "error"

---

# 🧠 FINAL CLEAR UNDERSTANDING

## 💥 Core idea:

👉 Functions are **values**

So you can:

* store them
* pass them
* use them dynamically

---

# 🔥 One Line Summary (VERY IMPORTANT)

> "Python treats functions as first-class objects, meaning they can be stored in variables, passed as arguments, and used dynamically."

---



