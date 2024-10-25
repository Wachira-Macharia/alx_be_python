# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deduct the specified amount if funds are sufficient. Returns True if successful, False otherwise."""
        if amount > 0:
            if self._account_balance >= amount:
                self._account_balance -= amount
                return True
            else:
                return False
        else:
            print("Withdraw amount must be positive.")
            return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self._account_balance:.2f}")
