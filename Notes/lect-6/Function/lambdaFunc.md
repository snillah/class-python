# What is a Lambda Function?

A lambda function is a small, one-line function without a name.
Defined using the keyword `lambda`.

```py

lambda arguments: expression

```

It can take any number of arguments, but must have only one expression.

# Example: Normal function vs Lambda

## Normal Function
```py
def add(a, b):
    return a + b

print(add(5, 3))   # 8

```

## Lambda function (same logic in one line):

```py
add = lambda a, b: a + b
print(add(5, 3))   # 8

```

# Examples of Lambda Functions

1) Square of a number

```py
square = lambda x: x**2

print(square(5))   # 25
```

2) Multiply two numbers

```py

multiply = lambda a, b: a * b
print(multiply(4, 6))   # 24
```

3) Check even/odd

```py
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even(7))   # Odd
print(is_even(10))  # Even
```

# Lambda with map(), filter(), sorted()

1) map() – apply function to each element
```py
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)   # [1, 4, 9, 16]
```
2) filter() – filter based on condition
```py
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)   # [2, 4, 6]
```
3) sorted() – custom sorting
```py
words = ["banana", "apple", "cherry"]
sorted_list = sorted(words, key=lambda w: len(w))
print(sorted_list)   # ['apple', 'banana', 'cherry']
```

# When to Use Lambda?

✅ When you need a quick, short function just once.
✅ Mostly used with map, filter, reduce, sorted.
❌ Not for complex logic (use def instead).