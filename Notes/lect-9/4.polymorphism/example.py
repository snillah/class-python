from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    radius =0
    def area(self,r):
        self.radius = r
        return 3.14 * self.radius**2

class Square(Shape):
    length =0
    def area(self,l):
        self.length = l
        return self.length * self.length

shapes = [Circle(), Square()]
for s in shapes:
    print(s.area(2))



class Distance:
    def __init__(self, km):
        self.km = km

    def __add__(self, other):
        return Distance(self.km + other.km)

    # def __str__(self):
    #     return f"{self.km} km"

d1 = Distance(50)
d2 = Distance(70)

print(d1 + d2)   # 120 km
