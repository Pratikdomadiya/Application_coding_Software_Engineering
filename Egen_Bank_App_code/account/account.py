from Egen_Bank_App_code.Transaction.transaction import Transaction
class Account:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction(self.account_number, self.account_number, amount))

    def withdraw(self, amount):
        if amount >= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction(self.account_number, self.account_number, -amount))
        else:
            print("insufficient balance ")

    def get_transactions(self):
        return self.transactions

    def hold_money(self, amount):
        self.balance -= amount
        return Transaction(self.account_number, None, amount)

    def accept_transfer(self, transaction):
        if transaction.receiver == self.account_number and not transaction.accepted:
            self.balance += transaction.amount
            transaction.accepted = True
            self.transactions.append(transaction)

