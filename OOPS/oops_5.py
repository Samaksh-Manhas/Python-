class calculator:
    def sum(self, a, b):
        print(f"Sum of {a} + {b}: {a+b}")
    
    def sub(self, a, b):
        print(f"Sub of {a} - {b}: {a-b}")
        
    def mult(self, a, b):
        print(f"Mult of {a} * {b}: {a*b}")
        
    def div(self, a, b):
        print(f"Div of {a} / {b}: {a/b}")
    

a=int(input("Enter a number: "))
b=int(input("Enter another number: "))

obj=calculator()
obj.sum(a, b)
obj.sub(a, b)
obj.mult(a, b)
obj.div(a, b)
