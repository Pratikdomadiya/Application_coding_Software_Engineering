from datetime import datetime
from Egen_Bank_App_code.account.account import Account
class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_number):
        if self.get_account(account_number) is None:
            self.accounts.append(Account(account_number))
            print(f"Account {account_number} created successfully.")
        else:
            print("Account number already exists.")

    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def rank_accounts(self, n):
        ranked_accounts = sorted(self.accounts, key=lambda account: sum(t.amount for t in account.transactions), reverse=True)
        return ranked_accounts[:n]

    def schedule_transfer(self, sender, receiver, amount):
        sender_account = self.get_account(sender)
        if sender_account:
            transaction = sender_account.hold_money(amount)
            print(f"Transfer scheduled: {sender} -> {receiver}, Amount: {amount}")
            return transaction
        else:
            print("Sender account not found.")
            return None

    def check_transfer_status(self, transaction):
        current_time = datetime.now()
        if transaction.receiver and not transaction.accepted:
            time_remaining = transaction.timestamp + timedelta(hours=24) - current_time
            print(f"Transfer is pending. Time remaining: {time_remaining}")
        else:
            print("Transfer has been executed.")

    def merge_accounts(self, account1, account2):
        if account1 and account2:
            merged_account = AccountMerger(account1, account2).merge_accounts()
            self.accounts.append(merged_account)
            self.accounts.remove(account1)
            self.accounts.remove(account2)
            print(f"Accounts {account1.account_number} and {account2.account_number} have been merged into {merged_account.account_number}.")
