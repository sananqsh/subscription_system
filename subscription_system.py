from datetime import datetime, timedelta
from subscription_handler import SubscriptionHandler
from customer import Customer

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
        self.subscriptions = []
        self._time = datetime.now()

    def run(self):
        while True:
            cmd = input()
            self.handle_cmd(cmd)
            self.pass_time()

            # Test:
            print(f"time: {self._time.minute}")

    def handle_cmd(self, cmd):
        if cmd == "add":
            # Test:
            customer = Customer(1, "sanan", 100)

            handler = SubscriptionHandler(customer, self._time, self.subscription_interval)
            Subject.subscribe(self, handler)
        elif cmd == "deact":
            self._observers[0].deactivate()
        elif cmd == "react":
            self._observers[0].activate(self._time)

    def pass_time(self):
        self._time += timedelta(minutes=1)
        self.notify(self._time)
