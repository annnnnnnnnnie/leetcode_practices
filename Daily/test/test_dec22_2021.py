import unittest

import Daily.src.dec22_2021


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.is_substring = Daily.src.dec22_2021.is_substring
        self.index_of = Daily.src.dec22_2021.index_of_slow
        self.repeated_string_match = Daily.src.dec22_2021.repeated_string_match

    def test_equal_string_is_substring(self):
        s1 = "abc"
        s2 = "abc"
        i = 0
        self.assertTrue(self.is_substring(s1, s2, i))

    def test_short_string_is_substring_of_long_string(self):
        s1 = "abcdef"
        s2 = "abc"
        i = 0
        self.assertTrue(self.is_substring(s1, s2, i))

    def test_middle_string_is_substring_of_long_string(self):
        s1 = "abcdef"
        s2 = "bcde"
        i = 1
        self.assertTrue(self.is_substring(s1, s2, i))

    def test_unequal_string_is_not_substring_of_each_other(self):
        s1 = "abcdef"
        s2 = "defab"
        i = 0
        self.assertFalse(self.is_substring(s1, s2, i))

    def test_can_find_index_of_substring(self):
        s1 = "abcdef"
        s2 = "bcd"
        result = self.index_of(s1, s2)
        answer = s1.index(s2)
        self.assertEqual(answer, result)

    def test_returns_minus_one_if_not_found(self):
        s1 = "abcdef"
        s2 = "qwe"
        result = self.index_of(s1, s2)
        answer = -1
        self.assertEqual(answer, result)

    def test_case_1(self):
        a = "abcd"
        b = "cdabcdab"
        result = self.repeated_string_match(a, b)
        answer = 3
        self.assertEqual(answer, result)

    def test_case_2(self):
        a = "a"
        b = "aa"
        result = self.repeated_string_match(a, b)
        answer = 2
        self.assertEqual(answer, result)

    def test_case_3(self):
        a = "a"
        b = "a"
        result = self.repeated_string_match(a, b)
        answer = 1
        self.assertEqual(answer, result)

    def test_case_4(self):
        a = "abc"
        b = "wxyz"
        result = self.repeated_string_match(a, b)
        answer = -1
        self.assertEqual(answer, result)

    def test_case_overtime(self):
        a = "a" * 9999
        b = "a" * 9998 + "b" + "a"
        result = self.repeated_string_match(a, b)
        answer = -1
        self.assertEqual(answer, result)


if __name__ == '__main__':
    unittest.main()
