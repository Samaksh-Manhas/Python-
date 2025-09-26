balance=float(input("Enter the Account Balance: "))
withdraw=float(input("Enter the withrawl amount: "))
day=input("Enter the type of day (Weekday/Weekend): ").lower()
type=input("Enter the Account type (Saving/Current): ").lower()

extra=0
limit=0
min_balance=1000

if day=="weekend":
    extra=50

elif day=="weekday":
    extra=0

else:
    print("Enter a valid type of day!!!")
    exit()

total=withdraw+extra

if type=="saving":
    limit=25000
    
elif type=="current":
    limit=50000
    
else:
    print("Enter a valid Account type!!!")
    exit()

if withdraw>limit:
    print("Failure!!! Withdrawl Amount exceeds the Daily Account limit")
    
elif balance<total+min_balance:
    print("Failure!!! Insufficient Balance to maintain Minimum Balance")

else:
    print("Withdrawl Successful!")
    print("Updated Balance:", balance-total)