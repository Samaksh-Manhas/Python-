#
basic=float(input("Enter basic salary: "))
hra=20/100*basic
da=10/100*basic
pf=12/100*basic
gross=basic+hra+da
net=gross-pf

print("Basic: ", basic)
print("HRA: ", hra)
print("DA: ", da)
print("PF: ", pf)
print("Gross: ", gross)
print("Net: ", net)

if net>=80000:
    print("Category: High Earner")
elif net>=50000:
    print("Category: Mid Earner")
else:
    print("Category: Low Earner")