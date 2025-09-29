# Polymorphism → same method name, different behavior.

```py
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Woof")

for animal in (Cat(), Dog()):
    animal.sound()


```