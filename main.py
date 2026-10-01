print("Expense Tracker")

expenses = []
def menu():
    print("\nMenu:")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Exit")
choice = ""

while choice != "3":
    menu()
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        # Add Expense logic here
        amount = input("Enter amount: ")
        category = input("Enter category: ")
        description = input("Enter description: ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }
        expenses.append(expense)
        print("Expense added successfully!")


    elif choice == "2":
        # View Expense logic here
        if not expenses:
            print("No expense found.")
        else:
            print("\nExpenses:\n") 

            for expense in expenses:
                print("Amount:", expense["amount"])
                print("Category:", expense["category"])
                print("Description:", expense["description"])
                print()

    elif choice == "3":
        print("GoodBye!")

    else:
        print("Invalid choice. Please try again.")


    