
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

    def charge(self, money):
        # Test:
        print("============Customer.charge()============")
        print(f"credit: {self.credit}, money: {money}")

        if self.payable(money):
            self.credit -= money
            # Test:
            print(f"credit ==> {self.credit}")
        else:
            raise NotEnoughCredit("Customer does not have enough credit.")
        

    def payable(self, money):
        return money <= self.credit
        