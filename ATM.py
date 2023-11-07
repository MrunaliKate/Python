class ATM:
    def __init__(self, balance=0):
        self.balance = balance

        def check_balance(self):
            print(f"Your current balance is ${self.balance:.2f}")

        def deposit(self, amount):
            if amount > 0:
                self.balance += amount
                print(f"${amount:.2f} has been deposited.")
                self.check_balance()
            else:
                print("Invalid amount. Deposit amount must be positive.")     