import unittest
import knapsack_01


class TestKnapsackZeroOne(unittest.TestCase):
    def setUp(self) -> None:
        self.zero_one_knap_sack = knapsack_01.zero_one_knapsack
        self.zero_one_knap_sack_opt_mem = knapsack_01.zero_one_knapsack_optimize_mem

    def test_case_1(self):
        costs = [10, 20, 30]
        values = [60, 100, 120]
        items = list(zip(costs, values))
        knapsack_size = 50
        result = self.zero_one_knap_sack(items, knapsack_size)
        answer = 220
        self.assertEqual(answer, result)

    def test_big_item_at_the_beginning(self):
        knapsack_size = 50
        costs = [50, 10, 20, 30]
        values = [200, 60, 100, 120]
        items = list(zip(costs, values))
        result = self.zero_one_knap_sack(items, knapsack_size)
        answer = 220
        self.assertEqual(answer, result)

    def test_two_possible_combinations(self):
        knapsack_size = 50
        costs = [40, 10, 20, 30]
        values = [150, 60, 100, 120]
        items = list(zip(costs, values))
        result = self.zero_one_knap_sack(items, knapsack_size)
        answer = 220
        self.assertEqual(answer, result)

    def test_opt_mem_version(self):
        knapsack_size = 50
        costs = [40, 10, 20, 30]
        values = [150, 60, 100, 120]
        items = list(zip(costs, values))
        result = self.zero_one_knap_sack_opt_mem(items, knapsack_size)
        answer = 220
        self.assertEqual(answer, result)


if __name__ == '__main__':
    unittest.main()
