
income = 0
expenses = []

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. View Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter income amount: "))
        income += amount
        print("Income added successfully!")

    elif choice == "2":
        amount = float(input("Enter expense amount: "))
        expenses.append(amount)
        print("Expense added successfully!")

    elif choice == "3":
        print("\nTotal Income:", income)
        print("Expenses:")

        if len(expenses) == 0:
            print("No expenses added.")
        else:
            for expense in expenses:
                print(expense)

    elif choice == "4":
        total_expense = sum(expenses)
        balance = income - total_expense

        print("Total Income:", income)
        print("Total Expense:", total_expense)
        print("Remaining Balance:", balance)

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Try again.")
