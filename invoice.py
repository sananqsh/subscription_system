class Invoice:
    def __init__(self, customer_id, subscription_title, subscription_fee, start_date, end_date):
      self.customer_id = customer_id
      self.subscription_title = subscription_title
      self.subscription_fee = subscription_fee
      self.start_date = start_date
      self.end_date = end_date
    
    def display(self):
      print("=======================Invoice=======================")
      print(f"========Customer ID: {self.customer_id}============================")
      print(f"======subscription: {self.subscription_title}============================")
      print(f"===========price: {self.subscription_fee}============================")
      print(f"=====start_date: {self.start_date}==============")
      print(f"======end_date: {self.end_date}==============")
      print("===========================================")