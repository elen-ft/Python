class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Current balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate / 100
        self.balance += interest_amount

    def __str__(self):
        return f"Current balance: ${self.balance}, Interest rate: {self.interest_rate}%"

bank_account = BankAccount("123789", "John Doe")
bank_account.deposit(1000)
bank_account.withdraw(500)

savings_account = SavingsAccount("983211", "Jane Smith", 2.5)
savings_account.deposit(2000)
savings_account.apply_interest()
print(savings_account)
