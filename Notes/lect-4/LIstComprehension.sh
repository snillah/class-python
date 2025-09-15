What is a List Comprehension?

👉 A short way to create or transform lists instead of writing long for loops.

General Syntax:

[expression for item in iterable if condition]

 1. Flatten a 2D List

👉 Turn a matrix into a single list.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flat = [num for row in matrix for num in row]
print(flat)


✅ Output:

[1, 2, 3, 4, 5, 6, 7, 8, 9]

 2. Multiply Each Element by 2
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

doubled = [[num * 2 for num in row] for row in matrix]
print(doubled)


✅ Output:

[[2, 4], [6, 8], [10, 12]]

 3. Create a 3x3 Matrix with Zeros
zeros = [[0 for _ in range(3)] for _ in range(3)]
print(zeros)


✅ Output:

[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

 4. Generate Multiplication Table (3x3)
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(table)


✅ Output:

[[1, 2, 3], [2, 4, 6], [3, 6, 9]]

 5. Conditional List Comprehension (Only Even Numbers)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

evens = [num for row in matrix for num in row if num % 2 == 0]
print(evens)


✅ Output:

[2, 4, 6, 8]


Normal nested loops → more lines, step-by-step.

List comprehensions → one-line, cleaner, faster.

Useful for matrix creation, transformation, filtering.