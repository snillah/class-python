from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Using a lambda function for addition
sum_result = reduce(lambda x, y: x + y, numbers)
print(f"Sum: {sum_result}") # Output: Sum: 15

# Using a defined function for multiplication
def multiply(x, y):
    return x * y

product_result = reduce(multiply, numbers)
print(f"Product: {product_result}") # Output: Product: 120