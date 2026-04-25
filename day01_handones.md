# 📘 Day 1 Notes – Log Analyzer Script (DevOps Python)

---

## 🧩 🟢 Problem Statement (Scenario)

**Role:** DevOps Engineer
**Task:** Work with log files (application logs / cloud logs)

### 🎯 Goal

Build a Python script that:

* Reads a log file
* Counts:

  * ERROR
  * INFO
  * WARNING
* Handles errors (file not found)
* Generates a report

---

## 🧠 🟡 My Thought Process & Learning Journey

---

### 🔹 Step 1: Initial Attempt (Beginner Approach)

I started with a simple list-based solution:

```python
log_file = ["Error", "Info", "Erro", "Warning"]

counte = []
counti = []
countw = []

for log in log_file:
    if "Error" in log:
        counte = counte + 1
    if "Info" in log:
        counti += 1
    if "Warning" in log:
        countw += 1

print(countw, countw, counti)
```

### ❗ Observations:

* Used lists instead of integers for counters
* Faced errors while incrementing
* Basic logic idea was correct, but implementation had issues

---

### 🔹 Step 2: Fixed Basic Version

Corrected the logic using integers:

```python
log_file = ["Error", "Info", "Error", "Warning"]

counte = 0
counti = 0
countw = 0

for log in log_file:
    if log == "Error":
        counte += 1
    elif log == "Info":
        counti += 1
    elif log == "Warning":
        countw += 1

print("Error:", counte)
print("Info:", counti)
print("Warning:", countw)
```

### ✅ Learning:

* Proper variable initialization
* Correct use of conditions and loops

---

### 🔹 Step 3: Improved Approach (Dictionary – Scalable)

Moved to a better design using dictionary:

```python
log_file = ["Error", "Info", "Error", "Warning"]

counts = {
    "Error": 0,
    "Info": 0,
    "Warning": 0
}

for log in log_file:
    if log in counts:
        counts[log] += 1

print(counts)
```

### ✅ Learning:

* Cleaner and scalable approach
* Better for real-world scenarios

---

## 🚀 Step 4: Working with Real Log Files

### ❌ My Attempt:

```python
import os

counts = {
    "Error": 0,
    "Info": 0,
    "Warning": 0
}

log_file = vars/logs/cloudwatch

with open("log_file") as log:
    data = log.readlines

if counts in data.lower():
    counts[data] += 1

print(counts)
```

### ❗ Issues Faced:

* Incorrect file path syntax
* Incorrect file reading method
* Wrong condition logic
* Misuse of dictionary

---

### ✅ Correct Version (File Handling + Case Handling)

```python
log_file = "vars/logs/cloudwatch"

counts = {
    "error": 0,
    "info": 0,
    "warning": 0
}

with open(log_file, "r") as log:
    for line in log:
        line = line.lower()

        if "error" in line:
            counts["error"] += 1
        elif "info" in line:
            counts["info"] += 1
        elif "warning" in line:
            counts["warning"] += 1

print(counts)
```

### ✅ Learning:

* File reading using `with open()`
* Looping line-by-line
* Handling case sensitivity

---

## ⚡ Step 5: Adding Error Handling

```python
try:
    with open(log_file, "r") as log:
        for line in log:
            line = line.lower()

            if "error" in line:
                counts["Error"] += 1
            elif "info" in line:
                counts["Info"] += 1
            elif "warning" in line:
                counts["Warning"] += 1

    print(counts)

except FileNotFoundError:
    print("Log file not Found")
```

### ✅ Learning:

* Exception handling using `try-except`
* Handling missing files gracefully

---

## 🧾 Step 6: Final Version with Report Generation

```python
import os 

counts = {
    "Error": 0,
    "Info": 0,
    "Warning": 0
}

log_file = "logs/cloudwatch"

try:
    with open(log_file, "r") as log:
        for line in log:
            line = line.lower()
        
            if "error" in line:
                counts["Error"] += 1
            elif "info" in line:
                counts["Info"] += 1
            elif "warning" in line:
                counts["Warning"] += 1
         
    print(counts)
    
except FileNotFoundError:
    print("Log file not Found")

result = "report.txt "
with open(result, "a") as file:
    file.write(str(counts))
```

---

## 💡 Final Learnings from Day 1

### ✅ Technical Skills Covered:

* Loops (`for`)
* Conditions (`if / elif`)
* Dictionaries
* File handling (`open`)
* Exception handling (`try-except`)

---

### ✅ DevOps Concepts Learned:

* Log parsing
* Automation scripting
* Handling real-world data
* Generating reports

---

### 🧠 Key Takeaway

Started with a basic idea → made mistakes → fixed logic → improved structure → handled real files → generated report.

This shows **step-by-step problem-solving approach**, which is important in real DevOps work and interviews.

---

## 🚀 Day 1 Status

✔ Completed core logic
✔ Implemented real-world scenario
✔ Generated output report


