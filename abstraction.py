# Abstraction in PYthon
from abc import ABC, abstractmethod

class wallets(ABC):
    
    @abstractmethod
    def pay(self):
        print("Test")

class Paypal(wallets):
    def pay(self):
        print("Paypal payment")
    
    def displayInfo():
        wallets.pay()
        
obj = wallets
wallets.pay()

