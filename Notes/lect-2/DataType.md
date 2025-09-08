# What is a Data Type?

A data type defines the kind of value a variable can hold and what operations can be performed on it.

In simple words:

A data type tells what type of data is stored (number, text, list, etc.).

Example: If x = 10, Python knows it’s an integer (int).


# The basic data types in Python with examples.


1. Integer (int)

Whole numbers (positive or negative) without decimals.

Examples: 10, -25, 0

```py
a = 10
b = -5
print(type(a))   # <class 'int'>
```
2. Float (float)

Numbers with decimals or in scientific notation.

Examples: 3.14, -0.5, 2e3 (2000.0)

```py
pi = 3.14
temperature = -5.6
print(type(pi))   # <class 'float'>

```
3. String (str)

Sequence of characters enclosed in single quotes ' ', double quotes " ", or triple quotes ''' ''' / """ """.

Examples: "Hello", 'Python'


```py
name = "Python"
msg = 'Hello, World!'
multiline = """This is
a multi-line string"""
print(type(name))   # <class 'str'>

```
4. Boolean (bool)

Represents truth values: True or False

Often used in conditions and comparisons.
```py
x = True
y = False
print(type(x))     # <class 'bool'>

print(10 > 5)      # True
print(3 == 7)      # False
```

| Data Type | Example Values        | Description       |
| --------- | --------------------- | ----------------- |
| **int**   | `10`, `-25`, `0`      | Whole numbers     |
| **float** | `3.14`, `-0.5`, `2e3` | Decimal numbers   |
| **str**   | `"Hello"`, `'Python'` | Text (characters) |
| **bool**  | `True`, `False`       | Logical values    |
