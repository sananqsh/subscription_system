from datetime import timedelta
from customer import NotEnoughCredit
from invoice import Invoice

ZERO_TIMEDELTA = timedelta(0)

class Observer:
    def update(self, data):
        pass

class SubscriptionHandler(Observer):
    """Update user credit and generate invoice on time"""

    def __init__(self, customer, subscription, subscription_interval, time):
        self.customer = customer
        self.subscription = subscription
        self.subscription_interval = subscription_interval

        self.previous_usage = ZERO_TIMEDELTA
        self.activate(time)


    def update(self, time):
        # Test:
        print("==========Observer===========")
        if self.active:
            self.current_time = time

            if self.current_interval() >= self.subscription_interval:
                # Test:
                print("==========Interval reached!!!===========")

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

        # Test:
        print(f"start: {self.start_time.minute}")
        print(f"current_time: {self.current_time.minute}")
        print(f"previous_usage: {self.previous_usage}")
        print(f"delta: {self.current_interval()}")
        print("=================!!!================")

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
        invoice = Invoice(self.customer.id, self.subscription.title, self.subscription.price, self.start_time, self.current_time)
        self.customer.add_invoice(invoice)
