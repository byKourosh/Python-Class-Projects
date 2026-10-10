from account import Account


class Check(Account):
    def __init__(self, account_id, amount, branch, person, start_num, end_num):
        Account.__init__(self, account_id, amount, branch, person)
        self.start_num = start_num
        self.end_num = end_num

    def __str__(self):
        return f"Check {self.account_id} - {self.amount} - {self.start_num} - {self.end_num}"