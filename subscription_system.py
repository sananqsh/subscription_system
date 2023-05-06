from datetime import datetime, timedelta
from subscription_handler import SubscriptionHandler
from customer import Customer, NotEnoughCredit, CustomerInDebt
from subscription import Subscription
from display import AlertMessage

class Subject:
    def __init__(self):
        self._observers = {}

    def register(self, observer_key, observer):
        if observer not in self._observers:
            self._observers[observer_key] = observer

    def detach(self, observer_key):
        try:
            del self._observers[observer_key]
        except ValueError:
            pass

    def notify(self, data = None):
        for _, observer in self._observers.items():
            observer.update(data)

class SubscriptionSystem(Subject):
    """General class to manage subscriptions"""
    def __init__(self, subscription_interval=timedelta(minutes=3)):
        Subject.__init__(self)
        self.subscription_interval = subscription_interval
        self.subscriptions = {}
        self._time = datetime.now()
        self.customers = {}

    def run(self):
        while True:
            try:
                command = input()
                self.handle_command(command)
                self.pass_time()

            except NotEnoughCredit as e:
                AlertMessage(e.message())
            except KeyError:
                AlertMessage(f"Key(customer_id/subscription_title) not found")

            # Test:
            print(f"--> System Time: {self._time}")

    def handle_command(self, command):
        if command == "":
            return

        tokens = command.split(" ")
        invalid_command = False
        
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
            
            else:
                invalid_command = True

        elif tokens[0] == "subscribe":
            customer_id, title = tokens[1], tokens[2]
            self.subscribe_customer(customer_id, title)

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
            else:
                invalid_command = True
        
        elif tokens[0] == "report":
            customer_id = tokens[1]
            self.customers[customer_id].display_report()
        
        elif tokens[0] == "help":
            try:
                self.prompt_help(' '.join(tokens[1:]))
                return
            except IndexError:
                self.prompt_help()
                return
        
        if invalid_command:
            self.prompt_help()

    def add_subscription(self, title, price):
        subscription = Subscription(title, price)
        self.subscriptions[title] = subscription 

    def add_customer(self, customer_id, username, credit):
        customer = Customer(int(customer_id), username, credit)
        self.customers[customer_id] = customer

    def subscribe_customer(self, customer_id, title):
        handler_key = customer_id + title
        if handler_key in self._observers.keys():
            AlertMessage("Already subscribed!")
        else:
            try:
                handler = SubscriptionHandler(
                    self.customers[customer_id], self.subscriptions[title], 
                    self.subscription_interval, self._time
                )

                Subject.register(self, handler_key, handler)
            except CustomerInDebt as e:
                AlertMessage(e.message())

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

    def prompt_help(self, parent=""):
        commands = ["add", "subscribe", "deact", "react", "pay", "ls", "report"]

        print()
        print("-------------------------------------------------------------------")
        if parent == "add":
            print(f"Usage: {parent} [sub/customer/credit] [ARG...]")
            print()
            print("Add items to the subscription system")
        elif parent == "add sub":
            print(f"Usage: {parent} title price")
            print()
            print("Add subscription to the system")
        elif parent == "add customer":
            print(f"Usage: {parent} id username credit")
            print()
            print("Add customer to the system")
        elif parent == "add credit":
            print(f"Usage: {parent} customer_id amount")
            print()
            print("Add credit to customer")
        elif parent == "subscribe":
            print(f"Usage: {parent} customer_id subscription_title")
            print()
            print("Subscribe customer to a subscription")
        elif parent in ["deact", "react"]:
            print(f"Usage: deact/react customer_id subscription_title")
            print()
            print("Deactivate/activate a subscription")
        elif parent == "pay":
            print(f"Usage: {parent} customer_id")
            print()
            print("Pay user's debts")
        elif parent == "ls":
            print(f"Usage: {parent} [subs/invoices] customer_id")
            print()
            print("List customer's [subscriptions/invoices]")
        elif parent == "report":
            print(f"Usage: {parent} customer_id")
            print()
            print("Generate report of customer's invoices and credit spent in the system")
        else:
            print("Usage: COMMAND customer_id [ARGS...]")
            print("Commands:")
            for  cmd in commands:
                print()
                print("  " + cmd)

        print()
        print("For additional detail on each command try `help COMMAND [SUBCOMMAND]`")
        print("-------------------------------------------------------------------")
        print()
