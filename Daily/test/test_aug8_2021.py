import unittest

from Daily.src import aug8_2021


class TestIterationMethod(unittest.TestCase):
    def setUp(self) -> None:
        self.test_subject = aug8_2021.tribonacci_iter

    def test_small_case1(self):
        n = 4
        answer = 4
        result = self.test_subject(n)
        self.assertEqual(answer, result)

    def test_big_case1(self):
        n = 37
        answer = 2082876103
        result = self.test_subject(n)
        self.assertEqual(answer, result)


class TestTableMethod(unittest.TestCase):
    def setUp(self) -> None:
        self.test_subject = aug8_2021.tribonacci_table

    def test_small_case1(self):
        n = 4
        answer = 4
        result = self.test_subject(n)
        self.assertEqual(answer, result)

    def test_big_case1(self):
        n = 37
        answer = 2082876103
        result = self.test_subject(n)
        self.assertEqual(answer, result)
