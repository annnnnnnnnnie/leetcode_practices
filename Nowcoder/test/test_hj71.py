import unittest
import Nowcoder.src.hj71_simple_regex as solution


class MyTestCase(unittest.TestCase):
    def test_can_simplify_pattern(self):
        pattern = "abc***abc**abc*"
        simplified = solution.simplify_pattern(pattern)
        answer = "abc*abc*abc*"
        self.assertEqual(answer, simplified)

    def test_can_simplify_complex_pattern(self):
        pattern = "abc*?**abc**?abc*"
        simplified = solution.simplify_pattern(pattern)
        answer = "abc*?*abc*?abc*"
        self.assertEqual(answer, simplified)

    def test_can_match_simple_string(self):
        pattern = "abc"
        s = "abc"
        self.assertTrue(solution.can_match(pattern, s))

    def test_can_match_simple_string_case_insensitive(self):
        pattern = "ABC"
        s = "abc"
        self.assertTrue(solution.can_match(pattern, s))

    def test_can_match_simple_string_incl_symbols(self):
        pattern = "a^^bc##"
        s = "a^^bc##"
        self.assertTrue(solution.can_match(pattern, s))

    def test_can_match_single_wildcard(self):
        pattern = "abc?abc"
        s = "abcdabc"
        self.assertTrue(solution.can_match(pattern, s))

    def test_can_match_multiple_wildcard(self):
        pattern = "??abc??abc??"
        s = "xxabcxxabcxx"
        self.assertTrue(solution.can_match(pattern, s))

    def test_can_match_single_star(self):
        pattern = "*"
        s = "abcdefg"
        self.assertTrue(solution.can_match(pattern, s))

    def test_can_match_multiple_star(self):
        pattern = "1*t*tx*s"
        s = "123txtxls"
        self.assertTrue(solution.can_match(pattern, s))

    def test_can_match_multiple_star_and_symbols(self):
        pattern = "1*.t*t.x*s"
        s = "123.txtxt.xls"
        self.assertTrue(solution.can_match(pattern, s))

    def test_can_match_trailing_star(self):
        pattern = "abc*"
        s = "abc"
        self.assertTrue(solution.can_match(pattern, s))

    def test_cannot_match_unmatched(self):
        pattern = "1*.t*t.x*s"
        s = "123.txt.xls.xx"
        self.assertFalse(solution.can_match(pattern, s))

    def test_star_cannot_match_symbol(self):
        pattern = "*"
        s = "."
        self.assertFalse(solution.can_match(pattern, s))


if __name__ == '__main__':
    unittest.main()
