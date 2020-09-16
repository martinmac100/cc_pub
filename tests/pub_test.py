import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Ox", 100.00)
        self.beer = Drink("Tennents", 4.00)
        self.cocktail = Drink("Depth Charge",8.50)
        self.pub.drinks = [self.beer, self.cocktail]

    def test_pub_has_name(self):
        self.assertEqual("Ox", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual(2,len(self.pub.drinks))
    
    def test_add_money_to_till(self):
        money_to_add = self.beer.price
        self.pub.add_money_to_till(money_to_add)
        self.assertEqual(104.00, self.pub.till)

    def test_sell_drink(self):
        test_customer = Customer("Drunken Bob", 200)
        self.pub.sell_drink(self.beer.price, test_customer)
        self.assertEqual(104.00, self.pub.till)
        self.assertEqual(196, test_customer.wallet)

    def test_add_drink(self):
        self.pub.add_drink(self.beer)
        self.assertEqual(3, len(self.pub.drinks))

    def test_remove_drink(self):
        self.pub.remove_drink(self.beer)
        self.assertEqual(1, len(self.pub.drinks))

    