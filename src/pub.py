class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def add_money_to_till(self, money_to_add):
        self.till += money_to_add

    def sell_drink(self, drink_price, customer):
        self.add_money_to_till(drink_price)
        customer.remove_money_from_customer_wallet(drink_price)

    def add_drink(self, drink):
        self.drinks.append(drink)

    def remove_drink(self, drink):
        self.drinks.remove(drink)

    def stock_count(self):
        return len(self.drinks)