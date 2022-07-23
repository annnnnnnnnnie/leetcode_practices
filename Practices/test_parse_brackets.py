import unittest
import parse_brackets


class TestParser(unittest.TestCase):
    def setUp(self) -> None:
        self.parse = parse_brackets.parser
        self.preprocess = parse_brackets.preprocess

    def test_parse_single_pair(self):
        input_string = "()"
        tokens = self.preprocess(input_string)
        result = self.parse(tokens)
        self.assertTrue(result)

    def test_parse_double_pair(self):
        input_string = "(())"
        tokens = self.preprocess(input_string)
        result = self.parse(tokens)
        self.assertTrue(result)

    def test_parse_consecutive_pair(self):
        input_string = "()()()"
        tokens = self.preprocess(input_string)
        result = self.parse(tokens)
        self.assertTrue(result)

    def test_parse_wrong_pair(self):
        input_string = "()()())"
        tokens = self.preprocess(input_string)
        result = self.parse(tokens)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
