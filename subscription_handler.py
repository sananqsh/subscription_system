from datetime import timedelta
from customer import NotEnoughCredit
from invoice import Invoice
from display import PrettyDisplay

ZERO_TIMEDELTA = timedelta(0)

class Observer:
    def update(self, data):
        pass

class SubscriptionHandler(Observer):
    """Update user credit and generate invoice on time"""

    def __init__(self, customer, subscription, subscription_interval, time):
        self.customer = customer
        self.subscription = subscription

        if not self.customer.can_pay(self.subscription.price):
            raise NotEnoughCredit("Customer does not have enough credit")
        self.subscription_interval = subscription_interval

        self.previous_usage = ZERO_TIMEDELTA
        self.activate(time)

    def update(self, time):
        if self.active:
            self.current_time = time

            if self.current_interval() >= self.subscription_interval:
                # Reduce credit from customer and Generate invoice
                try:
                    self.customer.charge(self.subscription.price)
                    self.generate_invoice()
                except NotEnoughCredit as e:
                    print(e.message())
                    self.customer.add_debt(self.subscription.price)
                    self.deactivate()

                self.start_time = self.current_time
                self.previous_usage = ZERO_TIMEDELTA

    def current_interval(self):
        return (self.current_time - self.start_time) + self.previous_usage

    def activate(self, time):
        if not self.customer.in_debt():
            self.start_time = time
            self.current_time = self.start_time
            self.active = True
        else:
            print("Customer has to pay their debts first!")
    
    def deactivate(self):
        self.previous_usage = self.current_time - self.start_time
        self.start_time = self.current_time
        self.active = False

    def generate_invoice(self):
        invoice = Invoice(self.customer.id, self.subscription.title, 
                          self.subscription.price, self.start_time, self.current_time)

        self.customer.add_invoice(invoice)

    def display(self):
        PrettyDisplay(
            "Subscription", f"Customer ID: {self.customer.id}", 
            f"subscription: {self.subscription.title}", f"is active: {self.active}",
            f"price: {self.subscription.price}"
        )
