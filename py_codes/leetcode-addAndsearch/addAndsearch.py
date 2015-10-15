class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.value = 0
        self.children = [None] * 26


class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()
        """
        initialize your data structure here.
        """
    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        p = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not p.children[idx]:
                p.children[idx] = TrieNode()
            p = p.children[idx]
        p.value = 1

    def search(self, word):
        return self.find(self.root, word)

    def find(self, node, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if word == '':
            return (node.value == 1)

        ch = word[0]
        if ch == '.':
            for p in node.children:
                if p and self.find(p, word[1:]):
                    return True
            return False
        else:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
            return self.find(node, word[1:])
# Your WordDictionary object will be instantiated and called as such:
# test = WordDictionary()
# test.addWord("word")
# test.addWord("bad")
# print test.search("b.d")
# print test.search(".ord")
