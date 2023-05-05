from datetime import datetime, timedelta
from subscription_system import SubscriptionSystem
from customer import Customer

if __name__ == "__main__":
    sub_system = SubscriptionSystem()
    customer = Customer(1, "sanan", 100)
    sub_system.customers["1"] = customer
    sub_system.run()
