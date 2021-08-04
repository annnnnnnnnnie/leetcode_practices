import unittest
from x2zsx1 import Solution


class Tests(unittest.TestCase):
    def test_max_profit(self):
        prices = [1, 2, 3, 4, 5]

        max_profit = Solution.max_profit(prices)
        self.assertEqual(max_profit, 4)
