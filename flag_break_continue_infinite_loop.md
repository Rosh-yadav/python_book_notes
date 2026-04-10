👉 **Different ways to control when a loop should stop or continue**

---

# 🧠 1. Problem first (why we need this)

Earlier you saw:

```python
while message != "quit":
```

👉 Works fine for simple case

❌ But in real programs:

* many conditions can stop program
* code becomes messy

---

# 🚩 2. Using a FLAG (very important concept)

## 👉 What is a flag?

👉 A **flag = a variable (True/False)**
👉 It controls whether program runs or stops

---

## ✅ Example

```python
active = True

while active:
    message = input("Enter message: ")

    if message == "quit":
        active = False
    else:
        print(message)
```

---

## 🧠 How it works

👉 Step by step:

1. `active = True` → program starts
2. `while active:` → loop runs
3. if user types `"quit"` →
   👉 `active = False`
4. loop stops

---

## 💡 Why use flag?

👉 Because you can add **many conditions easily**

Example:

```python
if message == "quit":
    active = False
elif message == "exit":
    active = False
elif message == "stop":
    active = False
```

👉 Much cleaner than writing everything in `while`

---

# 🔥 3. break — immediately stop loop

## 👉 What is break?

👉 “STOP LOOP RIGHT NOW”

---

## ✅ Example

```python
while True:
    city = input("Enter city: ")

    if city == "quit":
        break

    print(city)
```

---

## 🧠 How it works

* `while True` → infinite loop
* `break` → exits loop immediately

---

## 💡 When to use break?

👉 When:

* you want **instant exit**
* no need to check condition again

---

# 🔁 4. continue — skip current loop

## 👉 What is continue?

👉 “Skip this iteration and go to next loop”

---

## ✅ Example

```python
number = 0

while number < 10:
    number += 1

    if number % 2 == 0:
        continue

    print(number)
```

---

## 🧠 Output

```text
1 3 5 7 9
```

---

## 💡 Why?

* even numbers → skipped
* odd numbers → printed

---

# ⚠️ 5. Infinite loop (danger 🚨)

## ❌ Example

```python
x = 1

while x <= 5:
    print(x)
```

👉 ❌ runs forever

---

## 🧠 Why?

👉 `x` never changes
👉 condition always True

---

## ✅ Fix

```python
x += 1
```

---

# 🧠 VERY IMPORTANT CONCEPT

👉 Every while loop must have:

✔ condition that can become False
OR
✔ break statement

---

# 🔥 6. Comparison (SUPER IMPORTANT)

| Concept       | Meaning                       |
| ------------- | ----------------------------- |
| flag          | control loop using True/False |
| break         | exit loop immediately         |
| continue      | skip current iteration        |
| infinite loop | loop never stops              |

---

# 🧠 7. When to use what? (REAL LOGIC)

## ✅ Use FLAG when:

* many conditions to stop program
* big programs (games, apps)

---

## ✅ Use BREAK when:

* user types "quit"
* you want instant exit

---

## ✅ Use CONTINUE when:

* skip some cases
* filter data

---

# 🚀 Real-life examples

## 🎮 Game loop

```python
game_running = True

while game_running:
    if player_dead:
        game_running = False
```

---

## 🔐 Login system

```python
while True:
    password = input("Enter password: ")

    if password == "1234":
        break
```

---

## 🔢 Filter numbers

```python
if number % 2 == 0:
    continue
```

---

# 💡 Final Simple Summary

👉 This section teaches:

1. **Flag**
   → control loop using True/False

2. **break**
   → stop loop immediately

3. **continue**
   → skip current loop

4. **Infinite loop**
   → avoid it


