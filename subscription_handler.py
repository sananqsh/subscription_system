from datetime import timedelta

ZERO_TIMEDELTA = timedelta(0)

class Observer:
    def update(self, data):
        pass

class SubscriptionHandler(Observer):
    """Update user credit and generate invoice on time"""

    def __init__(self, time, subscription_interval):
        self.subscription_interval = subscription_interval
        
        self.previous_usage = ZERO_TIMEDELTA
        self.activate(time)


    def update(self, time):
        print("==========Observer===========")
        if self.active:
            self.time_at = time

            if self.current_interval() >= self.subscription_interval:
                print("==========Interval reached!!!===========")

                # TODO: Reduce credit and generate invoice

                # Update datetimes for next intervals (ignore cases when checking time at is more
                # than subscription_interval that can be calculated as the next interval of
                # subscription. For now...):
                self.start_date = self.time_at
                self.previous_usage = ZERO_TIMEDELTA


        print(f"start: {self.start_date}")
        print(f"time_at: {self.time_at}")
        print(f"delta: {self.current_interval()}")


        print("=================!!!================")

    def current_interval(self):
        return (self.time_at - self.start_date) + self.previous_usage

    def activate(self, time):
        self.start_date = time
        self.time_at = self.start_date
        self.active = True
    
    def deactivate(self):
        self.previous_usage = self.current_interval()
        self.start_date = ZERO_TIMEDELTA
        self.time_at = ZERO_TIMEDELTA
        self.active = False
