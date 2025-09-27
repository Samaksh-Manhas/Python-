n=int(input("Enter the number of rows: "))
i=n
while i>=1:
    j=0
    while j<i:
        print(1+j, end=" ")
        j+=1
    i-=1
    print()