import unittest
import trie


class TestTrieOperations(unittest.TestCase):
    def setUp(self) -> None:
        self.prefix_trie = trie.Trie()

    def test_initialize_trie(self):
        test_initialize_trie = trie.Trie()

    def test_insert_into_and_search_trie(self):
        words = ["a", "aa", "aab", "b", "bb", "bba"]
        for word in words:
            self.prefix_trie.insert(word)
        for word in words:
            self.assertTrue(self.prefix_trie.search(word))

        nonexistent_words = ["c", "abc", "bbc"]
        for non_word in nonexistent_words:
            self.assertFalse(self.prefix_trie.search(non_word))

    def test_repeated_insert_into_and_search_trie(self):
        words = ["a", "aa", "aab", "b", "bb", "bba"]
        for _ in range(10):
            for word in words:
                self.prefix_trie.insert(word)
        for word in words:
            self.assertTrue(self.prefix_trie.search(word))

        nonexistent_words = ["c", "abc", "bbc"]
        for non_word in nonexistent_words:
            self.assertFalse(self.prefix_trie.search(non_word))

    def test_trie_search_prefix_same_word(self):
        words = ["aaa"]
        prefixes = words
        for word in words:
            self.prefix_trie.insert(word)
        for prefix in prefixes:
            self.assertTrue(self.prefix_trie.startsWith(prefix))

    def test_trie_search_prefix_simple_prefix(self):
        words = ["aaab"]
        prefixes = ["aaa"]
        for word in words:
            self.prefix_trie.insert(word)
        for prefix in prefixes:
            self.assertTrue(self.prefix_trie.startsWith(prefix))

    def test_trie_search_prefix_larger_tree(self):
        words = ["cats", "dogs", "pumpkins"]
        prefixes = ["cat", "dog", "pump"]
        for word in words:
            self.prefix_trie.insert(word)
        for prefix in prefixes:
            self.assertTrue(self.prefix_trie.startsWith(prefix))

    def test_trie_search_non_prefix_should_return_false(self):
        words = ["cats", "dogs", "pumpkins"]
        non_prefixes = ["cate", "dod", "pumpkinsupermario"]
        for word in words:
            self.prefix_trie.insert(word)
        for non_prefix in non_prefixes:
            self.assertFalse(self.prefix_trie.startsWith(non_prefix))


if __name__ == '__main__':
    unittest.main()
