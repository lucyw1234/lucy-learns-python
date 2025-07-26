# Personal Budget Calculator
# This program helps users calculate their monthly budget based on income and expenses.

# Get user input for monthly income
name = input("Enter your name: ") # string data type
income = float(input("Enter your monthly income: "))  # float data type

# Get users expenses
rent = float(input("Enter your monthly rent: "))  # float data type
food = float(input("Enter your monthly food expenses: "))  # float data type
transport = float(input("Enter your monthly transport expenses: "))  # float data type

# Calculate total expenses and savings
total_expenses = rent + food + transport  # float data type
savings = income - total_expenses  # float data type

# Display a summary of the budget
print("\n----Budget Summary----")
print("Name:", name)
print("Total income:", income)
print("Total expenses:", total_expenses)
print("Savings:", savings)
