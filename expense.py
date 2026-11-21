expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    reason = input("Enter reason: ")

    expenses.append({
        "amount": amount,
        "reason": reason
    })

    print("Expense added successfully!")

def view_expenses():
    for expense in expenses:
        print(expense["reason"], expense["amount"])

def total_expense():
    total = sum(item["amount"] for item in expenses)
    print("Total Expense:", total)

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        break
    else:
        print("Invalid choice")