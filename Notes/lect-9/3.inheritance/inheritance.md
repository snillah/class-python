# Inheritance → one class (child) inherits from another (parent).

```py

class Animal:
    def speak(self):
        print("This is an animal.")

     def eat(self):
        print("it can eat by mouth.")


class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        print("Woof! Woof!")

d = Dog()
d.speak()   # Woof! Woof!
d.eat()


```