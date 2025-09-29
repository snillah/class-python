# 1)Introduction to Errors & Exceptions

In Python, errors can happen when the code is running.

## Two main types:

### Syntax Errors → mistakes in code structure.

```py

print("Hello"   # ❌ Missing bracket → SyntaxError

```
### Exceptions → errors that occur during execution.

```py
x = 10 / 0   # ❌ ZeroDivisionError

```

Without handling, exceptions `stop the program`.



# 2)Using try and except

try: the block of code to test.

except: the block that runs if an error happens.

```py
try:
    num = int("abc")   # ❌ ValueError
    print(num)
except ValueError:
    print("Oops! That is not a valid number.")

# o/p
Oops! That is not a valid number.

```
# 3) Handling Multiple Exceptions

```py
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Invalid value entered")

# o/p

You cannot divide by zero!

```

# 4) Catching Any Exception

```py

try:
    a = int("hello")
except Exception as e:
    print("Error:", e)

# o/p
Error: invalid literal for int() with base 10: 'hello'

```
# 5) Using finally

```py
try:
    f = open("test.txt", "r")
    content = f.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution finished (closing resources).")

# Output

File not found.
Execution finished (closing resources).

```


## Summary

Errors stop the program unless handled.

try → test code.

except → handle errors.

finally → always runs (cleanup).