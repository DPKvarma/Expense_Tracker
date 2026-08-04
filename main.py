import sqlite3
from datetime import datetime

# ---------------- DATABASE ----------------

connection = sqlite3.connect("expenses.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    date TEXT NOT NULL
)
""")

connection.commit()


# ---------------- ADD EXPENSE ----------------

def add_expense():
    title = input("Enter expense title: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount!")
        return

    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")

    if date == "":
        date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
    INSERT INTO expenses (title, amount, category, date)
    VALUES (?, ?, ?, ?)
    """, (title, amount, category, date))

    connection.commit()

    print("Expense added successfully!")


# ---------------- VIEW EXPENSES ----------------

def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    if not expenses:
        print("No expenses found.")
        return

    print("\nID | Title | Amount | Category | Date")
    print("-" * 50)

    for expense in expenses:
        print(
            f"{expense[0]} | "
            f"{expense[1]} | "
            f"₹{expense[2]:.2f} | "
            f"{expense[3]} | "
            f"{expense[4]}"
        )


# ---------------- SEARCH EXPENSE ----------------

def search_expense():
    category = input("Enter category to search: ")

    cursor.execute("""
    SELECT * FROM expenses
    WHERE category LIKE ?
    """, ('%' + category + '%',))

    expenses = cursor.fetchall()

    if not expenses:
        print("No expenses found.")
        return

    print("\nSearch Results")
    print("-" * 50)

    for expense in expenses:
        print(
            f"ID: {expense[0]} | "
            f"{expense[1]} | "
            f"₹{expense[2]:.2f} | "
            f"{expense[3]} | "
            f"{expense[4]}"
        )


# ---------------- UPDATE EXPENSE ----------------

def update_expense():
    try:
        expense_id = int(input("Enter expense ID to update: "))
    except ValueError:
        print("Invalid ID!")
        return

    cursor.execute(
        "SELECT * FROM expenses WHERE id = ?",
        (expense_id,)
    )

    expense = cursor.fetchone()

    if not expense:
        print("Expense not found.")
        return

    title = input("Enter new title: ")

    try:
        amount = float(input("Enter new amount: "))
    except ValueError:
        print("Invalid amount!")
        return

    category = input("Enter new category: ")
    date = input("Enter new date (YYYY-MM-DD): ")

    cursor.execute("""
    UPDATE expenses
    SET title = ?, amount = ?, category = ?, date = ?
    WHERE id = ?
    """, (title, amount, category, date, expense_id))

    connection.commit()

    print("Expense updated successfully!")


# ---------------- DELETE EXPENSE ----------------

def delete_expense():
    try:
        expense_id = int(input("Enter expense ID to delete: "))
    except ValueError:
        print("Invalid ID!")
        return

    cursor.execute(
        "SELECT * FROM expenses WHERE id = ?",
        (expense_id,)
    )

    expense = cursor.fetchone()

    if not expense:
        print("Expense not found.")
        return

    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    connection.commit()

    print("Expense deleted successfully!")


# ---------------- TOTAL EXPENSE ----------------

def total_expense():
    cursor.execute("SELECT SUM(amount) FROM expenses")

    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    print(f"\nTotal Expenses: ₹{total:.2f}")


# ---------------- CATEGORY SUMMARY ----------------

def category_summary():
    cursor.execute("""
    SELECT category, SUM(amount)
    FROM expenses
    GROUP BY category
    """)

    results = cursor.fetchall()

    if not results:
        print("No expenses found.")
        return

    print("\n===== CATEGORY SUMMARY =====")

    for category, amount in results:
        print(f"{category}: ₹{amount:.2f}")


# ---------------- MAIN MENU ----------------

def main():

    while True:

        print("\n==============================")
        print("       EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Update Expense")
        print("5. Delete Expense")
        print("6. Total Expenses")
        print("7. Category Summary")
        print("8. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_expense()

        elif choice == "4":
            update_expense()

        elif choice == "5":
            delete_expense()

        elif choice == "6":
            total_expense()

        elif choice == "7":
            category_summary()

        elif choice == "8":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


# ---------------- RUN PROGRAM ----------------

if __name__ == "__main__":
    main()

connection.close()