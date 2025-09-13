# Loops:

1) for Loop Basics
Used to iterate (loop) over a sequence (list, string, tuple, range, etc.).

```py
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

#o/p
apple
banana
cherry

```

2) while Loop Basics
Runs as long as the condition is True.

```py
count = 1
while count <= 5:
    print(count)
    count += 1

#o/p
1
2
3
4
5

```

3) Loop Control Statements

break → Exit the loop immediately

```py

for i in range(1, 6):
    if i == 3:
        break
    print(i)

#o/p
1
2

```
continue → Skip current iteration, continue next

```py
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
 
#o/P
1
2
4
5

```
pass → Do nothing (placeholder)

```py
for i in range(1, 4):
    if i == 2:
        pass  # just a placeholder
    print(i)

#o/p
1
2
3

```

4) Using range() with Loops

range(start, stop, step) generates a sequence of numbers.
```py
# Example 1: simple range
for i in range(5):
    print(i)

#o/p
0
1
2
3
4

```
```py
# Example 3: with start,stop,step
for i in range(1, 10, 2):
    print(i)

# op
1
3
5
7
9

```
| Loop Type    | Use                                                |
| ------------ | -------------------------------------------------- |
| **for**      | Iterate over sequence (list, tuple, string, range) |
| **while**    | Repeat while condition is True                     |
| **break**    | Exit loop completely                               |
| **continue** | Skip current iteration                             |
| **pass**     | Do nothing (placeholder)                           |
| **range()**  | Generate numbers for looping                       |

# What is a Nested Loop?

A loop inside another loop.

The outer loop runs first.

For each iteration of the outer loop, the inner loop runs completely.

1. Simple Nested Loop:
```py
for i in range(3):          # Outer loop
    for j in range(2):      # Inner loop
        print(f"i={i}, j={j}")


#o/p:
i=0, j=0
i=0, j=1
i=1, j=0
i=1, j=1
i=2, j=0
i=2, j=1
# Here, for each i, the full inner loop runs.
```

2. Multiplication Table
```py
for i in range(1, 4):        # Outer loop (rows)
    for j in range(1, 4):    # Inner loop (columns)
        print(i * j, end=" ")
    print()   # Move to next line after inner loop

# o/p
1 2 3 
2 4 6 
3 6 9 

```

3. Star Pattern (Pyramid Shape)
```py
for i in range(1, 6):      # Outer loop (rows)
    for j in range(i):     # Inner loop (columns)
        print("*", end=" ")
    print()

# o/p
* 
* * 
* * * 
* * * * 
* * * * * 
```

4. Using while in Nested Loops
```py
i = 1
while i <= 3:       # Outer loop
    j = 1
    while j <= 2:   # Inner loop
        print(f"i={i}, j={j}")
        j += 1
    i += 1
# o/p
i=1, j=1
i=1, j=2
i=2, j=1
i=2, j=2
i=3, j=1
i=3, j=2


```