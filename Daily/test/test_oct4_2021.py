import unittest

from Daily.src import oct4_2021


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.format_license_key = oct4_2021.format_license_key
        self.reformat_string = oct4_2021.reformat_string
        self.separate_with = oct4_2021.separate_with

    def test_remove_break_and_to_upper(self):
        s = "123-abc-321-cba"
        result = self.reformat_string(s)
        answer = "123ABC321CBA"
        self.assertEqual(answer, result)

    def test_reformat_string_edge_case(self):
        s1 = "1-"
        s2 = "A"
        s3 = "b"
        result1 = self.reformat_string(s1)
        result2 = self.reformat_string(s2)
        result3 = self.reformat_string(s3)
        answer1 = "1"
        answer2 = "A"
        answer3 = "B"
        self.assertEqual(answer1, result1)
        self.assertEqual(answer2, result2)
        self.assertEqual(answer3, result3)

    def test_separate_with_break_divisible(self):
        s = "123ABC"
        k = 3
        result = self.separate_with('-', k, s)
        answer = "123-ABC"
        self.assertEqual(answer, result)

    def test_separate_with_break_not_divisible(self):
        s = "123ABCD"
        k = 3
        result = self.separate_with('-', k, s)
        answer = "1-23A-BCD"
        self.assertEqual(answer, result)

    def test_format_license_key_given_case_1(self):
        s = "5F3Z-2e-9-w"
        k = 4
        result = self.format_license_key(s, k)
        answer = "5F3Z-2E9W"
        self.assertEqual(answer, result)

    def test_format_license_key_given_case_2(self):
        s = "2-5g-3-J"
        k = 2
        result = self.format_license_key(s, k)
        answer = "2-5G-3J"
        self.assertEqual(answer, result)


if __name__ == '__main__':
    unittest.main()
