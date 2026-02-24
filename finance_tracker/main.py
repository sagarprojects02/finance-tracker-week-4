from .expense_manager import ExpenseManager
from .reports import generate_monthly_report
from .file_handler import load_expenses, save_expenses

def start_app():
    manager = ExpenseManager()
    expenses = load_expenses()
    manager.set_expenses(expenses)

    while True:
        print("\n==== Personal Finance Tracker ====")
        print("1. Add Expense")
        print("2. View Report")
        print("3. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            date = input("Date (YYYY-MM-DD): ")
            amount = float(input("Amount: "))
            category = input("Category: ")
            description = input("Description: ")
            manager.add_expense(date, amount, category, description)

        elif choice == "2":
            generate_monthly_report(manager.get_expenses())

        elif choice == "3":
            save_expenses(manager.get_expenses())
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid choice!")
