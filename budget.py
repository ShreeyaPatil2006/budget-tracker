class Expense:
    def __init__(self, Name, Cost):
        self.Name = Name
        self.Cost = Cost

    def display_info(self):
        print(f"{self.Name} - {self.Cost}")


class Budget:
    def __init__(self, income):
        self.income = income   
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def view_expenses(self):
        if len(self.expenses) == 0:
            print("No expenses added yet.")
        else:
            for exp in self.expenses:
                exp.display_info()

    def total_spent(self):
        total = 0
        for exp in self.expenses:
            total += exp.Cost
        print("Total spent:", total)

    def remaining_balance(self):
        total = 0
        for exp in self.expenses:
            total += exp.Cost
        print("Remaining balance:", self.income - total)


name = input("Enter your name: ")
income = int(input("Enter your income: "))

my_budget = Budget(income)

while True:
    print("\nMenu")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View total spent")
    print("4. View remaining balance")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter expense name: ")
        cost = int(input("Enter cost: "))
        exp = Expense(name, cost)
        my_budget.add_expense(exp)

    elif choice == 2:
        my_budget.view_expenses()

    elif choice == 3:
        my_budget.total_spent()

    elif choice == 4:
        my_budget.remaining_balance()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice")