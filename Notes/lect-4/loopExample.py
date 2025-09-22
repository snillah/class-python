matrix = matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flat = [num for row in matrix for num in row]
print(flat)

value = []
for x in matrix:
    for v in x:
        value.append(v)

print(value)