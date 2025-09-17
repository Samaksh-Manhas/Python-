#Accept input from user and print result
n=input("""S for Sunday
M for Monday
T for Tuesday
W for Wednesday
Th for Thursday
F for Friday
Sa for Saturday
Enter your choice:""")

n=n.upper()

if n=="S":
    print("Sunday")
elif n=="M":
    print("Monday")
elif n=="T":
    print("Tuesday")
elif n=="W":
    print("Wednesday")
elif n=="TH":
    print("Thursday")
elif n=="F":
    print("Friday")
elif n=="SA":
    print("Saturday")
else:
    print("Enter a valid choice")