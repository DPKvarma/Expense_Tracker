# 💰 Expense Tracker

A simple **command-line Expense Tracker** built using **Python and SQLite**. This project allows users to record, manage, search, and analyze their daily expenses through a terminal-based interface.

## 📌 Project Overview

The Expense Tracker helps users keep track of their spending by storing expense details such as **title, amount, category, and date**.

The application uses **SQLite** to permanently store expense data, so the information remains available even after closing the program.

## 🚀 Features

* ➕ Add new expenses
* 📋 View all expenses
* 🔍 Search expenses by category
* ✏️ Update existing expenses
* 🗑️ Delete expenses
* 💰 Calculate total expenses
* 📊 View category-wise expense summary
* 💾 Store data using SQLite database
* 🖥️ Simple command-line interface

## 🛠️ Technologies Used

* **Python 3**
* **SQLite**
* **SQL**
* **Python `sqlite3` module**

## 📂 Project Structure

```text
expense-tracker-python/
│
├── main.py
├── README.md
└── .gitignore
```

> The `expenses.db` database file is automatically created when the program runs.

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/expense-tracker-python.git
```

### 2. Navigate to the project folder

```bash
cd expense-tracker-python
```

### 3. Run the application

```bash
python main.py
```

> No external Python packages are required because SQLite support is included with Python.

## 🖥️ Application Menu

```text
==============================
       EXPENSE TRACKER
==============================
1. Add Expense
2. View Expenses
3. Search Expense
4. Update Expense
5. Delete Expense
6. Total Expenses
7. Category Summary
8. Exit
==============================
```

## 🗃️ Database Structure

The application creates an SQLite database named:

```text
expenses.db
```

It contains an `expenses` table with the following fields:

| Field      | Description                        |
| ---------- | ---------------------------------- |
| `id`       | Unique expense ID                  |
| `title`    | Name or description of the expense |
| `amount`   | Amount spent                       |
| `category` | Expense category                   |
| `date`     | Date of the expense                |

### Example Data

| ID | Title      | Amount | Category  | Date       |
| -: | ---------- | -----: | --------- | ---------- |
|  1 | Lunch      |   ₹150 | Food      | 2026-08-04 |
|  2 | Bus Ticket |    ₹50 | Travel    | 2026-08-04 |
|  3 | Notebook   |    ₹80 | Education | 2026-08-03 |

## 🔄 CRUD Operations

This project demonstrates basic **CRUD operations**:

* **Create** → Add an expense
* **Read** → View and search expenses
* **Update** → Modify an expense
* **Delete** → Remove an expense

## 🎯 Learning Outcomes

Through this project, I practiced:

* Python functions
* Conditional statements and loops
* Exception handling
* SQLite database integration
* SQL queries
* CRUD operations
* User input handling
* Data storage and retrieval
* Basic project structure

## 🔮 Future Improvements

* Add a graphical user interface
* Add monthly expense reports
* Add income and balance tracking
* Add date-based filtering
* Add data visualization
* Add user authentication
* Convert the project into a REST API using Flask or FastAPI

## 👨‍💻 Author

**D. Pavan Kumar Varma**

B.Tech – Electronics and Communication Engineering

---

⭐ If you find this project useful, consider giving the repository a star!
