#Loan eligibility
age= int(input("Enter your age: "))
monthly_income=float(input("Enter your monthly income: "))
existing_loan=float(input("Enter your Existing loan: "))
cibil_score=int(input("Enter your CIBIL Score: "))

if 21>=age<=60:
    print("Rejected due to age not between 21-60")

elif monthly_income < 25000:
    print("Rejected due to low monthly income")
elif existing_loan > (0.5 * monthly_income):
    print("Rejected due to high existing loan")
elif cibil_score<700:
    print("Rejected due to low CIBIL score")
else:
    print("Eligible for loan")