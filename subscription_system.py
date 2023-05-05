from datetime import datetime, timedelta
from subscription_handler import SubscriptionHandler
from customer import Customer
from subscription import Subscription

class Subject:
    def __init__(self):
        self._observers = {}

    def subscribe(self, observer_key, observer):
        if observer not in self._observers:
            self._observers[observer_key] = observer

    def unsubscribe(self, observer_key):
        try:
            del self._observers[observer_key]
        except ValueError:
            pass

    def notify(self, data = None):
        for _, observer in self._observers.items():
            observer.update(data)

class SubscriptionSystem(Subject):
    """General class to manage subscriptions"""
    def __init__(self, subscription_interval=timedelta(minutes=10)):
        Subject.__init__(self)
        self.subscription_interval = subscription_interval
        self.subscriptions = {}
        self._time = datetime.now()
        self.customers = {}

    def run(self):
        while True:
            command = input()
            self.handle_command(command)
            self.pass_time()

            # Test:
            print(f"time: {self._time.minute}")

    def handle_command(self, command):
        tokens = command.split(" ")
        if tokens[0] == "add":
            if tokens[1] == "sub":
                title, price = tokens[2], int(tokens[3])
                self.add_subscription(title, price)

            elif tokens[1] == "customer":
                customer_id, username , credit = tokens[2], tokens[3], int(tokens[4])
                self.add_customer(customer_id, username, credit)

            elif tokens[1] == "credit":
                customer_id, credit_amount = tokens[2], int(tokens[3])
                self.customers[customer_id].add_credit(credit_amount)

        elif tokens[0] == "subscribe":
            customer_id, title = tokens[1], tokens[2]
            self.subscribe_user(customer_id, title)

        elif tokens[0] == "deact":
            customer_id, title = tokens[1], tokens[2]
            self.deactivate_subscription(customer_id, title)

        elif tokens[0] == "react":
            customer_id, title = tokens[1], tokens[2]
            self.activate_subscription(customer_id, title, self._time)
            
        elif tokens[0] == "pay":
            customer_id = tokens[1]
            self.customers[customer_id].pay_debts()

        elif tokens[0] == "ls":
            customer_id = tokens[2]
            if tokens[1] == "subs":
                self.list_customer_subs(customer_id)
            elif tokens[1] == "invoices":
                self.customers[customer_id].display_invoices()
        
        elif tokens[0] == "report":
            customer_id = tokens[1]
            self.customers[customer_id].display_report()

    def add_subscription(self, title, price):
        subscription = Subscription(title, price)
        self.subscriptions[title] = subscription 

    def add_customer(self, customer_id, username, credit):
        customer = Customer(int(customer_id), username, credit)
        self.customers[customer_id] = customer

    def subscribe_user(self, customer_id, title):
        handler_key = customer_id + title
        if handler_key in self._observers.keys():
                print("Already subscribed!")
        else:
            handler = SubscriptionHandler(
                self.customers[customer_id], self.subscriptions[title], 
                self.subscription_interval, self._time
            )

            Subject.subscribe(self, handler_key, handler)


    def deactivate_subscription(self, customer_id, title):
        handler_key = customer_id + title
        self._observers[handler_key].deactivate()

    def activate_subscription(self, customer_id, title, time):
        handler_key = customer_id + title
        self._observers[handler_key].activate(time)

    def list_customer_subs(self, customer_id):
        for key, sub in self._observers.items():
            if key.startswith(customer_id):
                sub.display()        
         
    def pass_time(self):
        self._time += timedelta(minutes=1)
        self.notify(self._time)
