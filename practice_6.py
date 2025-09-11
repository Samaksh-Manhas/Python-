a=int(input("Enter a number: "))
if a>=0:
    if a%2==0:
        print(a,"is a positive even number")
    else:
        print(a,"is a positive odd number")
if a<0:
    if a%2==0:
        print(a,"is a negitive even number")
    else:
        print(a,"is a negitive odd number")