import json
import os
from .expense import Expense

DATA_FILE = "data/expenses.json"

def save_expenses(expenses):
    data = [expense.to_dict() for expense in expenses]
    os.makedirs("data", exist_ok=True)

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return [Expense(**item) for item in data]
    except:
        return []
