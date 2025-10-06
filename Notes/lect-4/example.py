# def number_type(n):
n =10
match n:
    case x if x > 0:
        print("Positive")
    case x if x < 0:
        print("Negative")
    case 0:
        print("Zero")

# print(number_type(10))
# print(number_type(-5))
# print(number_type(0))

for item in "fruits":
    print("value : ",item)