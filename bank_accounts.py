class BankAccount:

    # constructor
    def __init__(self, account_number, bank_balance):
        self.account_number = account_number
        self.bank_balance = bank_balance

    # deposit method
    def deposit(self, amount):
        self.bank_balance = self.bank_balance + amount
        print("Amount deposited:", amount)

    # withdraw method
    def withdraw(self, amount):
        if amount <= self.bank_balance:
            self.bank_balance = self.bank_balance - amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    # check balance method
    def check_balance(self):
        print("Account Number:", self.account_number)
        print("Current Balance:", self.bank_balance)


# creating object
acc1 = BankAccount(12345, 5000)

acc1.deposit(1000)
acc1.withdraw(2000)
acc1.check_balance()