#Accept price of 10 diff items and calculate total (if total>2000 provide discount 20%)
total=0
for i in range(1,11):
    a=int(input(f"Enter the price of Item {i}: "))
    total+=a
if total>2000:
    discount=total*20/100
    new_amount=total-discount
    print("Original Amount:",total)
    print("Dicount:",discount)
    print("Fianl amount:",new_amount)
else:
    print("Fianl Amount:",total)