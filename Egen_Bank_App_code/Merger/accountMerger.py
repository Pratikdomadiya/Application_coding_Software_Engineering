from Egen_Bank_App_code.account.account import Account
class AccountMerger:
    def __init__(self, account1, account2):
        self.account1 = account1
        self.account2 = account2

    def merge_accounts(self):
        merged_account = Account(f"Merged_{self.account1.account_number}_{self.account2.account_number}")
        merged_account.balance = self.account1.balance + self.account2.balance
        merged_account.transactions = self.account1.transactions + self.account2.transactions
        return merged_account

