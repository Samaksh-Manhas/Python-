vehicle_type=input("Enter type of vehicle (car/bike/truck): ").lower()
speed=float(input("Enter vehicle speed: "))
helmet="yes"
seat_belt="yes"
if vehicle_type=="bike":
    helmet=input("Wearing Helmet? (Yes/No): ").lower()
else:
    seat_belt=input("Wearing Seat belt? (Yes/No): ").lower()

total_fine=0

if speed > 80:
    total_fine+=2000

if vehicle_type=="car" and seat_belt=="no":
    total_fine+=1000
if vehicle_type=="bike" and helmet=="no":
    total_fine+=1500
if vehicle_type=="truck" and speed>60:
    total_fine+=3000
if total_fine>0:
    print(f"Total fine: Rs. {total_fine}")
else:
    print("No Fine, Drive safe.")