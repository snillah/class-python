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
