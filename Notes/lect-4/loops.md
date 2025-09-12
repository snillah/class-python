Loops:

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