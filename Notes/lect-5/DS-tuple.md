1) What is a Tuple?

A tuple is similar to a list, but:

Ordered (keeps items in sequence).

Immutable (cannot be changed after creation).

Can hold different data types.

```py
my_tuple = (10, "hello", 3.14, True)
print(my_tuple)

# o/p
(10, 'hello', 3.14, True)

```

2) Creating Tuples

```py
# Normal tuple
numbers = (1, 2, 3, 4, 5)

# Mixed data
mixed = (1, "python", 3.5, False)

# Single-element tuple (comma is required!)
single = (5,)
print(type(single))   # <class 'tuple'>

# Without parentheses (tuple packing)
tuple1 = 10, 20, 30
print(tuple1)         # (10, 20, 30)

# Using tuple() constructor
letters = tuple("ABC")
print(letters)        # ('A', 'B', 'C')

```

3) Indexing and Slicing

```py
fruits = ("apple", "banana", "cherry", "mango")

print(fruits[0])    # apple
print(fruits[-1])   # mango
print(fruits[1:3])  # ('banana', 'cherry')
print(fruits[::-1]) # ('mango', 'cherry', 'banana', 'apple')

```

4) Immutability (Cannot be Changed)

Tuples cannot be modified after creation.

```py
colors = ("red", "green", "blue")

# colors[0] = "yellow"   ❌ Error: 'tuple' object does not support item assignment

```

### important

```py
`But you can convert tuple → list, modify, then back to tuple:`  

colors = ("red", "green", "blue")
temp = list(colors)        # Convert to list
temp[0] = "yellow"         # Modify
colors = tuple(temp)       # Convert back
print(colors)              # ('yellow', 'green', 'blue')

```

5) Common Tuple Methods
| Method     | Example                | Result |
| ---------- | ---------------------- | ------ |
| `count(x)` | `(1,2,2,3).count(2)`   | 2      |
| `index(x)` | `(10,20,30).index(20)` | 1      |
| `len(t)`   | `len((1,2,3))`         | 3      |

6) Tuple Unpacking
Assign tuple values to variables.

```py
point = (4, 5)

x, y = point
print("x =", x)   # 4
print("y =", y)   # 5

```
`Swap variables easily`:
```py
a, b = 10, 20
a, b = b, a
print(a, b)   # 20 10

```
Tuples = immutable lists (cannot change).

Ordered, can store multiple & mixed data types.

Useful when data should not be changed.

Supports indexing, slicing, unpacking.