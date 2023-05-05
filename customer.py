
class NotEnoughCredit(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    
    def message(self):
        return self.args[0]

class Customer:
    def __init__(self, id, username, credit):
        self.id = id
        self.username = username
        self.credit = credit
        self.invoices = []

    def charge(self, money):
        if self.payable(money):
            self.credit -= money
        else:
            raise NotEnoughCredit("Customer does not have enough credit.")
    
    def add_invoice(self, invoice):
        self.invoices.append(invoice)

    def payable(self, money):
        return money <= self.credit
        