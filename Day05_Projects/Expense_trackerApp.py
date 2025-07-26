# We are going to create an app that helps the user to add new expenses, view their expenses and calculate the amount spent

while True:
    print("\nWhat do you want to do? ")
    print("1. Add a new expense ")
    print("2. View all expenses ")
    print("3. View total spent ")
    print("4. Exit the app ")
    choice = input("Enter your choice between 1 and 4")
    if choice == "1":
        print("Add your expenses ")
        date = input("Enter the date of the expense: ")
        print(f"The date of the expense is,{date}")
        category = input("What is your expense category: ")
        print(f"Your category is, {category}")
        amount = input("How much did you spent..?")
        print(f"The amount you spent is, {amount}")
        with open("expenses.txt", "a") as file:
            file.write(f"{date}, {category}, {amount}\n")
            print(f"Expense saved, Keep tracking🤪!")
    elif choice == "2":
        print("View your expenses ")
        try:
            with open("expenses.txt", "r") as file:
                lines = file.readlines()
                if not lines:
                    print("Your expense file is empty! ")
                else:
                    for line in lines:
                        print(line.strip())
        except FileNotFoundError:
            print("No expenses found. The file does not exist yet.")
    elif choice == "3":
        print("Check your total amount you spent ")
        with open("expenses.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("Your expense to total is empty! ")
            else:
                total = 0
            for line in lines:
                parts = line.strip().split(",")
                total += float(parts[1].strip())
            print(f"The total amount spent is {total} You've tried this time!")

                    


