from display import PrettyDisplay

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
        if self.can_pay(money):
            self.credit -= money
        else:
            raise NotEnoughCredit("Customer does not have enough credit")
    
    def add_invoice(self, invoice):
        self.invoices.append(invoice)

    def can_pay(self, money):
        return money <= self.credit
    
    def add_debt(self, debt_amount):
        self.debt += debt_amount

    def in_debt(self):
        return self.debt > 0
    
    def add_credit(self, credit):
        self.credit += credit
    
    def pay_debts(self):
        self.debt = 0

    def display_invoices(self):
        for invoice in self.invoices:
            invoice.display()
    
    def display_report(self):
        number_of_invoices = len(self.invoices)
        credit_spent = 0
        for invoice in self.invoices:
            credit_spent += invoice.price

        PrettyDisplay(
            f"Number of invoices generated: {number_of_invoices}",
            f"Credit spent by customer: {credit_spent}",
            f"Customer credit: {self.credit}",
            f"Customer debt: {self.debt}"
        )
