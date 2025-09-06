# Python Built-in Data Types

## Numeric Types

        int     → whole numbers (positive, negative, zero).
        float   → decimal numbers
        complex → numbers with real and imaginary part
```py
        z = 2 + 3j
print(type(z))   # <class 'complex'>
print(z.real, z.imag)  # 2.0  3.0
```

## Sequence Types
    
### List
list → ordered, mutable (can change), allows duplicates
```py
fruits = ["apple", "banana", "cherry"]
print(type(fruits))   # <class 'list'>

```
### Tuple

tuple → ordered, immutable (cannot change), allows duplicates

```py
colors = ("red", "green", "blue")
print(type(colors))   # <class 'tuple'>

```

### Range
range → sequence of numbers (often used in loops)

```py
r = range(5)
print(list(r))   # [0, 1, 2, 3, 4]

```
## Set Types

### Set

set → unordered, unique values only

```py
s = {1, 2, 3, 3}
print(s)        # {1, 2, 3}
print(type(s))  # <class 'set'>

```

### Frozenset 

frozenset → same as set but immutable

```py
fs = frozenset({1, 2, 3})
print(type(fs))   # <class 'frozenset'>

```

## Mapping Type

### Dict

dict (dictionary) → key-value pairs, unordered

```py
student = {"name": "John", "age": 20}
print(student["name"])   # John
print(type(student))     # <class 'dict'>

```

## Boolean Type
bool → logical values True or False

```py
a = True
b = False
print(type(a))   # <class 'bool'>

```
## Binary Types

### bytes

bytes → immutable sequence of bytes

```py
b = bytes([65, 66, 67])
print(b)        # b'ABC'
print(type(b))  # <class 'bytes'>

```

### bytearray

bytearray → mutable sequence of bytes

```py
ba = bytearray([65, 66, 67])
ba[0] = 68
print(ba)       # bytearray(b'DBC')
print(type(ba)) # <class 'bytearray'>

```
### memoryview
memoryview → provides a view (access) to memory of another object (like bytes/bytearray) without copying data

```py
mv = memoryview(b"Hello")
print(mv[0])    # 72 (ASCII of 'H')
print(type(mv)) # <class 'memoryview'>

```
## None Type

NoneType → represents “nothing” or “no value”

```py
x = None
print(x)         # None
print(type(x))   # <class 'NoneType'>

```

| Category     | Type                         | Example                                          |
| ------------ | ---------------------------- | ------------------------------------------------ |
| Numeric      | int, float, complex          | `10`, `3.14`, `2+3j`                             |
| Sequence     | list, tuple, range           | `[1,2,3]`, `(1,2,3)`, `range(5)`                 |
| Set Types    | set, frozenset               | `{1,2,3}`, `frozenset({1,2})`                    |
| Mapping      | dict                         | `{"key": "value"}`                               |
| Boolean      | bool                         | `True`, `False`                                  |
| Binary       | bytes, bytearray, memoryview | `b'ABC'`, `bytearray([65])`, `memoryview(b'Hi')` |
| Special Type | NoneType                     | `None`                                           |
