add = lambda a,b:a+b
square = lambda a,b: a**b

print(add(5,12))
print(square(5,3))

oddOrEven = lambda x :"Even" if (x % 2 == 0 ) else "Odd"

print(oddOrEven(76))

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

flat = [num for row in matrix for num in row]
print(flat)

mul = [[num *3 for num in row] for row in matrix]
print(mul)