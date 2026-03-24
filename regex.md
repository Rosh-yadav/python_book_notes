
---

# 🧠 What is he trying to teach?

👉 He is teaching:

1. How to **search text**
2. Difference between simple search vs **regex**
3. How to use **patterns instead of exact words**

---

# 🔹 Step 1: Simple Search (Easy)

You already know this:

```python
'Rostam' in cc_list
```

👉 Meaning:

> “Is the word ‘Rostam’ present?”

✔️ Output: `True`

---

# 🔹 Step 2: Using `re.search()`

```python
import re

re.search('Rostam', cc_list)
```

👉 Same result, but more powerful

✔️ If found → returns match
❌ If not → returns None

---

## Use in condition:

```python
if re.search('Rostam', cc_list):
    print("Found")
```

---

# 🔥 Important Difference

| Method        | Use                       |
| ------------- | ------------------------- |
| `in`          | simple match              |
| `re.search()` | powerful pattern matching |

---

# 🔹 Step 3: Character Sets `[ ]` (VERY IMPORTANT 🔥)

👉 This is the main concept here

---

## Example:

```python
re.search(r'[R,B]obb[i,y]', cc_list)
```

👉 Means:

* `[R,B]` → R or B
* `obb` → fixed
* `[i,y]` → i or y

---

👉 Matches:
✔️ Bobbi
✔️ Robby

---

### 🧠 Simple way to think:

> `[ ]` = “choose one from these”

---

# 🔹 Step 4: Ranges

```python
[A-Z]   # A to Z
[a-z]   # small letters
[0-9]   # numbers
```

---

## Example:

```python
re.search(r'Chr[a-z][a-z]', cc_list)
```

👉 Means:

* Chr + any 2 letters

✔️ Matches: "Chris"

---

# 🔹 Step 5: `+` (VERY IMPORTANT)

```python
[A-Za-z]+
```

👉 Means:

> One or more letters

---

✔️ Matches:

* Ezra
* Koenig

---

# 🔹 Step 6: `{}` (Exact count)

```python
[A-Za-z]{6}
```

👉 Means:

> Exactly 6 letters

✔️ Matches:

* Koenig

---

# 🔹 Step 7: Email Pattern Example

```python
re.search(r'[A-Za-z]+@[a-z]+\.[a-z]+', cc_list)
```

---

👉 Break it:

| Part        | Meaning          |
| ----------- | ---------------- |
| `[A-Za-z]+` | name             |
| `@`         | @ symbol         |
| `[a-z]+`    | domain           |
| `\.`        | dot (IMPORTANT!) |
| `[a-z]+`    | extension        |

---

## ⚠️ VERY IMPORTANT

👉 `.` means:

> ANY character

So to match real dot:

```python
\.
```

---

# 🎯 What he REALLY wants you to understand

## 🔥 Main idea:

👉 Instead of searching exact text:

> You can search **patterns**

---

# 🔥 Real-Life Example (DevOps 🔥)

👉 Logs:

```python
log = "ERROR 500 at /api"
```

Find error:

```python
re.search(r'ERROR \d+', log)
```

✔️ Matches: "ERROR 500"

---

# 🧠 SUPER SIMPLE SUMMARY

👉 Regex = smart search

| Symbol  | Meaning     |
| ------- | ----------- |
| `[abc]` | a or b or c |
| `[a-z]` | range       |
| `+`     | one or more |
| `{n}`   | exact count |
| `.`     | any char    |
| `\.`    | real dot    |

---

# 💡 One Line Understanding (VERY IMPORTANT)

> "Regex allows you to search patterns in text instead of exact words."

---

