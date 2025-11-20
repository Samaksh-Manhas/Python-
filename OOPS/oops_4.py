#Write a program to display a application
#create a class with name Library_Management_Sysytem
#create Function with name Books()
#this function display list of available books
#on execution of this application pass default username(user1) and pin(123)
#create a validate() functions accept username and pin from user.
#if user enter valid details show list of books otherwise display
#invalid information entered


class Library_Management_System:

    def Books(self):
        print("\nAvailable Books:")
        print("1. Python Programming")
        print("2. Database Management Systems")

    def validate(self, username, pin):
        default_username = "user1"
        default_pin = 123

        if username == default_username and pin == default_pin:
            print("\nLogin Successful!")
            self.Books()
        else:
            print("\nInvalid information entered")


obj = Library_Management_System()
user = input("Enter Username: ")
pin = int(input("Enter PIN: "))
obj.validate(user, pin)
