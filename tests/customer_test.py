import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Drunken Bob", 200.00)

    def test_customer_has_name(self):
        self.assertEqual("Drunken Bob",self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(200.00, self.customer.wallet)

    def test_remove_customer_money(self):
        test_drink = Drink("Old Fashioned", 10.00)
        money_to_remove = test_drink.price
        self.customer.remove_money_from_customer_wallet(money_to_remove)
        self.assertEqual(190.00, self.customer.wallet)