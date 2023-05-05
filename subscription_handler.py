from datetime import datetime, timedelta

class Observer:
    def update(self, data):
        pass

class SubscriptionHandler(Observer):
    """Update user credit and generate invoice on time"""

    def __init__(self, subscription_interval):
        self.subscription_interval = subscription_interval
        
        self.previous_usage = timedelta(0)
        self.activate()


    def update(self, time):
        pass

    def activate(self):
        self.start_date = datetime.now()
        self.time_at = self.start_date
        self.active = True
    
    def deactivate(self):
        self.active = False
