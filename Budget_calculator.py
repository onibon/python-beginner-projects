print("Personal Budget calculator")
income = float(input("How much money do you have this month? ₦ "))
food = float(input("How much money do you spend on food? ₦ "))
rent = float(input("How much do you spend on rent? ₦ "))
transport = float(input("How much do you spend on transport? ₦ "))
subscription = float(input("How much do you spend on subscription monthly? ₦ "))
shopping = float(input("How much do you spend on shopping? ₦ "))

total_expenses = rent + food + transport + subscription + shopping
balance = income - total_expenses

print("\n--- Budget Summary ---")
print(f"Total Expenses: ₦{total_expenses}")
print(f"Money left: ₦{balance}")



