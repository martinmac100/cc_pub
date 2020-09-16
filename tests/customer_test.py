import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Drunken Bob", 200.00)

    def test_customer_has_name(self):
        self.assertEqual("Drunken Bob",self.customer.name)

    