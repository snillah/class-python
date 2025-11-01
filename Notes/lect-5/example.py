def add(a,b):
    print(a+b)


def add(a,b):
    print(a*b)

add(15+5,20)
add(15+5,20)

def outer():
    print("This is outer function")

    def inner():
        print("This is inner function")

    inner()

outer()
