
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