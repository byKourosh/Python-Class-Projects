class Account:
    def __init__(self, account_id, amount, branch, person):
        self.account_id = account_id
        self.amount = amount
        self.branch = branch
        self.person = person

    def bardasht(self):
        print("Withdraw")

    def variz(self):
        print("Deposit")

    def __str__(self):
        return f"Account {self.account_id} - {self.amount} - {self.branch}"