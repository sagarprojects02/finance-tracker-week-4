from finance_tracker.expense import Expense
from finance_tracker.reports import generate_monthly_report

def test_report():
    expenses = [
        Expense("2026-02-20", 100, "Food", "Lunch"),
        Expense("2026-02-21", 200, "Transport", "Bus")
    ]
    generate_monthly_report(expenses)
