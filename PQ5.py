#University Admission System
phy=float(input("Enter marks of Physics: "))
chem=float(input("Enter marks of Chemistry: "))
maths=float(input("Enter marks of Maths"))

total=phy+chem+maths
avg=total/3

print(f"Total Marks: {total}")
print(f"Average Marks: {avg:.2f}")

if avg>=70 and phy>=60 and chem>=60 and maths>=60:
    print("Eligible for Admission.")

elif maths>=90:
    print("Eligible under Maths Special Quota")

else:
    print("Not Eligible")