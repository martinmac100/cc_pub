import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Drunken Bob", 200.00, 53, 20.00)

    def test_customer_has_name(self):
        self.assertEqual("Drunken Bob",self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(200.00, self.customer.wallet)

    def test_remove_customer_money(self):
        money_to_remove = 10.00
        self.customer.remove_money_from_customer_wallet(money_to_remove)
        self.assertEqual(190.00, self.customer.wallet)

    def test_customer_has_age(self):
        self.assertEqual(53, self.customer.age)