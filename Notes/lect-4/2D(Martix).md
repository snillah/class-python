# Nested loops work with lists (2D arrays / matrices) in Python.

A list of lists.

```py
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:          # Outer loop → each row
    for element in row:     # Inner loop → each element in row
        print(element, end=" ")
    print()                 # Move to next line after row

# o/p
1 2 3 
4 5 6 
7 8 9 


```

2. Accessing by Index

```py
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

for i in range(len(matrix)):          # Row index
    for j in range(len(matrix[i])):   # Column index
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")
# o/p
matrix[0][0] = 10
matrix[0][1] = 20
matrix[0][2] = 30
matrix[1][0] = 40
matrix[1][1] = 50
matrix[1][2] = 60
matrix[2][0] = 70
matrix[2][1] = 80
matrix[2][2] = 90

```
3. Multiplying All Elements by 2

```py
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] *= 2   # Multiply each element by 2

print(matrix)

# o/p
[[2, 4], [6, 8], [10, 12]]


```

4. Printing Matrix in Grid Format

```py
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    print(" | ".join(str(x) for x in row))

# o/p
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9


```
Nested loops are perfect for 2D data (matrices, tables, grids).

Outer loop = row, Inner loop = column.

You can process, modify, or format data easily.
