import json
from datetime import datetime

# Function to load transactions from a file
def load_transactions():
    try:
        with open("transactions.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"income": 0, "expenses": []}

# Function to save transactions to a file
def save_transactions(transactions):
    with open("transactions.json", "w") as file:
        json.dump(transactions, file)

# Function to enter income
def enter_income(transactions):
    income_amount = float(input("Enter income amount: "))
    transactions["income"] += income_amount
    print(f"Income of ${income_amount} added successfully.")
    save_transactions(transactions)

# Function to enter an expense
def enter_expense(transactions):
    category = input("Enter expense category: ")
    expense_amount = float(input("Enter expense amount: "))
    transactions["expenses"].append({"category": category, "amount": expense_amount, "date": str(datetime.now())})
    transactions["income"] -= expense_amount
    print(f"Expense of ${expense_amount} in {category} added successfully.")
    save_transactions(transactions)

# Function to calculate remaining budget
def calculate_budget(transactions):
    return transactions["income"]

# Function to analyze expenses
def analyze_expenses(transactions):
    expense_categories = {}
    for expense in transactions["expenses"]:
        category = expense["category"]
        amount = expense["amount"]
        if category in expense_categories:
            expense_categories[category] += amount
        else:
            expense_categories[category] = amount

    print("\nExpense Analysis:")
    for category, amount in expense_categories.items():
        print(f"{category}: ${amount}")

# Main function
def main():
    transactions = load_transactions()

    while True:
        print("\n1. Enter Income")
        print("2. Enter Expense")
        print("3. Calculate Remaining Budget")
        print("4. Expense Analysis")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            enter_income(transactions)
        elif choice == "2":
            enter_expense(transactions)
        elif choice == "3":
            remaining_budget = calculate_budget(transactions)
            print(f"\nRemaining Budget: ${remaining_budget}")
        elif choice == "4":
            analyze_expenses(transactions)
        elif choice == "5":
            print("Exiting Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
