import json

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
print("Expense Tracker")

expenses = load_expenses()
def menu():
    print("\nMenu:")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. View Total Expenses")
    print("4. Delete Expense")
    print("5. Edit Expense")
    print("6. Exit")
choice = ""

while choice != "6":
    menu()
    choice = input("Enter your choice (1-6): ")
# Add expense logic here...

    if choice == "1":
        amount = input("Enter amount: ")
        category = input("Enter category: ")
        description = input("Enter description: ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }
        expenses.append(expense)
        save_expenses()
        print("Expense added successfully!")

# Add expense viewing logic here...

    elif choice == "2":
        if not expenses:
            print("No expense found.")
        else:
            print("\nExpenses:\n") 

            for expense in expenses:
                print("Amount:", expense["amount"])
                print("Category:", expense["category"])
                print("Description:", expense["description"])
                print()
# Add total expenses calculation logic here...

    elif choice == "3":
        total = 0
        for expense in expenses:
            total = total + float(expense["amount"])
            print("Total Expenses:", total)
    elif choice == "4":
        if len(expenses) == 0:
            print("No expense to delete")
        else:
            print("Expenses:")
            for i in range(len(expenses)):
                print(i + 1, expenses[i]["description"])
            number = int(input("Enter expense number to be delete: "))

            if number >= 1 and number <= len(expenses):
                expenses.pop(number - 1)
                save_expenses()
            
                print("Expense deleted succcessfully!")
            else:
                print("Invalid expense number:")
    elif choice == "5":
        if len(expenses) == 0:
            print("No expenses to edit.")
        else:
            print("Expenses:")

            for i in range(len(expenses)):
                print(i + 1, expenses[i]["description"])
            number = int(input("Enter expense number to edit: "))
            if number >= 1 and number <= len(expenses):
                amount = input("Enter new amount: ")
                category = input("Enter new category: ")
                description = input("Enter new description: ")
                expenses[number - 1]["amount"] = amount
                expenses[number - 1]["category"] = category
                expenses[number - 1]["description"] = description
                save_expenses()
                print("Expense updated successfully!")
    elif choice == "6":
        print("GoodBye!")

    else:
        print("Invalid choice. Please try again.")


    