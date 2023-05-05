from datetime import timedelta
from customer import NotEnoughCredit
from invoice import Invoice

ZERO_TIMEDELTA = timedelta(0)

class Observer:
    def update(self, data):
        pass

class SubscriptionHandler(Observer):
    """Update user credit and generate invoice on time"""

    def __init__(self, customer, time, subscription_interval):
        self.customer = customer
        self.subscription_interval = subscription_interval
        
        self.previous_usage = ZERO_TIMEDELTA
        self.activate(time)


    def update(self, time):
        # Test:
        print("==========Observer===========")
        if self.active:
            self.time_at = time

            if self.current_interval() >= self.subscription_interval:
                # Test:
                print("==========Interval reached!!!===========")

                # Reduce credit from customer
                # TODO: charge by real subscription fee -> self.sub.price)
                try:
                  self.customer.charge(99)
                  self.generate_invoice()
                except NotEnoughCredit as e:
                  print(e.message())
                  self.customer.add_debt(99)
                  self.deactivate()

                # Update datetimes for next intervals (ignore cases when checking time at is more
                # than subscription_interval that can be calculated as the next interval of
                # subscription. For now...):
                self.start_date = self.time_at
                self.previous_usage = ZERO_TIMEDELTA

        # Test:
        print(f"start: {self.start_date.minute}")
        print(f"time_at: {self.time_at.minute}")
        print(f"delta: {self.current_interval()}")
        print("=================!!!================")

    def current_interval(self):
        return (self.time_at - self.start_date) + self.previous_usage

    def activate(self, time):
        if not self.customer.in_debt():
          self.start_date = time
          self.time_at = self.start_date
          self.active = True
        else:
            print("Customer has to pay their debts first!")
    
    def deactivate(self):
        self.previous_usage = self.current_interval()
        self.active = False

    def generate_invoice(self):
        invoice = Invoice(self.customer.id, "TEST", 99, self.start_date, self.time_at)
        self.customer.add_invoice(invoice)
