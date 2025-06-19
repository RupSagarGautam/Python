class A:
    def displayName():
        print("This is Class A")
    
    def displayHello():
        print("Hello from Class A")
    
class B(A):
    def displayName():
        print("This is Class B")
        
class C(B):
    def displayName():
        print("This is Class C")
    
    def sum(num1,num2=0,num3=0):
        return num1 + num2 + num3
        
    # Using args
    def add(*args):
        sum = 0
        for num in args:
            sum += num
        return sum
    
obj = A
# obj.displayName()

obj1 = B
# obj1.displayName()

obj2 = C
# obj2.displayName()
# obj2.displayHello()        

result = obj2.sum(10)
print(result)  # Output: 10
result1 = obj2.sum(10,20,30)
print(result1)  # Output: 60

# Using args
result2 = obj2.add(10,20,30,50,40)
print(result2)  # Output: 150

