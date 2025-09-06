# What is Type Casting?

It means converting one data type into another.
Python provides built-in functions like int(), float(), and str() for type casting.

int(x) → converts to integer (drops decimals).

float(x) → converts to float (decimal).

str(x) → converts to string.

```py
age = "25"          # string
age_int = int(age)  # string → int
age_float = float(age)  # string → float

print(age_int + 5)      # 30
print(age_float + 0.5)  # 25.5

num = 100
print("My number is " + str(num))  # concatenation requires str

```