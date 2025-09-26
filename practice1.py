s=int(input("Enter the start value: "))
e=int(input("Enter the end value: "))

for i in range(s,e+1):
    if i%5==0:
        print(f"Table of {i}:")
        for j in range(1,11):
            print(f"{i}*{j}={i*j}")
        print("\n")
else:
    print("This program will help to understand f or format function used with print function")