import itertools
import unittest
from collections import Counter

from Beginner.x2ba4i import x2ba4i


def get_answer(nums):
    zeros = itertools.filterfalse(lambda n: n != 0, nums)
    no_zero = itertools.filterfalse(lambda n: n == 0, nums)
    result = list(itertools.chain(no_zero, zeros))
    return result


class TestOverall(unittest.TestCase):
    def setUp(self) -> None:
        self.put_off_zeros = x2ba4i.move_zeros

    def test_simple_case_1(self):
        nums = [1, 0]
        self.put_off_zeros(nums)
        result = nums
        answer = get_answer(nums)
        self.assertListEqual(answer, result)

    def test_simple_case_2(self):
        nums = [0, 1]
        self.put_off_zeros(nums)
        result = nums
        answer = get_answer(nums)
        self.assertListEqual(answer, result)

    def test_simple_case_3(self):
        nums = [0, 1, 0, 0, 2]
        self.put_off_zeros(nums)
        result = nums
        answer = get_answer(nums)
        self.assertListEqual(answer, result)

    def test_long_case_1(self):
        nums = [-959151711, 623836953, 209446690, -1950418142, 1339915067, -733626417, 481171539, -2125997010,
                -1225423476, 1462109565, 147434687, -1800073781, -1431212205, -450443973, 50097298, 753533734,
                -747189404, -2070885638, 0, -1484353894, -340296594, -2133744570, 619639811, -1626162038, 669689561, 0,
                112220218, 502447212, -787793179, 0, -726846372, -1611013491, 204107194, 1605165582, -566891128,
                2082852116, 0, 532995238, -1502590712, 0, 2136989777, -2031153343, 371398938, -1907397429, 342796391,
                609166045, -2007448660, -1096076344, -323570318, 0, -2082980371, 2129956379, -243553361, -1549960929,
                1502383415, 0, -1394618779, 694799815, 78595689, -1439173023, -1416578800, 685225786, -333502212,
                -1181308536, -380569313, 772035354, 0, -915266376, 663709718, 1443496021, -777017729, -883300731,
                -387828385, 1907473488, -725483724, -972961871, -1255712537, 383120918, 1383877998, 1722751914, 0,
                -1156050682, 1952527902, -560244497, 1304305692, 1173974542, -1313227247, -201476579, -298899493,
                -1828496581, -1724396350, 1933643204, 1531804925, 1728655262, -955565449, 0, -69843702, -461760848,
                268336768, 1446130876]

        self.put_off_zeros(nums)
        result = nums
        answer = get_answer(nums)
        self.assertListEqual(answer, result)

    def test_long_case_2(self):
        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                0, 0, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
                52, 53,
                54, 55, 56, 57, 58, 59, 60, 61, 0, 0, 0, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
                78, 79,
                80, 81, 0, 0, 0, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 0, 92, 93, 94, 95, 96, 97, 0, 98, 99, 0]

        self.put_off_zeros(nums)
        result = nums
        answer = get_answer(nums)
        self.assertListEqual(answer, result)
