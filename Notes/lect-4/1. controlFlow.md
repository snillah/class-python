# Control Flow (Decision Making in Python) step by step.

1) if Statement

 Used when you want to execute code only if a condition is true.

```py
age = 20

if age >= 18:
    print("You are an adult")

#o/p
You are an adult

```
2) if-else Statement
Adds an alternative block when the condition is false.

```py
age = 15

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

```

3) if-elif-else (Multiple Conditions)
Used when you need to check more than two conditions

```py
marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")

#o/p
Grade: B

```

4) Nested Conditions
An if inside another if.

```py
age = 25
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
    else:
        print("Not a citizen")
else:
    print("Not eligible to vote")

# o/p
Eligible to vote

```

5) Short-hand if
When you have a single statement, you can write it in one line.

```py
x = 10
if x > 5: print("x is greater than 5")

#o/p 
x is greater than 5
```

6) Short-hand if-else (Ternary Operator)

```py
x = 5
result = "Even" if x % 2 == 0  else "Odd"
print(result)

#op
Odd

```

| Statement            | Use                                          |
| -------------------- | -------------------------------------------- |
| `if`                 | Executes a block if condition is true        |
| `if-else`            | Executes one block if true, another if false |
| `if-elif-else`       | Multiple conditions                          |
| Nested `if`          | One condition inside another                 |
| Short-hand `if`      | One-line if                                  |
| Short-hand `if-else` | One-line conditional expression              |
