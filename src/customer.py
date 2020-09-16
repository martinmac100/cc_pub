class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age

    def remove_money_from_customer_wallet(self, money_to_remove):
        self.wallet -= money_to_remove