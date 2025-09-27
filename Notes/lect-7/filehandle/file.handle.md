# File Handling in Python (Basics)

Python uses the built-in open() function for file operations.

Syntax:

```py

open(filename, mode)

```
Common Modes:

"r" → read (default)

"w" → write (overwrites file)

"a" → append (adds to file)

"x" → create new file (error if file exists)

"rb"/"wb" → read/write in binary

# Reading Text Files

```py
# Open file in read mode
file = open("sample.txt", "r")

# Read entire file
content = file.read()
print(content)

file.close()

```
# Other useful methods:
```py
file.readline()   # reads one line
file.readlines()  # reads all lines into a list
```

# Example (sample.txt):

```py
Hello World
Welcome to Python

# o/p
Hello World
Welcome to Python
```
# Writing Text Files
```py
# Open file in write mode (creates new or overwrites existing)
file = open("sample.txt", "w")
file.write("This is my first line.\n")
file.write("This is my second line.")
file.close()

```
# Appending to Files

```py
# Open file in append mode
file = open("sample.txt", "a")
file.write("\nThis line is added at the end.")
file.close()

```
# Now sample.txt will contain:
```py
This is my first line.
This is my second line.
This line is added at the end.

```

# Best Practice → Use with (auto close)

```py
with open("sample.txt", "r") as f:
    print(f.read())

```
No need to `call close()`, Python handles it.

# Summary

"r" → read (error if file doesn’t exist)

"w" → write (creates new, overwrites existing)

"a" → append (adds content at the end)

Always close() the file (or use with).