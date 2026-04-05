
# 🔹 What is he trying to teach here?

This whole section is about:

👉 **How Python interacts with your Operating System (OS)**
👉 **How to manage files, folders, and paths using Python**

In DevOps, this is used for:

* automation scripts
* file cleanup
* log management
* config handling

---

# 🧠 1. `os` module — Simple meaning

👉 Think of `os` as:

> “Python talking to your system (Linux/Windows)”

It lets Python do things like:

* create folder
* delete file
* check file info
* change permissions

---

## 🔹 Example functions (VERY IMPORTANT)

### 1. List files in a folder

```python
import os
print(os.listdir('.'))
```

👉 Output:

```
['file1.txt', 'test.py']
```

👉 Means: "show all files in current directory"

---

### 2. Create folder

```python
os.mkdir("myfolder")
```

👉 Creates folder like `mkdir` command in Linux

---

### 3. Delete file

```python
os.remove("file.txt")
```

👉 Same as:

```
rm file.txt
```

---

### 4. Rename file

```python
os.rename("old.txt", "new.txt")
```

---

### 5. Change permission

```python
os.chmod("file.py", 0o777)
```

👉 Same as:

```
chmod 777 file.py
```

---

### 6. Get file details

```python
os.stat("file.txt")
```

👉 Gives:

* size
* last accessed
* permissions

---

# 🔹 DevOps connection

You use this for:

* log cleanup scripts
* deployment scripts
* file monitoring

---

Got it 👍 — this time I’ll slow down and explain **properly like a beginner**, not just “what” but also:

👉 **why we use it**
👉 **what problem it solves**
👉 **what exactly happens step-by-step**

---

# 🧠 First Understand the BIG PICTURE

In DevOps, we always deal with:

* files (logs, configs)
* folders (projects, backups)
* paths (where files are stored)

👉 Python `os` module helps you **automate all this instead of doing manually**

---

# 🔹 1. Why do we even need `os` module?

### ❓ Problem (Real Life)

You normally do things like:

```bash
ls
mkdir test
rm file.txt
chmod 777 script.sh
```

👉 These are **manual commands**

---

### ✅ Solution

We want Python to do this automatically:

```python
import os
```

👉 Now Python can behave like a **Linux terminal**

---

# 🔹 2. `os.listdir()` — WHAT + WHY + HOW

```python
import os
os.listdir('.')
```

---

### 🔍 What it does

👉 Shows all files inside a folder

---

### ❓ Why we use it

👉 Suppose:

* You want to delete old logs
* You want to backup files

First you need to **know what files exist**

---

### ⚙️ How it works

```python
os.listdir('.')
```

* `.` means → current folder
* Python asks OS → “give me file list”
* OS returns list

---

### 📦 Output

```python
['file1.txt', 'app.log', 'script.py']
```

---

# 🔹 3. `os.mkdir()` — WHAT + WHY + HOW

```python
os.mkdir("backup")
```

---

### 🔍 What it does

👉 Creates a folder

---

### ❓ Why we use it

👉 Example:

* Before backup → create backup folder
* Before deployment → create directory

---

### ⚙️ Action

👉 Same as Linux:

```bash
mkdir backup
```

---

# 🔹 4. `os.remove()` — WHAT + WHY

```python
os.remove("file.txt")
```

---

### 🔍 What it does

👉 Deletes a file

---

### ❓ Why we use it

👉 DevOps use case:

* delete logs older than 7 days
* clean temp files

---

### ⚠️ Important

👉 Only deletes files, NOT folders

---

# 🔹 5. `os.rename()` — WHAT + WHY

```python
os.rename("old.txt", "new.txt")
```

---

### 🔍 What it does

👉 Renames file

---

### ❓ Why we use it

👉 Example:

* rotate logs → `app.log` → `app.log.1`

---

# 🔹 6. `os.chmod()` — VERY IMPORTANT

```python
os.chmod("file.sh", 0o777)
```

---

### 🔍 What it does

👉 Changes file permissions

---

### ❓ Why we use it

👉 Example:

* Make script executable
* Give access to users

---

### 🔥 Real DevOps use

Before running script:

```bash
chmod +x script.sh
```

👉 Python version = `os.chmod()`

---

# 🔹 7. `os.stat()` — WHAT + WHY

```python
os.stat("file.txt")
```

---

### 🔍 What it gives

👉 File information:

* size
* last modified
* permissions

---

### ❓ Why needed

👉 Example:

* find large files
* check last used file

---

# 🧠 NOW MOST IMPORTANT PART → `os.path`

---

# 🔹 Why `os.path` is needed?

### ❓ Problem

Paths differ:

* Windows → `C:\Users\Roshni\file.txt`
* Linux → `/home/roshni/file.txt`

👉 Hardcoding path = ❌ BAD

---

### ✅ Solution

```python
os.path
```

👉 Handles paths safely across OS

---

# 🔹 8. `os.path.join()` — VERY VERY IMPORTANT

```python
os.path.join("folder", "file.txt")
```

---

### 🔍 What it does

👉 Combines path safely

---

### ❓ Why needed

❌ Wrong:

```python
"folder/" + "file.txt"
```

👉 Breaks in Windows

---

✅ Correct:

```python
os.path.join("folder", "file.txt")
```

---

### ⚙️ Output

Windows:

```python
folder\file.txt
```

Linux:

```python
folder/file.txt
```

---

# 🔹 9. `os.path.exists()`

```python
os.path.exists("file.txt")
```

---

### 🔍 What it does

👉 Checks if file exists

---

### ❓ Why needed

👉 Avoid errors like:

```
FileNotFoundError
```

---

# 🔹 10. `os.path.isfile()` & `isdir()`

```python
os.path.isfile("file.txt")
os.path.isdir("folder")
```

---

### 🔍 What they do

👉 Check type of path

---

### ❓ Why needed

👉 Example:

* If file → read it
* If folder → go inside

---

# 🔥 VERY IMPORTANT (REAL SCRIPT FLOW)

---

## Example: Scan folder

```python
import os

files = os.listdir(".")

for f in files:
    if os.path.isfile(f):
        print("This is file:", f)
    elif os.path.isdir(f):
        print("This is folder:", f)
```

---

### 🧠 What’s happening step-by-step

1. Get all items
2. Loop each item
3. Check:

   * file?
   * folder?

---

# 🔥 FINAL PART → Walking directories (RECURSION)

---

## Why needed?

👉 Real DevOps scenario:

```
/logs
   /app1
       log1.log
   /app2
       log2.log
```

👉 You must go inside all folders

---

## Code

```python
def walk(path):
    items = os.listdir(path)

    for item in items:
        full_path = os.path.join(path, item)

        if os.path.isfile(full_path):
            print("File:", full_path)

        elif os.path.isdir(full_path):
            walk(full_path)
```

---

## 🧠 Step-by-step

1. Take folder
2. List items
3. For each item:

   * if file → print
   * if folder → go inside again

---

👉 This is called **recursion**

---

# 🔥 FINAL SIMPLE SUMMARY

👉 You learned:

| Concept        | Why            |
| -------------- | -------------- |
| `os`           | control system |
| `listdir`      | see files      |
| `mkdir`        | create folder  |
| `remove`       | delete file    |
| `chmod`        | permissions    |
| `os.path.join` | safe paths     |
| `exists`       | avoid errors   |
| `isfile/isdir` | identify type  |
| recursion      | scan folders   |

---

# 💡 Real DevOps Example

👉 Delete logs older than 7 days:

* list files
* check date
* delete using `os.remove`

---

