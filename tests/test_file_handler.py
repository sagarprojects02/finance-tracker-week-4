from finance_tracker.file_handler import save_expenses, load_expenses
from finance_tracker.expense import Expense

def test_save_and_load():
    exp = Expense("2026-02-20", 200, "Bills", "Electricity")
    save_expenses([exp])
    expenses = load_expenses()
    assert len(expenses) >= 1
