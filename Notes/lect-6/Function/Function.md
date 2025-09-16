# Function 

1) What is a Function?
A function is a block of code that:

Runs only when called.

Can take inputs (parameters).

Can return an output (result).

Helps avoid repeating the same code.

Eg:
Think of it like a machine:

You give input → the function does work → gives output.


2) Why Use Functions?

To make code organized.
    To avoid repetition.
    To reuse code anywhere.
    Makes debugging & maintenance easier.

3) Defining a Function

Use the `def` keyword.

```py
def greet():
    print("Hello, welcome to Python!")

```

4) Calling a Function
```py
greet()
```

5) Function with Parameters

You can pass values (arguments).

```py
def greet(name):
    print("Hello", name)

greet("Alice")   # Output: Hello Alice
greet("Bob")     # Output: Hello Bob

```

6) Function with Return Value

Functions can return a result using return.

```py
def add(a, b):
    return a + b

result = add(5, 3)
print(result)   # 8

```

7) Default Parameters

If you don’t give a value, Python uses the default.

```py
def greet(name="Guest"):
    print("Hello", name)

greet()          # Hello Guest
greet("Alice")   # Hello Alice

```
Combining Positional & Default Arguments
```py
def student(name, age=18):
    print("Name:", name, "| Age:", age)

student("Bob")          # Name: Bob | Age: 18
student("Alice", 21)    # Name: Alice | Age: 21

```
Here:
name → positional argument (must be provided).
age → default argument (optional).

Positional Argument → order matters.
Default Argument → value is optional, Python uses default if not given.

8) Keyword Arguments
You can pass values using parameter names.

```py
def student(name, age):
    print(f"Name: {name}, Age: {age}")

student(age=21, name="Alice")

# o/p
Name: Alice, Age: 21

```

9) Returning Multiple Values

Python can return multiple values as a tuple.

```py

def calc(a, b):
    return a+b, a-b, a*b

res = calc(10, 5)
print(res)         # (15, 5, 50)

x, y, z = calc(10, 5)
print(x, y, z)     # 15 5 50

```

Quick Summary

Function = reusable block of code.

Defined using def.

Can take arguments and return values.

Supports default values, keyword args, multiple returns.