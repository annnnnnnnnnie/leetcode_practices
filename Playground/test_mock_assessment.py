import unittest
import mock_assessment_q1, mock_assessment_q2, mock_assessment_q3


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.words_avg_weight = mock_assessment_q1.compute_sentence_avg_weight
        self.compute_num_permutations = mock_assessment_q3.compute_permutations

    def test_three_words_avg_weight(self):
        line = "Who love solo"
        words = line.strip().split()
        result = self.words_avg_weight(words)
        rounded = round(result, 2)
        answer = 3.67
        self.assertEqual(answer, rounded)

    def test_integer_avg_weight(self):
        line = "What does solo mean"
        words = line.strip().split()
        result = self.words_avg_weight(words)
        rounded = round(result, 2)
        answer = 4
        self.assertEqual(answer, rounded)

    def test_compute_all_same_permutation(self):
        line = "AAA"
        result = self.compute_num_permutations(line)
        answer = 1
        self.assertEqual(answer, result)


if __name__ == '__main__':
    unittest.main()
