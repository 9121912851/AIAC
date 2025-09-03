import unittest
from task4 import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_single_item(self):
        self.cart.add_item("apple", 1.5)
        self.assertIn("apple", self.cart.items)
        self.assertEqual(self.cart.items["apple"], 1.5)

    def test_add_multiple_items(self):
        self.cart.add_item("apple", 1.5)
        self.cart.add_item("banana", 2.0)
        self.assertIn("apple", self.cart.items)
        self.assertIn("banana", self.cart.items)
        self.assertEqual(self.cart.items["banana"], 2.0)

    def test_add_item_overwrites_price(self):
        self.cart.add_item("apple", 1.5)
        self.cart.add_item("apple", 2.0)
        self.assertEqual(self.cart.items["apple"], 2.0)

    def test_remove_existing_item(self):
        self.cart.add_item("apple", 1.5)
        self.cart.remove_item("apple")
        self.assertNotIn("apple", self.cart.items)

    def test_remove_nonexistent_item(self):
        self.cart.add_item("apple", 1.5)
        # Should not raise an error
        self.cart.remove_item("banana")
        self.assertIn("apple", self.cart.items)

    def test_total_cost_empty_cart(self):
        self.assertEqual(self.cart.total_cost(), 0)

    def test_total_cost_single_item(self):
        self.cart.add_item("apple", 1.5)
        self.assertEqual(self.cart.total_cost(), 1.5)

    def test_total_cost_multiple_items(self):
        self.cart.add_item("apple", 1.5)
        self.cart.add_item("banana", 2.0)
        self.cart.add_item("orange", 3.0)
        self.assertEqual(self.cart.total_cost(), 6.5)

    def test_total_cost_after_removal(self):
        self.cart.add_item("apple", 1.5)
        self.cart.add_item("banana", 2.0)
        self.cart.remove_item("apple")
        self.assertEqual(self.cart.total_cost(), 2.0)

    def test_add_item_with_zero_price(self):
        self.cart.add_item("freebie", 0)
        self.assertIn("freebie", self.cart.items)
        self.assertEqual(self.cart.total_cost(), 0)

    def test_add_item_with_negative_price(self):
        self.cart.add_item("discount", -5)
        self.assertIn("discount", self.cart.items)
        self.assertEqual(self.cart.total_cost(), -5)

if __name__ == '__main__':
    unittest.main()
