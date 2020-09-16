import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Monkey Puzzle", 100.00)
        self.beer = Drink("Tennents", 4.00, 2.00)
        self.cocktail = Drink("Depth Charge",8.50, 3.00)
        self.pub.drinks = [self.beer, self.cocktail]

    def test_pub_has_name(self):
        self.assertEqual("The Monkey Puzzle", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual(2,len(self.pub.drinks))
    
    def test_add_money_to_till(self):
        money_to_add = self.beer.price
        self.pub.add_money_to_till(money_to_add)
        self.assertEqual(104.00, self.pub.till)

    def test_sell_drink(self):
        test_customer = Customer("Drunken Bob", 200, 53, 20.00)
        test_drink = self.beer
        self.pub.sell_drink(self.beer, test_customer)
        self.assertEqual(104.00, self.pub.till)
        self.assertEqual(196, test_customer.wallet)
        self.assertEqual(1, self.pub.stock_count())

    def test_add_drink(self):
        self.pub.add_drink(self.beer)
        self.assertEqual(3, len(self.pub.drinks))

    def test_remove_drink(self):
        self.pub.remove_drink(self.beer)
        self.assertEqual(1, len(self.pub.drinks))

    def test_stock_count(self):
        self.assertEqual(2, self.pub.stock_count())

    def test_age_check(self):
        test_customer = Customer("Young Bob", 1.50, 13, 0.00)
        self.assertEqual("Beat it scamp!", self.pub.sell_drink(self.beer, test_customer))

    def test_refuse_drunk(self):
        test_customer = Customer("Really Drunken Bob", 50.00, 23, 25.00)
        self.assertEqual("Beat it drunken scamp!", self.pub.sell_drink(self.cocktail, test_customer))