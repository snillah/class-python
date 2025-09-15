
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flat = [num for row in matrix for num in row]
print(flat)


doubled = [[num * 2 for num in row] for row in matrix]
print(doubled)