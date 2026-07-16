import csv

expenses = []
try:
    with open ("expenses.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            expense={"amount": float(row[0]), "category": row[1], "description": row[2]}
            expenses.append(expense)
            print("expenses loaded from expenses.csv")
except FileNotFoundError:
    print("No existing expense data found.")

while True:
    print("--- Expense Tracker ---")
    print("1. Add an Expense")
    print("2. View Expenses & Total")
    print("3. Save and Quit")
    choice = int(input("enter your choice 1, 2, 3:"))
    if (choice == 1):
        amt= float(input("Enter the amount:"))
        ct = input("Enter the category:")
        ds = input("Enter the Description:")
        expense = { "amount" : amt , "category" : ct , "description" : ds}
        expenses.append(expense)
        print("expense added succesfully")
    elif (choice == 2):
        total = 0
        for expense in expenses:
            total = total + expense["amount"]
            print(f"{expense['amount'] } ,{expense['category'] }, {expense['description']} ")
        print(f"Total spent={total}")
    else:
        with open("expenses.csv", "w", newline="") as file:
            file.write("Amount,Category,Description\n")
            for expense in expenses:
                file.write(f"{expense['amount']}, {expense['category']}, {expense['description']}\n")
            print("expenses saved to expenses.csv")
            break