class BankAccount:

    # initialize account with pin and history

    def __init__(self, name, pin, balance=0):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.history = []

    # deposit money

    def deposit(self, amount):
        if (amount>=0):
            self.balance += amount
            self.history.append(f"Deposited ${amount:.2f}")
            print(f"${amount:.2f} deposited! New balance: ${self.balance:.2f}")
        else:
            print("The amount you are typing must be greater than 0!")    

    # withdraw money

    def withdraw(self, amount):
        if (amount <= self.balance):
            self.balance -= amount
            self.history.append(f"Withdrew ${amount:.2f}")
            print(f"${amount:.2f} withdrawn! New balance: ${self.balance:.2f}")
        else:
            print("This amount can't be withdrawn! Insufficient balance")
    
    # show balance

    def show_balance(self):
        print(f"Account Holder: {self.name}, Balance: ${self.balance:.2f}")

    # show transaction history

    def show_history(self):
        print("\n--- Trasaction History ---")
        for h in self.history:
            print(h) if self.history else print("No transactions yet!")

#--- Main program---

name = input("Enter your name: ")
pin = input("Enter a 4 digit PIN: ")

account = BankAccount(name, pin)

# ask for PIN before access

if input("Enter PIN to login: ") != account.pin:
    print("Wrong PIN! Access denied.")
    exit()

while True:
    print("\n1.Deposit 2. Withdraw 3.Show Balance 4.Show History 5.Exit")
    choice = input("Choose: ")
    if choice == "1":
        account.deposit(float(input("Enter amount: ")))
    elif choice == "2":
        account.withdraw(float(input("Enter amount: ")))
    elif choice == "3":
        account.show_balance()
    elif choice == "4":
        account.show_history()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")