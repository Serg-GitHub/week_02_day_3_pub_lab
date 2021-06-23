from src.drinks import Drinks


class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def customer_buys_drink(self, price):
        self.wallet -= price
        return price

    
       