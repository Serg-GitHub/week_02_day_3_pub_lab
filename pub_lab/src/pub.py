class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def pub_sells_drink(self, amount):
        self.till += amount 