from account import Account


class Card(Account):
    def __init__(self, account_id, amount, branch, person, card_number):
        Account.__init__(self, account_id, amount, branch, person)
        self.card_number = card_number

    def __str__(self):
        return f"Card {self.account_id} - {self.amount} - {self.card_number}"