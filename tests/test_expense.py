from finance_tracker.expense import Expense

def test_expense_creation():
    exp = Expense("2026-02-20", 100, "Food", "Lunch")
    assert exp.amount == 100
