# What is a Module?

A module is simply a Python file (.py) that contains functions, classes, or variables you can reuse in other programs.

```py
import math
print(math.sqrt(16))

```
Here, math is a module that gives access to math functions like sqrt().

## Common & Useful Python Modules (Beginner Level)

| No  | Module           | Purpose                                | Example                                |
| --- | ---------------- | -------------------------------------- | -------------------------------------- |
| 1️⃣ | **math**         | Mathematical functions                 | `math.sqrt(25)`, `math.pi`             |
| 2️⃣ | **random**       | Generate random numbers                | `random.randint(1, 10)`                |
| 3️⃣ | **datetime**     | Work with date & time                  | `datetime.datetime.now()`              |
| 4️⃣ | **os**           | Work with files, folders, system paths | `os.getcwd()`, `os.listdir()`          |
| 5️⃣ | **sys**          | System-level info & arguments          | `sys.version`, `sys.argv`              |
| 6️⃣ | **statistics**   | Mean, median, mode                     | `statistics.mean([1,2,3])`             |
| 7️⃣ | **math / cmath** | Real & complex math                    | `cmath.sqrt(-1)`                       |
| 8️⃣ | **time**         | Handle delays & timestamps             | `time.sleep(2)`                        |
| 9️⃣ | **json**         | Read/write JSON data                   | `json.loads()`, `json.dumps()`         |
| 🔟  | **collections**  | Extra data structures                  | `Counter`, `defaultdict`, `namedtuple` |

1. math module

Used for mathematical operations.
```py
import math

print(math.sqrt(16))    # 4.0
print(math.ceil(4.3))   # 5
print(math.floor(4.7))  # 4
print(math.pi)          # 3.141592...

```

2. random module

Used to generate random numbers or choices.

```py
import random

print(random.randint(1, 10))   # Random number between 1 and 10
print(random.choice(["red", "green", "blue"]))  # Randomly pick an item

```
3. datetime module

Used for working with dates and times.
```py
import datetime

now = datetime.datetime.now()
print("Current time:", now)
print("Year:", now.year)
print("Month:", now.month)

```
4. os module

Used for interacting with the operating system.

```py
import os

print(os.getcwd())        # Get current working directory
print(os.listdir())       # List files in directory
# os.mkdir("test_folder") # Create a folder

```
5. sys module

Gives system information and handles command-line arguments.

```py
import sys

print(sys.version)        # Python version
print(sys.platform)       # Platform info

```

6. time module

For delays, timestamps, and measuring execution time.

```py
import time

print(time.time())      # current timestamp
time.sleep(2)           # pauses execution for 2 seconds
print("Done waiting")

```
7. json module

Used to work with JSON (very common in APIs).
```py
import json

data = {"name": "Alice", "age": 25}
json_str = json.dumps(data)       # Convert dict → JSON
print(json_str)

python_dict = json.loads(json_str) # Convert JSON → dict
print(python_dict["name"])

```

8. statistics module

Useful for mathematical and statistical operations.

```py
import statistics

data = [10, 20, 30, 40]
print(statistics.mean(data))   # 25
print(statistics.median(data)) # 25
print(statistics.mode([1,1,2])) # 1


```

10. platform module

Gives details about the system’s hardware and OS.

```py
import platform

print(platform.system())      # Windows / Linux / MacOS
print(platform.processor())   # CPU info

```

# Report

| Module        | Purpose                          |
| ------------- | -------------------------------- |
| `math`        | Mathematical functions           |
| `random`      | Random number generation         |
| `datetime`    | Date & time operations           |
| `os`          | Interacting with the file system |
| `sys`         | System-level info                |
| `time`        | Delays, timestamps               |
| `json`        | Read/write JSON data             |
| `statistics`  | Statistical operations           |
| `collections` | Advanced data structures         |
| `platform`    | System information               |
