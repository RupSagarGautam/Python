# Abstraction in PYthon
from abc import ABC, abstractmethod

class Wallets(ABC):
    
    @abstractmethod
    def pay(self,amount):
        pass


class Paypal(Wallets):
    def pay(self,amount):
        print("Paypal payment")
    
class Khalti(Wallets):
    def pay(self,amount):
        print(f"Khalti payment of {amount}")

def payment(wallet: Wallets, amount):
    wallet.pay(amount)
    
wallet = input("Enter Wallet Name: ")
amount = float(input("Enter amount to be paid: "))


if wallet.lower() == "paypal":
    payment(Paypal(), amount)
elif wallet.lower() == "khalti":
    payment(Khalti(), amount)
else:
    print("\nInvalid Wallet Name")

