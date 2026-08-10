"""
Expense Tracker
A simple command-line app to track daily expenses.

Concepts used:
Lists, Dictionaries, Functions, Loops,
List Comprehension, JSON, File Persistence
"""

import json
import os
from datetime import date


DATA_FILE = "expenses.json"


# ========================================
# FILE PERSISTENCE
# ========================================

def load_expenses():
    """Load expenses from the JSON file."""

    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        return []


def save_expenses(expenses):
    """Save expenses to the JSON file."""

    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


# ========================================
# CORE FUNCTIONALITY
# ========================================

def add_expense(expenses, amount, category, note=""):
    """Add a new expense."""

    # Generate a unique ID
    if expenses:
        new_id = max(expense["id"] for expense in expenses) + 1
    else:
        new_id = 1

    expense = {
        "id": new_id,
        "amount": amount,
        "category": category,
        "note": note,
        "date": str(date.today())
    }

    expenses.append(expense)

    save_expenses(expenses)

    print(f"\n✅ Expense added successfully!")
    print(f"   ID: {new_id}")
    print(f"   Amount: ${amount:.2f}")
    print(f"   Category: {category}")


def delete_expense(expenses, expense_id):
    """Delete an expense by its ID."""

    new_expenses = [
        expense
        for expense in expenses
        if expense["id"] != expense_id
    ]

    if len(new_expenses) == len(expenses):
        print(f"\n❌ No expense found with ID {expense_id}.")
        return expenses

    save_expenses(new_expenses)

    print(f"\n✅ Expense {expense_id} deleted successfully.")

    return new_expenses


def total_spent(expenses):
    """Calculate total spending."""

    return sum(expense["amount"] for expense in expenses)


def total_by_category(expenses):
    """Calculate total spending for each category."""

    categories = {}

    for expense in expenses:
        category = expense["category"]

        categories[category] = (
            categories.get(category, 0)
            + expense["amount"]
        )

    return categories


def filter_by_category(expenses, category):
    """Return expenses matching a category."""

    return [
        expense
        for expense in expenses
        if expense["category"].lower() == category.lower()
    ]


def list_expenses(expenses):
    """Display all expenses."""

    if not expenses:
        print("\n📭 No expenses recorded yet.")
        return

    print(
        f"\n{'ID':<5}"
        f"{'Date':<12}"
        f"{'Category':<15}"
        f"{'Amount':<12}"
        f"Note"
    )

    print("-" * 60)

    for expense in expenses:
        print(
            f"{expense['id']:<5}"
            f"{expense['date']:<12}"
            f"{expense['category']:<15}"
            f"${expense['amount']:<11.2f}"
            f"{expense['note']}"
        )

    print()


# ========================================
# MENU
# ========================================

def print_menu():

    print("""
========================================
          💰 EXPENSE TRACKER
========================================

1. Add expense
2. View all expenses
3. View total spent
4. View totals by category
5. Filter by category
6. Delete an expense
7. Exit

========================================
""")


# ========================================
# MAIN PROGRAM
# ========================================

def main():

    expenses = load_expenses()

    while True:

        print_menu()

        choice = input("Choose an option (1-7): ").strip()

        # --------------------------------
        # ADD EXPENSE
        # --------------------------------

        if choice == "1":

            try:
                amount = float(input("Amount: $"))

                if amount <= 0:
                    print("❌ Amount must be greater than 0.")
                    continue

                category = input(
                    "Category (food, transport, school...): "
                ).strip()

                if not category:
                    print("❌ Category cannot be empty.")
                    continue

                note = input(
                    "Note (optional): "
                ).strip()

                add_expense(
                    expenses,
                    amount,
                    category,
                    note
                )

            except ValueError:
                print("❌ Please enter a valid number.")

        # --------------------------------
        # VIEW EXPENSES
        # --------------------------------

        elif choice == "2":

            list_expenses(expenses)

        # --------------------------------
        # TOTAL SPENDING
        # --------------------------------

        elif choice == "3":

            total = total_spent(expenses)

            print(f"\n💰 Total spent: ${total:.2f}")

        # --------------------------------
        # TOTAL BY CATEGORY
        # --------------------------------

        elif choice == "4":

            totals = total_by_category(expenses)

            if not totals:
                print("\n📭 No expenses yet.")

            else:
                print("\n📊 Spending by category:")
                print("-" * 30)

                for category, amount in totals.items():
                    print(f"{category:<15} ${amount:.2f}")

        # --------------------------------
        # FILTER BY CATEGORY
        # --------------------------------

        elif choice == "5":

            category = input(
                "Enter category to search: "
            ).strip()

            results = filter_by_category(
                expenses,
                category
            )

            if not results:
                print(
                    f"\n❌ No expenses found "
                    f"for '{category}'."
                )
            else:
                list_expenses(results)

        # --------------------------------
        # DELETE EXPENSE
        # --------------------------------

        elif choice == "6":

            try:
                expense_id = int(
                    input("Enter expense ID to delete: ")
                )

                expenses = delete_expense(
                    expenses,
                    expense_id
                )

            except ValueError:
                print("❌ Please enter a valid ID number.")

        # --------------------------------
        # EXIT
        # --------------------------------

        elif choice == "7":

            print("\n👋 Goodbye!")
            break

        # --------------------------------
        # INVALID OPTION
        # --------------------------------

        else:

            print(
                "\n❌ Invalid option. "
                "Please choose between 1 and 7."
            )


# ========================================
# START PROGRAM
# ========================================

if __name__ == "__main__":
    main()



