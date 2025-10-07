# What is Encapsulation?

 Encapsulation means binding data (variables) and methods (functions) together into a single unit — a class.
 It helps to protect the internal state of an object from being changed directly from outside.

 Think of a capsule 💊 — it hides the medicine inside, but gives you only the safe outer shell to interact

# Why Do We Use Encapsulation?

 To protect sensitive data (like passwords, account balance).
 To prevent accidental modification.
 To control how data is accessed or updated (through methods only).
 To make code secure and maintainable.


# Encapsulation → hiding details, exposing only necessary parts.

```py
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private (name-mangling)
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance

```
## Examples :
### Basic 
```py
class BankAccount:
    def __init__(self, balance):
        self.balance = balance  # public variable

account = BankAccount(1000)
print(account.balance)   # Anyone can access
account.balance = -500   # ❌ Wrong, unsafe
print(account.balance)

``` 
### Encapsulation
```py
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    # public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    # public method to get balance
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())   # 1500

# print(account.__balance)     # ❌ Error: Attribute not accessible
```

## Access Modifiers in Python

Python doesn’t have strict private/public keywords (like Java or C++).
Instead, it uses naming conventions:

| Type      | Syntax       | Access Level                                 | Example       |
| --------- | ------------ | -------------------------------------------- | ------------- |
| Public    | `variable`   | Accessible anywhere                          | `self.name`   |
| Protected | `_variable`  | Accessible within class + subclasses         | `self._name`  |
| Private   | `__variable` | Accessible only inside class (name mangling) | `self.__name` |


## 4. Name Mangling (how Python hides private variables)
Even though __balance is private, Python internally changes its name:

```py
print(account._BankAccount__balance)   # 1500

#You can access it like this, but you shouldn’t — it breaks encapsulation.
```
### Real world example : students

```py
class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks
    
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks!")
    
    def get_marks(self):
        return self.__marks

s1 = Student("Alice", 85)
print(s1.get_marks())     # 85
s1.set_marks(95)          # valid update
print(s1.get_marks())     # 95
s1.set_marks(150)         # invalid

```

## Report
| Concept                | Meaning                                                       |
| ---------------------- | ------------------------------------------------------------- |
| **Encapsulation**      | Hiding internal data and allowing access only through methods |
| **Private Variable**   | `__variable` — cannot be accessed directly                    |
| **Protected Variable** | `_variable` — used within subclasses                          |
| **Public Variable**    | accessible anywhere                                           |
| **Goal**               | Secure, maintainable, controlled access to data               |
