Operator Precedence Table (Highest → Lowest)
| Precedence | Operator                 | Description                                       | Associativity |              |
| ---------- | ------------------------ | ------------------------------------------------- | ------------- | ------------ |
| 1          | `()`                     | Parentheses (grouping)                            | Left → Right  |              |
| 2          | `**`                     | Exponentiation                                    | Right → Left  |              |
| 3          | `+x, -x, ~x`             | Unary plus, Unary minus, Bitwise NOT              | Right → Left  |              |
| 4          | `*`, `/`, `//`, `%`      | Multiplication, Division, Floor division, Modulus | Left → Right  |              |
| 5          | `+`, `-`                 | Addition, Subtraction                             | Left → Right  |              |
| 6          | `<<`, `>>`               | Bitwise shift operators                           | Left → Right  |              |
| 7          | `&`                      | Bitwise AND                                       | Left → Right  |              |
| 8          | `^`                      | Bitwise XOR                                       | Left → Right  |              |
| 9          | \`                       | \`                                                | Bitwise OR    | Left → Right |
| 10         | `<, <=, >, >=`           | Comparison operators                              | Left → Right  |              |
| 11         | `==, !=`                 | Equality operators                                | Left → Right  |              |
| 12         | `is, is not, in, not in` | Identity / Membership operators                   | Left → Right  |              |
| 13         | `not`                    | Logical NOT                                       | Right → Left  |              |
| 14         | `and`                    | Logical AND                                       | Left → Right  |              |
| 15         | `or`                     | Logical OR                                        | Left → Right  |              |
| 16         | `=`, `+=`, `-=`, etc.    | Assignment operators                              | Right → Left  |              |

Examples
1) Multiplication before Addition
print(2 + 3 * 4)


Output:

14


Because * has higher precedence than +.

2) Use of Parentheses
print((2 + 3) * 4)


Output:

20


Parentheses change the natural precedence.

3) Exponentiation is Right-to-Left
print(2 ** 3 ** 2)   # 2 ** (3 ** 2)

print(2 ** 2 ** 2)   # 2 ** (2 ** 2)
Output:

512
16

4) Logical Operators

print(True or False and False)  # and first, then or


Output:

True

Report : 
Always use parentheses () for clarity when expressions are complex.

Remember: ** (power) is evaluated right-to-left; most others are left-to-right.
