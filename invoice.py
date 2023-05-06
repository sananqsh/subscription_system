from display import pretty_display

class Invoice:
    def __init__(self, customer_id, subscription_title, price, start_time, end_time):
        self.customer_id = customer_id
        self.subscription_title = subscription_title
        self.price = price
        self.start_time = start_time
        self.end_time = end_time
    
    def display(self):
        items = ["Invoice", f"Customer ID: {self.customer_id}", f"subscription: {self.subscription_title}",
                 f"price: {self.price}", f"start_time: {self.start_time}", f"end_time: {self.end_time}"]
        pretty_display(items)
