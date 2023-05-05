
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
        self.debt = 0

    def charge(self, money):
        if self.payable(money):
            self.credit -= money
        else:
            raise NotEnoughCredit("Customer does not have enough credit.")
    
    def add_invoice(self, invoice):
        self.invoices.append(invoice)

    def payable(self, money):
        return money <= self.credit
    
    def add_debt(self, debt_amount):
        self.debt += debt_amount

    def in_debt(self):
        return self.debt > 0
    
    def add_credit(self, credit):
        self.credit += credit
    
    def pay_debts(self):
        self.debt = 0