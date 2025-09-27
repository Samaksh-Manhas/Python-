n=int(input("Enter the number of rows: "))
i=1
while i<=n:
    j=0
    while j<i:
        print(chr(65+j), end=" ")
        j+=1
    i+=1
    print()