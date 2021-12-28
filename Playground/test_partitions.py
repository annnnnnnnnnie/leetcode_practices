import unittest
import miscs


class TestPartitions(unittest.TestCase):
    def setUp(self) -> None:
        self.partition = miscs.partition

    def test_partition_3_elements(self):
        xs = [1, 2, 3]
        result = self.partition(xs)
        answer = [([], [1, 2, 3]), ([1], [2, 3]), ([2], [1, 3]), ([3], [1, 2])]
        self.assertListEqual(answer, result)

    def test_partition_4_elements(self):
        xs = [1, 2, 3, 4]
        result = self.partition(xs)
        print(result)

    def test_partition_10_elements(self):
        xs = [i for i in range(10)]
        result = self.partition(xs)
        print(result)


if __name__ == '__main__':
    unittest.main()
