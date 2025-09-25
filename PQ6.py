#Movie Ticket Pricing System
age=int(input("Enter your Age: "))
movie_type=input("Enter movie type (2D/3D): ").lower()
day=input("Weekday/Weekend: ").lower()

base_price=200

if movie_type=="3d":
    base_price+=100

if day=="weekend":
    base_price+=50

if age < 12:
    discount=0.5*base_price
    base_price-=discount
if age > 60:
    discount=0.3*base_price
    base_price-=discount

print(f"Final Ticket Price: {base_price}")