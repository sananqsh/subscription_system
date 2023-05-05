class Invoice:
    def __init__(self, customer_id, subscription_title, subscription_fee, start_time, end_time):
        self.customer_id = customer_id
        self.subscription_title = subscription_title
        self.subscription_fee = subscription_fee
        self.start_time = start_time
        self.end_time = end_time
    
    def display(self):
        print("=======================Invoice=======================")
        print(f"========Customer ID: {self.customer_id}============================")
        print(f"======subscription: {self.subscription_title}============================")
        print(f"===========price: {self.subscription_fee}============================")
        print(f"=====start_time: {self.start_time}==============")
        print(f"======end_time: {self.end_time}==============")
        print("===========================================")