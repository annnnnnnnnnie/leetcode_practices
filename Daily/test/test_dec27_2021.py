import random
import unittest
import Daily.src.dec27_2021


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.find_num_friend_requests = Daily.src.dec27_2021.num_friend_requests

    def test_case_1(self):
        ages = [16, 16]
        result = self.find_num_friend_requests(ages)
        answer = 2
        self.assertEqual(answer, result)

    def test_case_2(self):
        ages = [16, 17, 18]
        result = self.find_num_friend_requests(ages)
        answer = 2
        self.assertEqual(answer, result)

    def test_case_3(self):
        ages = [20, 30, 100, 110, 120]
        result = self.find_num_friend_requests(ages)
        answer = 3
        self.assertEqual(answer, result)

    def test_overtime_case_1(self):
        ages = [random.randint(1, 120) for _ in range(20000)]
        result = self.find_num_friend_requests(ages)


if __name__ == '__main__':
    unittest.main()
