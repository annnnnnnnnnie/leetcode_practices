import unittest
import zhongzhixing


class TestSimpleCalc(unittest.TestCase):
    def setUp(self) -> None:
        self.parse_mult_div = zhongzhixing.parse_multiply_and_divide

    def test_parse_one_mult_operation(self):
        line = "1 * 2"
        result = self.parse_mult_div(line.split())
        expected = ["", "", 2]
        self.assertListEqual(expected, result)

    def test_parse_multiple_mult_div_op(self):
        line = "1 * 2 / 3 * 4"
        result = self.parse_mult_div(line.split())
        expected = ["", "", 2]

    def test_choose_song(self):
        songs = [chr(i) for i in range(ord('a'), ord('z'))]
        songs_priority = [10 * i for i in range(len(songs))]
        history = {}
        for _ in range(300):
            chosen = zhongzhixing.choose_song(songs, songs_priority)
            if chosen in history:
                history[chosen] += 1
            else:
                history[chosen] = 1
        sorted_history = sorted(history)
        print(sorted_history)
