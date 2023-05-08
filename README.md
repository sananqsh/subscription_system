# Subscription System
Implementing the financial system of a cloud storage service using Python

## Summary:
In this system, customer subscribes to a service, periodically having its credit reduced.

Each time the credit reduces, an invoice will be generated for the customer.

Customer can add/remove subscriptions.

The system must generate invoice each 10 minutes.

Customer must be able to see the list of their subscriptions and invoices.

Finally, customer must be able to recieve a report on how many invoices and how much credit 
they have spent in the system.

## UML Class Diagram:
![UML Class Diagram](./images/UML_class_diagram.png)

## How to work with:
The system runs a loop in which each time we hit `enter`, time passes by 1 minute (these are time modelings that can easily be modified if the project is used in real world). In each iteration of this loop, we can input a command to interact with the system. To see all the commands enter this as the input: `help` and if you want to see the manual for a specific command/subcommand: `help [COMMAND]`.

## Install
  - ### Requirements
    - [python](https://www.python.org/downloads/)
  
  - Having installed the requirements, run the following commands in terminal:
    1. `git clone https://github.com/sananqsh/subscription_system.git`
    2. `cd subscription_system`
    3. `python3 main.py`
