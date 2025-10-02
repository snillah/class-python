

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



# polymorphism

class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Woof")

for animal in (Cat(), Dog()):
    animal.sound()

