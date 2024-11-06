

def add_expense(expenses, name, amount):
    expenses.append({'name': name, 'amount': amount})

def display_expenses(expenses):
    print("\n--- Expenses ---")
    total = 0
    for expense in expenses:
        print(f"{expense['name']}: ${expense['amount']:.2f}")
        total += expense['amount']
    print(f"Total Expenses: ${total:.2f}\n")
    return total

def split_expenses(total, num_people):
    return total / num_people if num_people > 0 else 0

# Initialize list to store expenses
expenses = []

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Split Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter expense description: ")
        amount = float(input("Enter amount: "))
        add_expense(expenses, name, amount)

    elif choice == '2':
        display_expenses(expenses)

    elif choice == '3':
        num_people = int(input("Enter the number of people: "))
        total = display_expenses(expenses)
        split_amount = split_expenses(total, num_people)
        print(f"Each person should contribute: ${split_amount:.2f}\n")

    elif choice == '4':
        print("Exiting the tracker.")
        break

    else:
        print("Invalid choice. Please try again.")
