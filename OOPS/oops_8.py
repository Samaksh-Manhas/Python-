class check:
    def accept(self):
        self.num=int(input("Enter a number: "))
        
    def verify(self):
        if self.num%2==0:
            print(f"{self.num} is even")
        else:
            print(f"{self.num} is odd")
    
    def validate(self):
        if self.num >= 0:
            print(f"{self.num} is positive")
            self.verify()
        else:
            print(f"{self.num} is negative")

obj=check()
obj.accept()
obj.validate()
