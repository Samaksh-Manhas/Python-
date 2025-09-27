n=int(input("Enter the number of rows: "))
i=n
while i>=1:
    j=1
    while j<=i:
        print("*", end=" ")
        j+=1
    i-=1
    print()