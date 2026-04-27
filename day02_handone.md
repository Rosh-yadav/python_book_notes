# 📘 Day 2 Notes – System Monitoring Script (DevOps Python)

**Task:** Monitor system health of a server

### 🎯 Goal

Build a Python script that:

* Checks CPU usage
* Checks Memory usage
* Checks Disk usage
* Prints alerts if usage is high

---

## 🧠 🟡 My Learning Journey

---

### 🔹 Step 1: Basic System Monitoring Functions

Started by using `psutil` to get system metrics:

```python
import psutil

def check_cpu():
    return psutil.cpu_percent()

def check_memory():
    return psutil.virtual_memory().percent

def check_disk():
    return psutil.disk_usage('/').percent

cpu = check_cpu()
memory = check_memory()
disk = check_disk()

print(f"CPU: {cpu}%")
print(f"Memory: {memory}%")
print(f"Disk: {disk}%")
```

### ✅ Learning:

* Using external library (`psutil`)
* Creating reusable functions
* Fetching system metrics

---

### 🔹 Step 2: Adding Alerts

```python
if cpu > 80:
    print("⚠️ High CPU Usage")

if memory > 80:
    print("⚠️ High Memory Usage")

if disk > 80:
    print("⚠️ High Disk Usage")
```

### ✅ Learning:

* Conditional checks
* Basic alert system

---

### 🔹 Step 3: Continuous Monitoring

```python
import time

while True:
    cpu = psutil.cpu_percent()
    print("CPU:", cpu)

    time.sleep(5)
```

### ✅ Learning:

* Infinite loop (`while True`)
* Adding delay using `time.sleep()`
* Real-time monitoring concept

---

### 🔹 Step 4: My Attempt (Initial Code)

```python
import psutil 
import time 
import os 

while True:
    def cpu_usage():
        return psutil.cpu_percent()

    def disk_usage():
        return psutil.disk_usage("/").percent

    def memory_usage():
        return psutil.virtual_memory().percent

    cpu = cpu_usage()
    memory = memory_usage()
    disk = disk_usage()

    if cpu > 80:
        print(f"cpu usage is :", {cpu})
    if memory > 80:
        print(f"memory usage is :", {memory})
    if disk > 80:
        print(f"disk usage is :", {disk})

    time.sleep(1)

output = print(cpu, memory, disk)

with open("system_report.txt", "a") as data:
    data.write()

print(data)
```

### ❗ Observations:

* Functions defined inside loop
* File writing logic incomplete
* `print()` used instead of storing output
* Not sure how to write data into file

---

### 🔹 Step 5: Clean & Correct Version

```python
import psutil
import time
from datetime import datetime

def cpu_usage():
    return psutil.cpu_percent()

def memory_usage():
    return psutil.virtual_memory().percent

def disk_usage():
    return psutil.disk_usage('/').percent


while True:
    cpu = cpu_usage()
    memory = memory_usage()
    disk = disk_usage()

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\nTime: {current_time}")
    print(f"CPU: {cpu}%")
    print(f"Memory: {memory}%")
    print(f"Disk: {disk}%")

    if cpu > 80:
        print("⚠️ High CPU Usage")
    if memory > 80:
        print("⚠️ High Memory Usage")
    if disk > 80:
        print("⚠️ High Disk Usage")

    with open("system_report.txt", "a") as file:
        file.write(f"Time: {current_time}\n")
        file.write(f"CPU: {cpu}%\n")
        file.write(f"Memory: {memory}%\n")
        file.write(f"Disk: {disk}%\n")

        if cpu > 80:
            file.write("⚠️ High CPU Usage\n")
        if memory > 80:
            file.write("⚠️ High Memory Usage\n")
        if disk > 80:
            file.write("⚠️ High Disk Usage\n")

        file.write("\n")

    time.sleep(5)
```

---

## 🧠 Key Concepts Learned

---

### 🔸 1. File Writing

```python
file.write("text")
```

* Must pass a string
* Use `\n` for new lines

---

### 🔸 2. Storing Output

Instead of:

```python
print(cpu)
```

Use:

```python
line = f"CPU: {cpu}%\n"
file.write(line)
```

### ✅ Learning:

* `print()` displays output
* `write()` stores output

---

### 🔸 3. Function Call `()`

```python
psutil.cpu_percent()
```

* `()` means calling/executing a function
* Without `()`, function will not run

---

### 🔸 4. datetime & strftime()

```python
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

* `datetime.now()` → current date & time
* `strftime()` → formats time into readable string

Example:

```python
"%H:%M:%S" → 16:45:12
```

---

### 🔸 5. Loop Control

```python
for _ in range(5):
```

* `range(5)` → runs loop 5 times
* `_` → variable not needed

---

## 🚀 Bonus Task

Modify script:

* Replace `while True` with:

```python
for _ in range(5):
```

* Helps in testing instead of infinite loop

---

## 💡 Example Output

```
Time: 10:30:01
CPU: 45%
Memory: 60%
Disk: 70%

Time: 10:30:06
CPU: 85% ⚠️ High CPU Usage
```


