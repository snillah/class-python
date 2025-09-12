# What are Boolean Values?

Boolean values represent truth values:

`True`

`False`

They are written with an uppercase first letter (T and F).

Type is `bool`.

## Truthy & Falsy Values in Python

In Python, many values behave like True or False in conditions.

### Falsy values (considered False):

    0, 0.0, 0j (numbers = zero)

    "" (empty string)

    [], (), {}, set(), frozenset() (empty containers)

    None

    False

### Everything else is Truthy (considered True).

####  For Comparisons Operations
Comparison operators return boolean values.
```py
print(5 > 2)   # True
print(10 == 3) # False
print(7 <= 7)  # True
```

####  For Logical Operations 
Logical operators (and, or, not) work with booleans.

```py
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False

```


####  For Conditional
Booleans are mostly used in if/else and loops.

```py
age = 18
if age >= 18:
    print(True)   # condition is True
else:
    print(False)
```

### important :
After if age >= 18: → the : means: “If this condition is true, run the indented block below.”

After else: → the : means: “If the above condition is false, run the indented block below.”

In other languages (like C, Java), we use { } braces to mark a block.
In Python, we use colon : + indentation instead.

## report:

Boolean values: True, False (type bool).

Used in conditions, loops, comparisons, logical operations.

Python treats non-empty/ non-zero as True, and empty/zero as False.
