class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        elif amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance

    def reset_account(self):
        self.balance = 0