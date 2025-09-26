s=int(input("Enter the start value: "))
e=int(input("Enter the end value: "))

while s <= e:
    if s%5==0:
        print(f"Table of {s}:")
        j=1
        while j <=10:
            print(f"{s}*{j}={s*j}")
            j+=1
        print("\n")
    s+=1
else:
    print("This program will help to understand f or format function used with print function")