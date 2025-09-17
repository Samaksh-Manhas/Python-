#Movie ticket booking
a=int(input("""Choose the type of seat
1. Claasic ($100)
2. Premium ($300)
3. Recliner ($500)
Enter your choice: """))

b=int(input("Enter the number of seats: "))

if a==1:
    total=b*100
    if total>=500 and total<=1500:
        choice=int(input("""Choose your choice
1. $200 worth meal
2. 2% discount
Enter your choice: """))
        if choice==1:
            print("Total:", total, "with $200 meal")
        elif choice==2:
            dis=2/100*total
            final=total-dis  
            print("Original anount:",total, "\nDiscount:",dis, "\nFinal amount:",final)
        else:
            print("Enter a valid choice")
    elif total>1500:
        choice=int(input("""Choose your choice
1. $500 worth meal
2. 4% discount
Enter your choice: """))
        if choice==1:
            print("Total:", total, "with $500 meal")
        elif choice==2:
            dis=4/100*total
            final=total-dis  
            print("Original anount:",total, "\nDiscount:",dis, "\nFinal amount:",final)
        else:
            print("Enter a valid choice")
    else:
        print("Total:",total)

if a==2:
    total=b*300
    if total>=500 and total<=1500:
        choice=int(input("""Choose your choice
1. $200 worth meal
2. 2% discount
Enter your choice: """))
        if choice==1:
            print("Total:", total, "with $200 meal")
        elif choice==2:
            dis=2/100*total
            final=total-dis  
            print("Original anount:",total, "\nDiscount:",dis, "\nFinal amount:",final)
        else:
            print("Enter a valid choice")
    elif total>1500:
        choice=int(input("""Choose your choice
1. $500 worth meal
2. 4% discount
Enter your choice: """))
        if choice==1:
            print("Total:", total, "with $500 meal")
        elif choice==2:
            dis=4/100*total
            final=total-dis  
            print("Original anount:",total, "\nDiscount:",dis, "\nFinal amount:",final)
        else:
            print("Enter a valid choice")
    else:
        print("Total:",total)

if a==3:
    total=b*500
    if total>=500 and total<=1500:
        choice=int(input("""Choose your choice
1. $200 worth meal
2. 2% discount
Enter your choice: """))
        if choice==1:
            print("Total:", total, "with $200 meal")
        elif choice==2:
            dis=2/100*total
            final=total-dis  
            print("Original anount:",total, "\nDiscount:",dis, "\nFinal amount:",final)
        else:
            print("Enter a valid choice")
    elif total>1500:
        choice=int(input("""Choose your choice
1. $500 worth meal
2. 4% discount
Enter your choice: """))
        if choice==1:
            print("Total:", total, "with $500 meal")
        elif choice==2:
            dis=4/100*total
            final=total-dis  
            print("Original anount:",total, "\nDiscount:",dis, "\nFinal amount:",final)
        else:
            print("Enter a valid choice")
    else:
        print("Total:", total)
        