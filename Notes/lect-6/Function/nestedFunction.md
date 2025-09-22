
# Function inside another function (nested)

```py
def outer():
    print("This is outer function")

    def inner():
        print("This is inner function")

    inner()

outer()

```