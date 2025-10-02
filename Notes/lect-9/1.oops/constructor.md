# Constructor 
## What is a Constructor?

In Python, a constructor is a special method that automatically runs when an object is created.

It is always written as __init__().

```py
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Alice", 20)   # __init__ runs automatically
print(s1.name, s1.age)

# output
Alice 20


```
## How Many Constructors in Python?

In Python, there are two types of constructors:

### (A) Default Constructor

Takes only self (no arguments).

Used when you don’t pass any values.

```py
class Demo:
    def __init__(self):
        print("This is a default constructor")

d = Demo()

#output
This is a default constructor
```
### (B) Parameterized Constructor

Takes arguments along with self.

Used when you pass values during object creation.

```py

class Demo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

d = Demo("Alice", 21)
print(d.name, d.age)
# output
Alice 21
```
## Important Note 

Unlike Java or C++, Python does not support multiple constructors directly.

If you define more than one __init__, only the last one will work.

```py
class Demo:
    def __init__(self):
        print("First constructor")

    def __init__(self, name):
        print("Second constructor", name)

d = Demo("Alice")   # Works
# d = Demo()        # ❌ Error (missing argument)
```
## Workaround for Multiple Constructors

 Use default arguments or class methods.

Example (default arguments):

```py

class Demo:
    def __init__(self, name=None):
        if name is None:
            print("Default constructor")
        else:
            print("Parameterized constructor:", name)

d1 = Demo()          # Default constructor
d2 = Demo("Alice")   # Parameterized constructor: Alice

```
## Final Answer

Python has only one constructor method (__init__).

But it can behave as:

Default Constructor (no arguments).

Parameterized Constructor (with arguments).

Python does not support multiple constructors like Java, but we can simulate them using default arguments or @classmethod.