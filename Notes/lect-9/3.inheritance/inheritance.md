# What is Inheritance?

  Inheritance means one class (child) can use or extend the properties and methods of another class (parent).

## In simple words:

You create a new class based on an existing class — without rewriting all the code again.

## Real-Life Example:

A Father has some properties (like surname, house, car).

A Son inherits them — he doesn’t need to recreate them.

That’s inheritance!

### 1. Basic Example

```py

# Parent class
class Parent:
    def display_parent(self):
        print("This is the parent class")

# Child class
class Child(Parent):    # inherits from Parent
    def display_child(self):
        print("This is the child class")

# Create object
obj = Child()
obj.display_parent()   # from Parent class
obj.display_child()    # from Child class

#Output
This is the parent class
This is the child class

```
## Why Use Inheritance?

✔ Code Reuse → No need to rewrite existing code
✔ Easier Maintenance → Parent class updates reflect in children
✔ Better Organization → Shared logic in parent, specific logic in child

## Types of Inheritance in Python

| Type                         | Description                               | Example                       |
| ---------------------------- | ----------------------------------------- | ----------------------------- |
| **Single Inheritance**       | One child inherits from one parent        | `class B(A)`                  |
| **Multiple Inheritance**     | One child inherits from multiple parents  | `class C(A, B)`               |
| **Multilevel Inheritance**   | Inheritance chain                         | `class C(B)` and `class B(A)` |
| **Hierarchical Inheritance** | Multiple children inherit from one parent | `class B(A)`, `class C(A)`    |
| **Hybrid Inheritance**       | Combination of above types                | Mix of different structures   |

# (A) Single Inheritance

```py
class Animal:
    def eat(self):
        print("Animals can eat")

class Dog(Animal):
    def bark(self):
        print("Dogs can bark")

d = Dog()
d.eat()
d.bark()

```
# (B) Multilevel Inheritance

```py
class Grandparent:
    def house(self):
        print("Grandparent’s house")

class Parent(Grandparent):
    def car(self):
        print("Parent’s car")

class Child(Parent):
    def bike(self):
        print("Child’s bike")

obj = Child()
obj.house()
obj.car()
obj.bike()

##Output
Grandparent’s house
Parent’s car
Child’s bike

```
# (C) Multiple Inheritance

```py
class Father:
    def skills(self):
        print("Father: driving, gardening")

class Mother:
    def skills(self):
        print("Mother: cooking, painting")

class Child(Father, Mother):
    def skills(self):
        print("Child: ", end="")
        Father.skills(self)
        Mother.skills(self)

c = Child()
c.skills()

## output
Child: Father: driving, gardening
Mother: cooking, painting

```
# (D) Hierarchical Inheritance

```py
class Parent:
    def show(self):
        print("Parent class")

class Son(Parent):
    def display(self):
        print("Son class")

class Daughter(Parent):
    def display(self):
        print("Daughter class")

s = Son()
d = Daughter()
s.show()
d.show()

#output
Parent class
Parent class

```
## Using super() Keyword

super() is used to call the parent class’s constructor or methods inside the child class.

```py

class Parent:
    def __init__(self):
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()      # calls Parent’s __init__
        print("Child constructor")

obj = Child()

#output
Parent constructor
Child constructor


```
## Method Overriding

If the child class defines a method with the same name as in the parent, the child’s version overrides the parent’s one.

```py
class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        print("Child method")

c = Child()
c.show()
# output
Child method

```

# Report

| Concept         | Meaning                                             |
| --------------- | --------------------------------------------------- |
| **Inheritance** | Allows a class to reuse features from another class |
| **Syntax**      | `class Child(Parent):`                              |
| **super()**     | Used to call parent methods or constructors         |
| **Overriding**  | Redefining parent methods in the child              |
| **Types**       | Single, Multiple, Multilevel, Hierarchical, Hybrid  |
