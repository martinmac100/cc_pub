class Customer:
    def __init__(self, name, wallet, age, drunkeness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkeness = drunkeness

    def remove_money_from_customer_wallet(self, money_to_remove):
        self.wallet -= money_to_remove

    def increase_drunkeness(self, alcohol_units):
        self.drunkeness += alcohol_units