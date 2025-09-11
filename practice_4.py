#Accept marks of 5 subjects and calculate total, percentage, and print pass or fail
eng=float(input("Enter the marks of English: "))
maths=float(input("Enter the marks of Maths: "))
sci=float(input("Enter the marks of Science: "))
hindi=float(input("Enter the marks of Hindi: "))
sst=float(input("Enter the marks of SST: "))
total=eng+maths+sci+hindi+sst
per=total/500*100 
print("Total:",round(total,2))
print("Percent:",round(per,2))
if per>=50:
    print("Pass")
else:
    print("Fail")
