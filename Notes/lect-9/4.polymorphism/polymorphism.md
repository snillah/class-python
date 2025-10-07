# What is Polymorphism?

Polymorphism means “many forms”.
In simple terms — the same function or method name can behave differently depending on the object that calls it.

## Real-life Example:

Think of the word “run” —

A human runs (using legs 🏃‍♂️)

A car runs (on fuel 🚗)

A program runs (on a computer 💻)

The same action name ("run"), but different behaviors — that’s polymorphism!

# classifies

| Type                        | Example                               | Meaning                                     |
| --------------------------- | ------------------------------------- | ------------------------------------------- |
| Function Polymorphism       | `make_sound(dog)` / `make_sound(cat)` | Same function, different object             |
| Method Overriding           | Parent & Child class same method      | Child changes behavior                      |
| Built-in Polymorphism       | `len()`, `+`                          | Same operator/function, multiple data types |
| Operator Overloading        | `__add__`, `__sub__`                  | Custom meaning for operators                |
| Abstract Class Polymorphism | `area()` in different shapes          | Common interface, different implementation  |


## 1. Polymorphism with Functions and Objects

We can use the same function name for different objects:

```py
class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

# function using polymorphism
def make_sound(animal):
    print(animal.sound()) # parameter passing object

dog = Dog()
cat = Cat()

make_sound(dog)  # Bark
make_sound(cat)  # Meow

```
Explanation:

The same function make_sound() calls the sound() method.

But the behavior changes based on the object passed (Dog or Cat).


## 2. Polymorphism with Inheritance (Method Overriding)

When a child class changes (overrides) a method of the parent class.

```py
class Bird:
    def fly(self):
        print("Birds can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly")

b = Bird()
p = Penguin()

b.fly()   # Birds can fly
p.fly()   # Penguins cannot fly


```
Explanation:
Both classes have a method fly(), but the output depends on the object type.

## 3. Built-in Polymorphism

Python functions like len(), max(), or + work differently depending on data type:
```py
print(len("hello"))   # 5 (string length)
print(len([1, 2, 3])) # 3 (list length)

print(5 + 3)          # 8 (integer addition)
print("Hi" + "Bye")   # HiBye (string concatenation)

```
Same function/operator, different behavior → polymorphism.

## 4. Polymorphism with Abstract Classes

Using abstract base classes to enforce polymorphism.

```py
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5

class Square(Shape):
    def area(self):
        return 4 * 4

shapes = [Circle(), Square()]
for s in shapes:
    print(s.area())

```
Here, both classes implement the same method area() but behave differently — classic polymorphism.

## 5. Operator Overloading (Advanced Polymorphism)

Python lets you redefine operators for your own classes.

```py
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):   # Overloading + operator
        return self.pages + other.pages

b1 = Book(100)
b2 = Book(200)

print(b1 + b2)   # 300

```
Explanation:
The + operator is redefined using __add__() to add pages instead of numbers.