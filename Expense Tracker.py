import csv
import os

expenses = []

def add_expense():
    date = input("Input Date (YYYY-MM-DD): ")
    category = input("Category: ")
    while True:
        try:
            amount = float(input("Enter Amount: "))
            if amount<=0:
                print("Enter amount greater that 0")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number for the amount.")

    description = input("Enter a brief description of expense: ") 
    expense = {
        'date':date,
        'category':category,
        'amount':amount,
        'description':description
    }
    expenses.append(expense)
    print("Expense added successfully")


def display_expense():
    if not expenses:
        print("No expenses logged yet.")
        return
    
    for expense in expenses:
        if all(key in expense for key in ['date', 'category', 'amount', 'description']):
            print(f"Date: {expense['date']} | Category: {expense['category']} | Amount: {expense['amount']} | Description: {expense['description']}")
        else:
            print(f"Incomplete entry: {expense}")


def track_budget():
    global monthly_budget
    while True:
        try:
            monthly_budget = float(input("Enter your monthly budget: "))
            if monthly_budget <= 0:
                print("Budget must be greater than 0. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number for the budget.")
    
    total_expenses = sum(expense['amount'] for expense in expenses)
    if total_expenses > monthly_budget:
        print(f"You have exceeded your budget by {total_expenses - monthly_budget:.2f}!")
    else:
        remaining_balance = monthly_budget - total_expenses
        print(f"You have {remaining_balance:.2f} remaining for the month.")


def save_expenses():
    filename = 'expenses.csv'
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)
    print(f"Expenses saved to {filename}")


def load_expenses():
    global expenses
    filename = 'expenses.csv'
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            expenses = [row for row in reader]
        print(f"Expenses loaded from {filename}")
    else:
        print("No saved expenses file found.")


def display_menu():
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Track Budget")
        print("4. Save Expenses")
        print("5. Exit")
        
        try:
            choice = int(input("Enter the number of your choice: "))
            
            if choice == 1:
                add_expense()
            elif choice == 2:
                display_expense()
            elif choice == 3:
                track_budget()
            elif choice == 4:
                save_expenses()
            elif choice == 5:
                save_expenses()  
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


display_menu()
load_expenses()

