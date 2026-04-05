
# 🧠 First: What is this chapter REALLY teaching?

👉 Think like this:

Your system has:

* Logs 📄
* Config files ⚙️
* Data files (JSON, YAML)

Instead of opening them manually, Python lets you:

👉 **Read → Understand → Modify → Save**

That’s it. Everything in this chapter is just this.

---

# 🔹 Step 1: What is a FILE in Python?

A file is just:

```
data stored on disk (like .txt, .json, .log)
```

Example:

```
file.txt
---------
Hello Roshni
How are you
```

---

# 🔹 Step 2: How Python talks to a file

Python cannot directly read file.

👉 First it needs to **open** it.

### Basic syntax:

```python
open("filename", "mode")
```

---

# 🔹 Step 3: What is "mode"?

Mode tells Python:
👉 **What you want to do with file**

| Mode   | Meaning           |
| ------ | ----------------- |
| `"r"`  | Read file         |
| `"w"`  | Write (overwrite) |
| `"a"`  | Append            |
| `"rb"` | Read binary       |

---

# 🔹 Step 4: Reading a file (VERY IMPORTANT)

### Code:

```python
file = open("file.txt", "r")
data = file.read()
print(data)
file.close()
```

---

### Let’s understand LINE BY LINE:

### 1️⃣

```python
file = open("file.txt", "r")
```

👉 Open file in **read mode**

👉 `file` is like a **connection** to that file

---

### 2️⃣

```python
data = file.read()
```

👉 Read ALL content

👉 Store inside variable `data`

---

### 3️⃣

```python
print(data)
```

👉 Show content

---

### 4️⃣

```python
file.close()
```

👉 Close connection (important for system resources)

---

# 🔹 Step 5: Better way (IMPORTANT ⭐)

Instead of manually closing file:

```python
with open("file.txt", "r") as file:
    data = file.read()
    print(data)
```

---

### Why use `with`?

👉 Automatically closes file
👉 Cleaner
👉 Industry standard

---

# 🔹 Step 6: Reading line by line

```python
with open("file.txt") as file:
    lines = file.readlines()
    print(lines)
```

---

### Output:

```
['Hello Roshni\n', 'How are you\n']
```

👉 Each line becomes **list item**

---

# 🔹 Step 7: Writing to file

### Code:

```python
with open("file.txt", "w") as file:
    file.write("Hello DevOps")
```

---

### What happens?

👉 Old content deleted
👉 New content written

---

# 🔹 Step 8: Append (don’t delete old data)

```python
with open("file.txt", "a") as file:
    file.write("\nNew line added")
```

👉 Adds content at end

---

# 🔹 Step 9: Real DevOps Example

👉 Suppose log file:

```
error.log
-----------
Error: disk full
Error: memory high
```

You can read it:

```python
with open("error.log") as file:
    data = file.read()
    if "disk" in data:
        print("Disk issue found")
```

👉 This is **automation**

---

# 🔹 Step 10: JSON (MOST IMPORTANT FOR DEVOPS)

👉 JSON = structured data (key-value)

Example:

```json
{
  "name": "roshni",
  "age": 25
}
```

---

### Why JSON?

Used in:

* AWS policies
* APIs
* Kubernetes
* Config files

---

# 🔹 Step 11: Read JSON

```python
import json

with open("file.json") as file:
    data = json.load(file)
```

---

### What happens?

👉 JSON → Python dictionary

---

### Now you can access:

```python
print(data["name"])
```

---

# 🔹 Step 12: Modify JSON

```python
data["name"] = "new_name"
```

---

# 🔹 Step 13: Save JSON

```python
with open("file.json", "w") as file:
    json.dump(data, file)
```

---

# 🔹 Step 14: YAML (used in DevOps tools)

👉 Same as JSON but cleaner

Example:

```
name: roshni
age: 25
```

---

### Read YAML:

```python
import yaml

with open("file.yml") as file:
    data = yaml.safe_load(file)
```

---

👉 Used in:

* Kubernetes
* Ansible

---

# 🔹 Step 15: CSV (Excel-like files)

Example:

```
name,age
roshni,25
```

---

### Read CSV:

```python
import csv

with open("file.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

---

👉 Output:

```
['name', 'age']
['roshni', '25']
```

---

# 🔹 Step 16: BIG PICTURE (VERY IMPORTANT)

Everything you learned is:

| Task        | Tool    |
| ----------- | ------- |
| Read file   | open()  |
| Write file  | write() |
| JSON data   | json    |
| YAML config | yaml    |
| Excel data  | csv     |

---

# 🔥 FINAL SIMPLE UNDERSTANDING

👉 Python is helping you:

✔ Open file
✔ Read data
✔ Modify data
✔ Save it back

---
t”
