# 1.What is a List?

A list in Python is:

A collection that can hold multiple items.

Ordered (items keep their position).

Mutable (you can change items).

Can hold different data types in one list

```py

my_list = [10, "hello", 3.14, True]
print(my_list)

#o/p

[10, 'hello', 3.14, True]

```
# 2.Creating Lists

```py
# Empty list
empty = []

# List with numbers
numbers = [1, 2, 3, 4, 5]

# List with strings
fruits = ["apple", "banana", "cherry"]

# Mixed data types
mixed = [1, "hello", 3.5, False]

# Using list() constructor
letters = list("Python")  
print(letters)   # ['P', 'y', 't', 'h', 'o', 'n']

```

# 3.Indexing

Access elements using index (position).

Index starts at 0.

Negative index counts from end.

```py
fruits = ["apple", "banana", "cherry"]

print(fruits[0])   # apple
print(fruits[2])   # cherry
print(fruits[-1])  # cherry (last element)
print(fruits[-2])  # banana

```

# 4. Slicing
Extract a part (sub-list).
```py
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])   # [20, 30, 40] (from index 1 to 3)
print(numbers[:3])    # [10, 20, 30] (from start to index 2)
print(numbers[3:])    # [40, 50, 60] (from index 3 to end)
print(numbers[::2])   # [10, 30, 50] (step = 2)
print(numbers[::-1])  # [60, 50, 40, 30, 20, 10] (reversed)

```

| Method             | Example                      | Result                         |
| ------------------ | ---------------------------- | ------------------------------ |
| `append(x)`        | `fruits.append("mango")`     | Add at end                     |
| `insert(i, x)`     | `fruits.insert(1, "orange")` | Insert at index                |
| `remove(x)`        | `fruits.remove("banana")`    | Remove first match             |
| `pop(i)`           | `fruits.pop(2)`              | Remove by index                |
| `clear()`          | `fruits.clear()`             | Empty list                     |
| `index(x)`         | `fruits.index("apple")`      | Get position                   |
| `count(x)`         | `nums.count(2)`              | Count occurrences              |
| `sort()`           | `nums.sort()`                | Sort ascending                 |
| `reverse()`        | `nums.reverse()`             | Reverse list                   |
| `copy()`           | `new_list = nums.copy()`     | Copy list                      |
| `extend(iterable)` | `list1.extend(list2)`        | Add elements from another list |

# Example with Methods

```py
fruits = ["apple", "banana", "cherry"]

fruits.append("mango")       # ['apple', 'banana', 'cherry', 'mango']
fruits.insert(1, "orange")   # ['apple', 'orange', 'banana', 'cherry', 'mango']
fruits.remove("banana")      # ['apple', 'orange', 'cherry', 'mango']
fruits.pop()                 # removes 'mango'
fruits.sort()                # ['apple', 'cherry', 'orange']
fruits.reverse()             # ['orange', 'cherry', 'apple']

print(fruits)

#o/p
['orange', 'cherry', 'apple']

```

List = ordered, mutable collection.

Use indexing for single item, slicing for sub-list.

Many useful methods: append, insert, remove, sort, etc.