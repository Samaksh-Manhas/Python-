#Accept characters from user and print them in capital or small
ch=input("Enter a character:")
n=int(input("""1. Capital
2. Small
Enter your choice: """))

if n==1:
    print(ch.upper())
elif n==2:
    print(ch.lower())
else:
    print("Enter a Valid choice")