What is a Nested Function?

A nested function is simply a function defined inside another function.

def outer_function():
    print("This is the outer function")

    def inner_function():
        print("This is the inner function")

    inner_function()   # calling inner function from outer

outer_function()


✅ Output:

This is the outer function
This is the inner function

🔎 Why Use Nested Functions? (Use Cases)
1. Helper Function (organizing code)

Sometimes you want a small helper function that is only used inside another function.

def greet_user(name):
    def format_name(n):
        return n.strip().title()   # nested helper function

    formatted = format_name(name)
    print("Hello,", formatted)

greet_user("   saravanan  ")


✅ Output:

Hello, Saravanan


👉 format_name() is not needed outside, so we hide it inside.

2. Encapsulation (keeping things private)

Nested functions are not accessible outside the parent function, so they can be used to hide logic.

def password_checker():
    secret = "python123"

    def get_password():
        return secret   # hidden inside outer function

    return get_password()

print(password_checker())  # works
# print(get_password())    # ❌ error (not accessible outside)

3. Closures (functions remembering values)

Nested functions can "remember" variables from their outer function. This is called a closure.

def multiplier(n):
    def inner(x):
        return x * n   # inner function remembers n
    return inner

times2 = multiplier(2)
times3 = multiplier(3)

print(times2(5))  # 10
print(times3(5))  # 15


👉 Useful in decorators, callbacks, and configurable functions.

4. Practical Example – Calculator
def calculator(a, b):
    def add(): return a + b
    def sub(): return a - b
    def mul(): return a * b
    def div(): return a / b if b != 0 else "Error: Division by zero"

    return add(), sub(), mul(), div()

print(calculator(10, 5))


✅ Output:

(15, 5, 50, 2.0)


⚡ Summary:

Nested functions = functions inside functions.

Use when:

You need helper functions (only used inside).

You want to hide private logic.

You want closures/decorators.

👉 Do you want me to also show how nested functions are used in real life with decorators (like logging, authentication, timing execution)? That’s the most powerful use case.