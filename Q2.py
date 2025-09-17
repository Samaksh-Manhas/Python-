#Accept choice from user and print result
n=int(input("""1. Print Hi
2. Print Welcome
3. Print Bye
Enter your choice: """))

if n==1:
    print("Hi")
elif n==2:
    print("Welcome")
elif n==3:
    print("Bye")
else:
    print("Enter a valid choice.")