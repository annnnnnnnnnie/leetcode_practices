import unittest
import knapsack_complete


class TestKnapsackComplete(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


class TestPreprocessItems(unittest.TestCase):
    def setUp(self) -> None:
        self.preprocess_items = knapsack_complete.preprocess_item_list

    def test_can_throw_away_duplicates(self):
        knapsack_size = 30
        items = [(10, 20) for _ in range(3)]
        result = self.preprocess_items(items, knapsack_size)
        answer = [(10, 20)]
        self.assertListEqual(answer, result)

    def test_can_throw_away_expensive_ones(self):
        knapsack_size = 30
        items = list(zip([30, 40, 50], [300, 400, 500]))
        result = self.preprocess_items(items, knapsack_size)
        answer = [(30, 300)]
        self.assertListEqual(answer, result)

    def test_can_throw_away_less_cost_effective_ones(self):
        knapsack_size = 30
        items = list(zip([30, 30, 30], [300, 400, 500]))
        result = self.preprocess_items(items, knapsack_size)
        answer = [(30, 500)]
        self.assertListEqual(answer, result)


if __name__ == '__main__':
    unittest.main()
