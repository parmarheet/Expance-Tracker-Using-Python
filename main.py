import os
import json
import matplotlib.pyplot as plt

class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return {}

    def save_expenses(self):
        with open(self.filename, "w") as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount
        self.save_expenses()

    def view_expenses(self):
        print("\nYour Expenses:")
        for category, amount in self.expenses.items():
            print(f"{category}: Rs. {amount}")

    def visualize_expenses(self):
        categories = list(self.expenses.keys())
        amounts = list(self.expenses.values())

        if not categories:
            print("No expenses to visualize.")
            return

        # Pie Chart
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.pie(amounts, labels=categories, autopct="%1.1f%%", startangle=140)
        plt.title("Expense Distribution")

        # Bar Chart
        plt.subplot(1, 2, 2)
        plt.bar(categories, amounts, color="skyblue")
        plt.title("Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount (Rs.)")
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Visualize Expenses")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter category (e.g., Food, Travel): ").strip()
            try:
                amount = float(input("Enter amount (Rs.): "))
                tracker.add_expense(category, amount)
                print("Expense added successfully!")
            except ValueError:
                print("Invalid amount. Please try again.")
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.visualize_expenses()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()