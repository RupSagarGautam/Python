class A:
    def displayClassNameA():
        print("Hello World!")
        
# Inheritance in Python

class B(A):
    def displayClassNameB():
        print("I am in class B")

class C(B):
    def displayClassNameC():
        print("I am in Class C")
        
# obj = A
# obj.displayClassNameA()
# obj2 = B
# obj2.displayClassNameB()

obj3 = C
obj3.displayClassNameA() #displays function in class A
obj3.displayClassNameB() #displays function in class B
obj3.displayClassNameC() #displays function in class C

