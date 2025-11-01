# Sets in Python

A set is:

An unordered collection of items.

Stores unique elements only (no duplicates).

Mutable (you can add/remove items).

Doesn’t allow indexing/slicing (because unordered).

## Creating a Set

```py
my_set = {1, 2, 3, 4, 4, 5}
print(my_set)   # {1, 2, 3, 4, 5} (duplicate removed)

empty_set = set()   # Correct way ({} creates dict, not set)

```
## Common Operations

### Adding & Removing

```py
s = {1, 2, 3}
s.add(4)            # {1, 2, 3, 4}
s.remove(2)         # {1, 3, 4}
s.discard(10)       # No error if element not found

```
### Union & Intersection

```py
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)        # {1, 2, 3, 4, 5}   (union)
print(a & b)        # {3}               (intersection)
print(a - b)        # {1, 2}            (difference) - Means: take all elements that are in "a" but not in "b".
print(a ^ b)        # {1, 2, 4, 5}      (symmetric difference) - Means: take all elements that are in a or b, but not in both.

```

### Membership

```py
print(2 in a)   # True
print(10 in a)  # False

```