class BankAccount:
    def __init__(self, balance=0, pin=""):
        self.balance = balance
        self.pin = pin

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful. Current balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

    def set_pin(self, pin):
        self.pin = pin

    def verify_pin(self, entered_pin):
        return entered_pin == self.pin


class ATM:
    def __init__(self):
        self.checking_account = BankAccount()
        self.savings_account = BankAccount()

    def transfer(self, amount):
        if amount <= self.checking_account.get_balance():
            self.checking_account.withdraw(amount)
            self.savings_account.deposit(amount)
            print("Transfer successful.")
        else:
            print("Transfer failed. Insufficient funds in Checking Account.")

    def display_menu(self):
        print("\nATM Menu:")
        print("1. Make deposit")
        print("2. Make withdrawal")
        print("3. Get account balance")
        print("4. Transfer between accounts")
        print("5. Exit")

    def authenticate_user(self):
        pin_attempts = 0
        while pin_attempts < 3:
            entered_pin = input("Enter PIN: ")
            if self.checking_account.verify_pin(entered_pin):
                return True
            else:
                pin_attempts += 1
                print(f"Incorrect PIN. Attempts left: {3 - pin_attempts}")

        print("Account locked. Please contact administrator.")
        return False

    def run(self):
        if not self.authenticate_user():
            return

        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                amount = float(input("Enter deposit amount: "))
                self.checking_account.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter withdrawal amount: "))
                self.checking_account.withdraw(amount)
            elif choice == '3':
                print(f"Checking Account Balance: {self.checking_account.get_balance()}")
            elif choice == '4':
                amount = float(input("Enter transfer amount: "))
                self.transfer(amount)
            elif choice == '5':
                print("Exiting ATM. Thank you!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


# Example usage
if __name__ == "__main__":
    # Set PIN for the checking account
    checking_pin = input("Set PIN for Checking Account: ")
    atm = ATM()
    atm.checking_account.set_pin(checking_pin)

    atm.run()
