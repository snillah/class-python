# f-strings & string formatting in Python.

## f-Strings (Formatted String Literals, Python 3.6+)

### Start the string with f or F.

Place variables or expressions inside {} braces.

```py
name = "Alice"
age = 25

print(f"My name is {name} and I am {age} years old.")
print(f"Next year, I’ll be {age + 1}.")

#o/p
My name is Alice and I am 25 years old.
Next year, I’ll be 26.
```

### Formatting numbers with f-strings

```py
pi = 3.14159
print(f"Pi value: {pi:.2f}")   # 2 decimal places
print(f"Binary of 5: {5:b}")   # Binary
print(f"Hex of 255: {255:x}")  # Hexadecimal

#o/p
Pi value: 3.14
Binary of 5: 101
Hex of 255: ff

```

## str.format() Method (Older, still useful)

```py
name = "Bob"
lang = "Python"

print("Hello, my name is {} and I love {}.".format(name, lang))

# o/p
Hello, my name is Bob and I love Python.

```
### Positional & Keyword formatting

```py
print("{0} is learning {1}".format("Alice", "Python"))
print("{name} loves {language}".format(name="Bob", language="Java"))

# o/p
Alice is learning Python
Bob loves Java

```
### Formatting numbers with format()

```py
pi = 3.14159
print("Pi value: {:.2f}".format(pi))
print("Binary of 5: {:b}".format(5))
print("Hex of 255: {:x}".format(255))

```
##  Old % Formatting (C-style, less used now)

using % - d%,s%

```py
name = "Charlie"
age = 30
print("My name is %s and I am %d years old." % (name, age))

#o/p
My name is Charlie and I am 30 years old.

```

| Method             | Example                        | Best For                                 |
| ------------------ | ------------------------------ | ---------------------------------------- |
| **f-strings**      | `f"{name} is {age}"`           |  Modern, readable, supports expressions |
| **`.format()`**    | `"{} is {}".format(name, age)` |  Compatible with older Python versions  |
| **`%` formatting** | `"%s is %d" % (name, age)`     |  Legacy, not recommended                  |
