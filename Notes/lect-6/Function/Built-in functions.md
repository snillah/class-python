## What are Built-in Functions?

Python already comes with many functions that you can use without importing any library.
They save time because you don’t have to write code for common tasks.

Commonly Used Built-in Functions

1) len() → length of an object

```py
name = "Python"
print(len(name))   # 6

```
Works for strings, lists, tuples, sets, dicts, etc.

2) type() → tells the data type

```py
print(type(10))         # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type("Hello"))    # <class 'str'>
print(type([1,2,3]))    # <class 'list'>

```

3) sum() → adds numbers

```py
nums = [10, 20, 30]
print(sum(nums))              # 60
print(sum(nums, 100))         # 160 (adds starting value 100)

```
4) max() and min() → largest & smallest

```py
print(max(10, 20, 5))         # 20
print(min(10, 20, 5))         # 5

nums = [3, 7, 2, 9]
print(max(nums))    # 9
print(min(nums))    # 2

```

5) abs() → absolute value

```py
print(abs(-10))    # 10
print(abs(3.5))    # 3.5

```

6) round() → rounds numbers

```py
print(round(3.14159, 2))   # 3.14
print(round(5.678))        # 6

```

7) sorted() → returns sorted list

```py
nums = [5, 2, 8, 1]
print(sorted(nums))          # [1, 2, 5, 8]
print(sorted(nums, reverse=True))   # [8, 5, 2, 1]
```
8) id() → returns memory location of object
```py
x = 10
print(id(x))   # (some unique number, varies)
```
9) help() → shows documentation

```py
help(len)   # shows info about len() function

```
10) input() → takes user input

```py
name = input("Enter your name: ")
print("Hello", name)

```

len() → length

type() → data type

sum() → add numbers

max(), min() → biggest/smallest

abs() → absolute value

round() → round numbers

sorted() → sort list

id() → memory address

help() → documentation

input() → user input