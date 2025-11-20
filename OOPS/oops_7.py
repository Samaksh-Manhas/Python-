class Student_Management_System:
    def accept(self):
        self.name=input("Enter student's name: ")
        self.roll=int(input("Enter student's roll number: "))
        self.stream=input("Enter student's stream: ")
    def display(self):
        print(f"Name: {self.name} \nRoll Number: {self.roll} \nStream: {self.stream}")
    
    
obj1=Student_Management_System()
obj2=Student_Management_System()
obj3=Student_Management_System()
obj4=Student_Management_System()
obj5=Student_Management_System()

obj1.accept()
obj1.display()

obj2.accept()
obj2.display()

obj3.accept()
obj3.display()

obj4.accept()
obj4.display()

obj5.accept()
obj5.display()