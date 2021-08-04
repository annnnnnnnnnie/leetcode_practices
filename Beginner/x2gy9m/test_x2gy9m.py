import unittest
from x2gy9m import Solution


def check_result(n, nums, answer):
    try:
        i = 0
        for ans in answer:
            if nums[i] != ans:
                return False
            i += 1
    except Exception as e:
        print(e)
        return False
    return True


class Tests(unittest.TestCase):
    def test_solution1(self):
        nums = [0, 0, 1, 1, 2, 2]
        n = Solution.remove_duplicates(nums)
        answer = [0, 1, 2]
        self.assertTrue(check_result(n, nums, answer))


if __name__ == '__main__':
    unittest.main()
