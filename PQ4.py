#E-commerce discount calculator
price=float(input("Enter the price of the products: "))
user=input("Enter user type (Regular, Premium, VIP): ").lower()
payment=input("Enter the payment mode (Cash, online): ").lower()

discount=0

if user=="regular":
    if price < 500:
        discount+=0.05
    else:
        discount+=0.1
        
elif user=="premium":
    if price < 1000:
        discount+=0.15
    else:
        discount+=0.2

elif user=="vip":
    discount+=0.25

else:
    print("Enter a valid User Type!")

if payment=="online":
    discount+=0.05

discount_price=price-(price*discount)

print("Discounted price: ", discount_price)