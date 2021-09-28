import unittest

from Daily.src import sep26_2021


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.get_sum = sep26_2021.get_sum

    def add_two_numbers(self, a, b):
        result = self.get_sum(a, b)
        answer = a + b
        self.assertEqual(answer, result)

    def test_add_small_positive(self):
        a = 3
        b = 2
        self.add_two_numbers(a, b)

    def test_add_zero_and_positive(self):
        a = 0
        b = 2
        self.add_two_numbers(a, b)

    def test_add_positive_and_zero(self):
        a = 2
        b = 0
        self.add_two_numbers(a, b)

    def test_add_zero_and_negative(self):
        a = 0
        b = -2
        self.add_two_numbers(a, b)

    def test_add_negative_and_zero(self):
        a = -2
        b = 0
        self.add_two_numbers(a, b)

    def test_add_negative_and_negative(self):
        a = -3
        b = -2
        self.add_two_numbers(a, b)

    def test_add_positive_and_negative(self):
        a = 4
        b = -2
        self.add_two_numbers(a, b)

    def test_add_negative_and_positive(self):
        a = -3
        b = 5
        self.add_two_numbers(a, b)

if __name__ == '__main__':
    unittest.main()
