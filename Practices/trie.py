class Trie:
    """
    Contains only unique lower-case words.
    """

    def __init__(self):
        self.children: {Trie} = {}
        self.is_end_of_word = False

    def insert(self, word: str) -> None:
        if not word:
            self.is_end_of_word = True
        else:
            c, cs = word[0], word[1:]
            if c in self.children:
                child = self.children[c]
                return child.insert(cs)
            else:
                self.children[c] = Trie()
                return self.children[c].insert(cs)

    def search(self, word: str) -> bool:
        if not word:
            return self.is_end_of_word
        else:
            c, cs = word[0], word[1:]
            if c in self.children:
                child = self.children[c]
                return child.search(cs)
            else:
                return False

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return self.is_end_of_word or (self.children is not None)
        else:
            c, cs = prefix[0], prefix[1:]
            if c in self.children:
                child = self.children[c]
                return child.startsWith(cs)
            else:
                return False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
