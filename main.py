# from account.account import Account
from Egen_Bank_App_code.bank.bank import Bank
from Egen_Bank_App_code.Merger.accountMerger import AccountMerger



# Sample usage
if __name__ == "__main__":
    bank = Bank()

    bank.create_account("1001")
    bank.create_account("1002")
    bank.create_account("1003")

    account1 = bank.get_account("1001")
    account2 = bank.get_account("1002")
    account3 = bank.get_account("1003")

    account1.deposit(1000)
    account2.deposit(1500)
    account3.deposit(2000)

    account1.withdraw(500)
    account2.withdraw(300)

    print("Top Ranked Accounts:")
    ranked_accounts = bank.rank_accounts(2)
    for rank, account in enumerate(ranked_accounts, start=1):
        print(f"Rank {rank}: Account {account.account_number}, Total Transactions Value: {sum(t.amount for t in account.transactions)}")

    scheduled_transfer = bank.schedule_transfer("1002", "1001", 200)
    bank.check_transfer_status(scheduled_transfer)

    account1.accept_transfer(scheduled_transfer)
    bank.check_transfer_status(scheduled_transfer)

    merger = AccountMerger(account1, account2)
    merged_account = merger.merge_accounts()
    print(f"Merged Account: {merged_account.account_number}, Balance: {merged_account.balance}, Transaction Count: {len(merged_account.transactions)}")
