# __init__ Constructor

Special method called when object is created (used to initialize values).

```py
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def drive(self):
        print(f"{self.color} {self.brand} is driving.")

car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

car1.drive()   # Red Toyota is driving.
car2.drive()   # Blue Honda is driving.


```