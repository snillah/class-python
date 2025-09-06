# The last two categories of Python operators: Membership and Identity operators.

1. Membership Operators

Used to check if a value exists inside a sequence (like string, list, tuple, set, dictionary).
They return True or False.

| Operator | Meaning                      | Example            | Result |
| -------- | ---------------------------- | ------------------ | ------ |
| `in`     | True if value is present     | `"a" in "apple"`   | True   |
| `not in` | True if value is NOT present | `5 not in [1,2,3]` | True   |

```py

fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)      # True
print("grape" not in fruits)  # True

text = "hello world"
print("world" in text)        # True


```

2. Identity Operators

Used to compare memory location of two objects (not just values).
They check whether two variables point to the same object in memory.

| Operator | Meaning                                 | Example      |
| -------- | --------------------------------------- | ------------ |
| `is`     | True if both refer to same object       | `a is b`     |
| `is not` | True if both refer to different objects | `a is not b` |

```py
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x == y)    # True  (values are same)
print(x is y)    # False (different memory locations)
print(x is z)    # True  (same object in memory)
print(x is not y)  # True

```

| Operator Type | Operators      | Example          | Result                     |
| ------------- | -------------- | ---------------- | -------------------------- |
| Membership    | `in`, `not in` | `"a" in "apple"` | True                       |
| Identity      | `is`, `is not` | `x is y`         | Depends on memory location |
