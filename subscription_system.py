from datetime import datetime, timedelta
from subscription_handler import SubscriptionHandler
from customer import Customer
from subscription import Subscription

class Subject:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, data = None):
        for observer in self._observers:
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
        if command == "add":
            handler = SubscriptionHandler(self.customers[1], self.subscriptions["Cloud"], self.subscription_interval, self._time)
            Subject.subscribe(self, handler)
        elif command == "add sub":
            subscription = Subscription("Cloud", 49)
            self.subscriptions["Cloud"] = subscription
        elif command == "deact":
            self._observers[0].deactivate()
        elif command == "react":
            self._observers[0].activate(self._time)
        elif command == "pay debt":
            self.customers[1].pay_debts()


    def pass_time(self):
        self._time += timedelta(minutes=1)
        self.notify(self._time)
