from .expense import Expense

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, date, amount, category, description):
        expense = Expense(date, amount, category, description)
        self.expenses.append(expense)

    def get_expenses(self):
        return self.expenses

    def set_expenses(self, expense_list):
        self.expenses = expense_list
