# Functiom with no arguments and no return value
def displayHelloWorld():
    print("Hello, World!")
for i in range(10):
    displayHelloWorld()
# function with no arguments and return value

def add():
    num1=10
    num2=20
    sum = num1+num2
    return sum
print(add())

# function with arguments and no return values
def displayName(name):
    print("Hello, "+name + "!")
displayName("John")

# Function with arguments and return values
def displayData(num1, num2):
    pro = num1 * num2
    return pro
print(displayData(50, 20))


