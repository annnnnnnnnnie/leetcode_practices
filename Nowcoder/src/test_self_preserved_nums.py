import unittest
import self_preserved_number


class TestHelperFunctions(unittest.TestCase):
    def setUp(self) -> None:
        self.is_spn = self_preserved_number.is_self_preserved_num
        self.generate_table = self_preserved_number.generate_table

    def test_good_spns_are_recognized(self):
        spns = [0, 1, 5, 6, 25, 76]
        for n in spns:
            self.assertTrue(self.is_spn(n))

    def test_bad_spns_are_rejected(self):
        not_spns = [2, 3, 4]
        for n in not_spns:
            self.assertFalse(self.is_spn(n))

    def test_generate_table(self):
        start = 0
        end = 100
        result = self.generate_table(start, end)
        print(result)
        for n in result:
            self.assertTrue(self.is_spn(n))


if __name__ == '__main__':
    unittest.main()
