👉 **How to take input from user + how to keep program running using loops**
---

# 🧠 1. Why do we need this?

Before this chapter:
👉 Programs were **static** (fixed)

Now:
👉 Programs become **interactive** (user can talk to program)

---

# 🎯 2. input() — Taking input from user

## ✅ Basic syntax

```python
name = input("Enter your name: ")
```

👉 What happens:

1. Program **pauses**
2. User types something
3. That value is stored in `name`

---

## 📌 Example

```python
message = input("Say something: ")
print(message)
```

👉 Output:

```
Say something: Hello
Hello
```

---

## 💡 Important point

👉 `input()` ALWAYS returns **string**

Even if user types number:

```python
age = input("Enter age: ")
print(age)
```

👉 Output:

```
'21'   # string, not number
```

---

# 🔢 3. int() — Convert string to number

## ❌ Problem

```python
age = input("Enter age: ")
if age >= 18:
```

👉 ❌ ERROR (string vs number)

---

## ✅ Solution

```python
age = input("Enter age: ")
age = int(age)
```

👉 Now:

* `"21"` → `21` (number)

---

## 📌 Example

```python
age = int(input("Enter age: "))

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
```

---

# 🧮 4. Modulo operator (%) — very useful

## 👉 Syntax

```python
number % 2
```

👉 Gives **remainder**

---

## 📌 Example

```python
number = int(input("Enter number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## 💡 Logic

* Even → remainder = 0
* Odd → remainder ≠ 0

---

# 🔁 5. while loop — MOST IMPORTANT PART

## 👉 What is while loop?

👉 Runs code **again and again** until condition becomes false

---

## ✅ Basic syntax

```python
while condition:
    code
```

---

## 📌 Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

👉 Output:

```
1 2 3 4 5
```

---

# 🧠 6. Real meaning of while loop

👉 “Run this code **until condition becomes false**”

---

# 🛑 7. User decides when to stop (VERY IMPORTANT)

## Example:

```python
message = ""

while message != "quit":
    message = input("Enter message: ")
    print(message)
```

---

## 👉 How it works

1. Start → `message = ""`
2. Loop starts
3. User types something
4. It prints
5. Loop repeats

👉 Stops only when user types `"quit"`

---

## ⚠️ Problem

If user types `"quit"` → it still prints

---

## ✅ Fix

```python
message = ""

while message != "quit":
    message = input("Enter message: ")

    if message != "quit":
        print(message)
```

---

# 🧠 8. Very important concept (understand this)

👉 while loop = **control program lifetime**

Used in:

* games 🎮
* chat apps 💬
* login systems 🔐
* menus 📋

---

# 📊 9. Difference: for vs while

| for loop    | while loop      |
| ----------- | --------------- |
| fixed times | unknown times   |
| list-based  | condition-based |

---

# 🧠 10. Mental Model

Think like this:

👉 input() = **user talks to program**
👉 int() = **convert to number**
👉 while = **keep program alive**

---

# 🚀 Real-life example

```python
while True:
    password = input("Enter password: ")

    if password == "1234":
        print("Access granted")
        break
    else:
        print("Wrong password")
```

👉 This is exactly how login works!

---

# 💡 Final Summary (VERY IMPORTANT)

👉 This chapter teaches 3 things:

1. **input()**

   * Take user input
2. **int()**

   * Convert to number
3. **while loop**

   * Run program until condition is false

---

