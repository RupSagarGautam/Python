class ConstructorDemo:
    def __init__(self):
        print("This is a constructor")

class AddNumbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def sum(self):
        return self.a + self.b
    
    def __call__(self,a,b):
        return a + b
        

obj = ConstructorDemo()
add = AddNumbers(10,20)

print(add.sum())
print(add(20,30))