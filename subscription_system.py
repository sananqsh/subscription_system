from datetime import datetime, timedelta

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
