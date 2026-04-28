Got it — I’ll structure your **Day 3 journey into clean, reusable notes** just like Day 1 & Day 2.

---

# 📘 Day 3 Notes – Config-Based Monitoring Script (DevOps Python)

---

## 🧩 🟢 Scenario (Real DevOps Use Case)

**Role:** DevOps Engineer
**Task:** Improve system monitoring script

### 🎯 Problem

In Day 2, threshold values were hardcoded:

```python
if cpu > 80:
```

### ❌ Issue:

* Every change requires code update
* Not scalable in real environments

---

## 🚀 Day 3 Goal

👉 Move configuration (threshold values) **outside the code**

### ✅ New Approach:

* Store values in a config file
* Read them dynamically in Python

---

## 🧠 Core Concept

| Component     | Role              |
| ------------- | ----------------- |
| Python Script | Logic             |
| config.json   | Settings (values) |

👉 Code reads values → compares → takes action

---

## 📂 Step 1: Create Config File

**config.json**

```json
{
    "cpu_threshold": 80,
    "memory_threshold": 80,
    "disk_threshold": 80
}
```

### ✅ Learning:

* JSON is like a Python dictionary
* Used to store configuration values

---

## 🟢 Step 2: Read Config in Python

```python
import json

with open("config.json") as f:
    config = json.load(f)

print(config["cpu_threshold"])
```

### ✅ Learning:

* `json.load()` converts JSON → dictionary
* Access values using keys

---

## 🟡 Step 3: Connect Config with Monitoring

```python
import psutil
import json

with open("config.json") as f:
    config = json.load(f)

cpu = psutil.cpu_percent()

print("CPU:", cpu)

if cpu > config["cpu_threshold"]:
    print("⚠️ High CPU Usage")
```

### 🔄 Key Change:

Before:

```python
if cpu > 80
```

Now:

```python
if cpu > config["cpu_threshold"]
```

### ✅ Learning:

* Removed hardcoding
* Values now dynamic

---

## 🔁 Step 4: Add Loop (Controlled Execution)

```python
import time

for _ in range(5):
    # monitoring logic
    time.sleep(2)
```

### ✅ Learning:

* Run script multiple times
* Useful for testing (instead of infinite loop)

---

## 🧾 Step 5: Full Working Script

```python
import psutil
import json
import time
from datetime import datetime

# read config
with open("config.json", "r") as file:
    data = json.load(file)

for _ in range(3):

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    print(f"\nTime: {current_time}")
    print(f"CPU usage is {cpu}%")
    print(f"Memory usage is {memory}%")
    print(f"Disk usage is {disk}%")

    if cpu > data["cpu_threshold"]:
        print("⚠️ CPU usage is high")

    if memory > data["memory_threshold"]:
        print("⚠️ Memory usage is high")

    if disk > data["disk_threshold"]:
        print("⚠️ Disk usage is high")

    # write to file
    with open("output.txt", "a") as output:
        output.write(f"Time: {current_time}\n")
        output.write(f"CPU: {cpu}%\n")
        output.write(f"Memory: {memory}%\n")
        output.write(f"Disk: {disk}%\n\n")

    time.sleep(3)
```

---

## 🧠 Key Concepts Learned

---

### 🔸 1. Why Config Files?

👉 Avoid changing code again and again

Example:

* Change threshold → update JSON
* No need to modify Python script

---

### 🔸 2. What is JSON?

👉 A format to store structured data

Looks like:

```json
{
  "cpu_threshold": 80
}
```

👉 Same as Python dictionary

---

### 🔸 3. Code Flow (Important)

Every iteration:

1. Read config values
2. Get system metrics
3. Compare values
4. Print alerts
5. Save output

---

### 🔸 4. Separation of Concerns

* Code handles **logic**
* Config handles **values**

👉 This is real DevOps design

---

### 🔸 5. Loop Control

```python
for _ in range(3):
```

* Runs script limited times
* Useful for testing

---

## 💡 Example Output

```
Time: 2026-04-28 10:30:01
CPU usage is 45%
Memory usage is 60%
Disk usage is 70%

Time: 2026-04-28 10:30:04
CPU usage is 85%
⚠️ CPU usage is high
```

🚀 Next Step (Final Day 3 Upgrade)

If you want to go one level higher, next we can:

Add alerts into file also
Add separate log file per day
Make it run like a real service


import psutil
import json
import time
from datetime import datetime

# load config
with open("config.json", "r") as file:
    data = json.load(file)

while True:

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file = datetime.now().strftime("%Y-%m-%d") + ".txt"

    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    alerts = []

    if cpu > data["cpu_threshold"]:
        alerts.append("CPU usage is high")

    if memory > data["memory_threshold"]:
        alerts.append("Memory usage is high")

    if disk > data["disk_threshold"]:
        alerts.append("Disk usage is high")

    print(f"\nTime: {current_time}")
    print(f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%")

    for alert in alerts:
        print("⚠️", alert)

    with open(log_file, "a") as output:
        output.write(f"Time: {current_time}\n")
        output.write(f"CPU: {cpu}%\n")
        output.write(f"Memory: {memory}%\n")
        output.write(f"Disk: {disk}%\n")

        for alert in alerts:
            output.write(f"⚠️ {alert}\n")

        output.write("\n")

    time.sleep(5)




---

## 🚀 Day 3 Status

✔ Removed hardcoded values
✔ Introduced config file (JSON)
✔ Connected config with logic
✔ Implemented monitoring loop
✔ Saved output to file
  Dynamic daily log files (advanced concept)

---

## 🧠 Key Takeaway

Moved from:

* Hardcoded script → Config-driven system
* Fixed values → Dynamic values
🧠 What you just built (VERY IMPORTANT)

👉 This is now:

Continuous monitoring
Daily log rotation
Alert system
Config-driven

---


