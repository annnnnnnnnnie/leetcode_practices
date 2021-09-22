import unittest

from Daily.src.sep22_2021 import ListNode, count, cut, split_list_to_parts


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        three = ListNode(3, None)
        two = ListNode(2, three)
        one = ListNode(1, two)
        self.three_elem_list = one

        pass

    def test_count_3_elem_list(self):
        xs = self.three_elem_list
        result = count(xs)
        answer = 3
        self.assertEqual(answer, result)

    def test_cut_3_elem_list(self):
        xs = self.three_elem_list
        fst, snd = cut(xs, 2)
        n_fst = count(fst)
        ans_fst = 2
        n_snd = count(snd)
        ans_snd = 1
        self.assertEqual(ans_fst, n_fst)
        self.assertEqual(ans_snd, n_snd)

    def test_separate_3_elem_list(self):
        xs = self.three_elem_list
        result = split_list_to_parts(xs, 3)
        for x in result:
            length = count(x)
            self.assertEqual(1, length)


if __name__ == '__main__':
    unittest.main()
