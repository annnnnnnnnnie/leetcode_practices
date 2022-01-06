import unittest
import Daily.src.jan6_2022


class TestSimplyPath(unittest.TestCase):
    def setUp(self) -> None:
        self.simplify_path = Daily.src.jan6_2022.simplify_path

    def test_join_root_only(self):
        path = "/"
        result = self.simplify_path(path)
        answer = "/"
        self.assertEqual(answer, result)

    def test_join_root_duplicate(self):
        path = "///"
        result = self.simplify_path(path)
        answer = "/"
        self.assertEqual(answer, result)

    def test_join_root_prev(self):
        path = "/../..///../"
        result = self.simplify_path(path)
        answer = "/"
        self.assertEqual(answer, result)

    def test_join_root_current_prev(self):
        path = "/../../././../"
        result = self.simplify_path(path)
        answer = "/"
        self.assertEqual(answer, result)

    def test_join_simple_dir(self):
        path = "/abc/def/g"
        result = self.simplify_path(path)
        answer = "/abc/def/g"
        self.assertEqual(answer, result)

    def test_join_relative(self):
        path = "/abc/../def///./g"
        result = self.simplify_path(path)
        answer = "/def/g"
        self.assertEqual(answer, result)
