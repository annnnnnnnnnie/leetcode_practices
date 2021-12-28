import unittest
from functools import reduce

import searching


class TestBinarySearch(unittest.TestCase):
    def setUp(self) -> None:
        self.b_search_multi = searching.binary_search_multiset
        self.b_search = searching.binary_search
        self.collapse_list = searching.collapse_list

    def test_search_in_all_strictly_increasing(self):
        xs = [i for i in range(10)]
        targets = [i for i in range(10)]
        for t in targets:
            result = self.b_search(xs, t)
            self.assertEqual(result, t)

    def test_collapse_list_3_occurrence(self):
        a = [i for i in range(10)] * 3
        xs = sorted(a)
        result = self.collapse_list(xs)
        answer = [(i, 3) for i in range(10)]
        self.assertListEqual(answer, result)

    def test_collapse_list_1_occurrence(self):
        a = [i for i in range(10)]
        xs = sorted(a)
        result = self.collapse_list(xs)
        answer = [(i, 1) for i in range(10)]
        self.assertListEqual(answer, result)

    def test_search_in_multiset_returns_first_occurrence(self):
        a = [i for i in range(10)] * 3
        xs = sorted(a)
        targets = [i for i in range(10)]
        for t in targets:
            result = self.b_search_multi(xs, t)
            self.assertEqual(result, t * 3)


if __name__ == '__main__':
    unittest.main()
