class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"{amount} withdrawn successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Withdraw amount must be positive.")

    def check_balance(self):
        print(f"Current balance: {self.balance}")


# Taking input from the user
name = input("Enter your name: ")
initial_balance = float(input("Enter initial balance: "))

# Create account
account = BankAccount(name, initial_balance)

while True:
    print("\nChoose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == '3':
        account.check_balance()
    elif choice == '4':
        print("Thank you for using the bank system. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")