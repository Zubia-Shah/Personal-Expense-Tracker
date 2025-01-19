class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount
        print(f"Added {amount} to {category}.")

    def show_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
        else:
            print("\nExpense Report:")
            total = 0
            for category, amount in self.expenses.items():
                print(f"{category}: {amount}")
                total += amount
            print(f"\nTotal Expenses: {total}")
    
    def reset_expenses(self):
        self.expenses.clear()
        print("All expenses have been reset.")

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Reset Expenses")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            category = input("Enter expense category: ")
            try:
                amount = float(input("Enter expense amount: "))
                tracker.add_expense(category, amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        
        elif choice == '2':
            tracker.show_expenses()
        
        elif choice == '3':
            tracker.reset_expenses()
        
        elif choice == '4':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
