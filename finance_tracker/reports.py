from collections import defaultdict

def generate_monthly_report(expenses):
    if not expenses:
        print("No expenses found.")
        return

    total = sum(exp.amount for exp in expenses)
    category_totals = defaultdict(float)

    for exp in expenses:
        category_totals[exp.category] += exp.amount

    print("\n==== Monthly Report ====")
    print(f"Total Spending: {total}")

    for category, amount in category_totals.items():
        print(f"{category}: {amount}")
