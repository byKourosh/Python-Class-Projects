from account import Account


class Saving(Account):
    def __init__(self, account_id, amount, branch, person, benefit_pct):
        Account.__init__(self, account_id, amount, branch, person)
        self.benefit_pct = benefit_pct

    def __str__(self):
        return f"Saving {self.account_id} - {self.amount} - {self.benefit_pct}%"