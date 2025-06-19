# Calculator using OOP
# Author: [Rup Sagar Gautam]
# Date: 2025-Jun-19
class Calculator:
    
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def __call__(self,operation):
        num1 = self.num1
        num2 = self.num2
        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Division by zero is not allowed"
        else:
            return "Invalid operation"
        
a= int(input("Enter Num 1: "))
b= int(input("Enter Num 2: "))

calc = Calculator(a,b)
