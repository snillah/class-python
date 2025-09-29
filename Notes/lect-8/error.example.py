
try:
    num = int("abc")   # ❌ ValueError
    print(num)
except ValueError:
    print("Oops! That is not a valid number.",ValueError)

# ----------------------------

try:
    x = 14 /int('A')
    num = int(x) 
    print(num)
except ZeroDivisionError:
    print("You cannot divide by zero!",ZeroDivisionError)
except ValueError:
    print("Invalid value entered")


try:
    f =open("test.txt", "r")
    content = f.read()
    print(content)
    f.close()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution finished (closing resources).")
