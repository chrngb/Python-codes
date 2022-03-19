# Bill split program

while True:
    try:
        bill = float(input("Enter the initial bill amount: $"))
        if bill < 0 or bill == 0:
            print("The bill amount cannot be negative or zero. Please enter again.")
        else:
            break
    except:
        print("You entered invalid bill amount. Please enter again.")

while True:
    try:
        tip = int(input("Enter the tip percent: "))
        choice = [10, 12, 15]
        if tip not in choice:
            print("The tip can only be 10%, 12% or 15%. Please enter again.")
        else:
            break
    except:
        print("Invalid input. Please enter again.")

while True:
    people = input("How many people are there: ")
    if people.isdigit() == False or people == 0:
        print("Please enter valid number of people to split the bill.")
    else:
        break

total_bill = bill * (1 + tip/100)

split_bill = round(total_bill/int(people), 2)

print(f"From {people} people each should pay ${split_bill}")
