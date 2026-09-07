print(" ============Income and Expense Tracker=========== ")
UserName = input("Enter your name: ")
monthlySalary = int(input("Enter your monthly salary: "))
monthlyRent = int(input("Enter your monthly rent: "))
ExpensesOnFood = int(input("Enter your expenses on food: "))
SavingsAmount = int(input("Enter your savings amount: "))

Available_Amount_After_Rent = (monthlySalary - monthlyRent)
print("Available amount after rent: ", Available_Amount_After_Rent)

Available_amount_after_Rent_and_Food = (monthlySalary- monthlyRent - ExpensesOnFood)
print("Available amount after rent and food: ", Available_amount_after_Rent_and_Food)

Availabe_Amount_After_SavingsAmount = (monthlySalary - monthlyRent - ExpensesOnFood - SavingsAmount)
print("Available amount after Savings: ", Availabe_Amount_After_SavingsAmount)

print(" =========== MONTHLY SAVINGS REPORT =========== ")

print(f"hi... {UserName} !")
print(f"Your Monthly Salary is: ", monthlySalary)
print(f"Your Monthly Rent is: ", monthlyRent)
print(f"Your Expenses on Food is: ", ExpensesOnFood)
print(f"Your Savings Amount is: ", SavingsAmount)
print(f"Available amount after rent is: ", Available_Amount_After_Rent)
print(f"Available amount after rent and food is: ", Available_amount_after_Rent_and_Food)
print(f"Available amount after Savings is: ", Availabe_Amount_After_SavingsAmount)

print(UserName + " wants to save the amount of " + str(SavingsAmount) + " this month" )

print(" =========== MONTHLY SAVINGS REPORT =========== ")

