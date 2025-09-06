# Operators: arithmetic, comparison, logical, assignment

1. Arithmetic Operators - Used for mathematical calculations.

| Operator | Meaning             | Example (`a = 10, b = 3`) | Result   |
| -------- | ------------------- | ------------------------- | -------- |
| `+`      | Addition            | `a + b`                   | 13       |
| `-`      | Subtraction         | `a - b`                   | 7        |
| `*`      | Multiplication      | `a * b`                   | 30       |
| `/`      | Division (float)    | `a / b`                   | 3.333... |
| `//`     | Floor Division      | `a // b`                  | 3        |
| `%`      | Modulus (remainder) | `a % b`                   | 1        |
| `**`     | Exponent (power)    | `a ** b`                  | 1000     |

```py

a, b = 10, 3
print(a + b)   # 13
print(a // b)  # 3
print(a ** b)  # 1000

```
2. Comparison (Relational) Operators - Used to compare values, result is True or False.

| Operator | Meaning          | Example (`a=10, b=3`) | Result |
| -------- | ---------------- | --------------------- | ------ |
| `==`     | Equal to         | `a == b`              | False  |
| `!=`     | Not equal to     | `a != b`              | True   |
| `>`      | Greater than     | `a > b`               | True   |
| `<`      | Less than        | `a < b`               | False  |
| `>=`     | Greater or equal | `a >= b`              | True   |
| `<=`     | Less or equal    | `a <= b`              | False  |

```py
print(10 > 3)   # True
print(5 == 5)   # True
print(7 != 2)   # True
```
3. Logical Operators - Used to combine conditions.

| Operator | Meaning                          | Example                | Result |
| -------- | -------------------------------- | ---------------------- | ------ |
| `and`    | True if **both** are True        | `(10 > 5) and (8 > 6)` | True   |
| `or`     | True if **at least one** is True | `(10 < 5) or (8 > 6)`  | True   |
| `not`    | Negates the condition            | `not(10 > 5)`          | False  |

```py
x, y = True, False
print(x and y)   # False
print(x or y)    # True
print(not x)     # False

```
4. Assignment Operators - Used to assign values to variables (sometimes with operations).

| Operator | Meaning            | Example (`a = 5`) | Result |
| -------- | ------------------ | ----------------- | ------ |
| `=`      | Assign             | `a = 5`           | 5      |
| `+=`     | Add & assign       | `a += 3` (a=5)    | 8      |
| `-=`     | Subtract & assign  | `a -= 2` (a=8)    | 6      |
| `*=`     | Multiply & assign  | `a *= 4` (a=6)    | 24     |
| `/=`     | Divide & assign    | `a /= 2` (a=24)   | 12.0   |
| `//=`    | Floor div & assign | `a //= 5` (a=12)  | 2      |
| `%=`     | Modulus & assign   | `a %= 2` (a=2)    | 0      |
| `**=`    | Power & assign     | `a **= 3` (a=2)   | 8      |

```py

a = 10
a += 5   # a = a + 5 → 15
a *= 2   # a = a * 2 → 30
print(a)

```
# Summary

Arithmetic → + - * / % // **

Comparison → == != > < >= <=

Logical → and or not

Assignment → =, +=, -=, *=, /=, //=, %=, **=

# Bitwise Operators

& → AND

| → OR

^ → XOR

~ → NOT

<< → Left shift

>> → Right shift

| Operator    | Symbol | Meaning                                     | Example (`a = 6, b = 3`)          | Binary Work          | Result |        |               |   |
| ----------- | ------ | ------------------------------------------- | --------------------------------- | -------------------- | ------ | ------ | ------------- | - |
| AND         | `&`    | Sets bit to 1 if **both bits** are 1        | `a & b`                           | `0110 & 0011 = 0010` | 2      |        |               |   |
| OR          | \`     | \`                                          | Sets bit to 1 if **any bit** is 1 | \`a                  | b\`    | \`0110 | 0011 = 0111\` | 7 |
| XOR         | `^`    | Sets bit to 1 if **bits are different**     | `a ^ b`                           | `0110 ^ 0011 = 0101` | 5      |        |               |   |
| NOT         | `~`    | Inverts all bits (2’s complement in Python) | `~a`                              | `~0110 = ...1001`    | -7     |        |               |   |
| Left Shift  | `<<`   | Shifts bits left (adds zeros on right)      | `a << 1`                          | `0110 << 1 = 1100`   | 12     |        |               |   |
| Right Shift | `>>`   | Shifts bits right (drops rightmost bits)    | `a >> 1`                          | `0110 >> 1 = 0011`   | 3      |        |               |   |

## Quick Explanation with Binary

Let’s break a = 6 (0110) and b = 3 (0011)

AND (&) → 0110 & 0011 = 0010 → 2

OR (|) → 0110 | 0011 = 0111 → 7

XOR (^) → 0110 ^ 0011 = 0101 → 5

NOT (~a) → flips 0110 → ...1001 (2’s complement) = -7

Left Shift (<<) → 0110 << 1 = 1100 → 12

Right Shift (>>) → 0110 >> 1 = 0011 → 3

