class TrieNode:
    def __init__(self, isEnd=False):
        self.children = {}
        self.isEnd = isEnd


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        t = self.root
        for i in word:
            if not i in t.children:
                t.children[i] = TrieNode()
            t = t.children[i]
        t.isEnd = True

    def startsWith(self, prefix: str):
        t = self.root
        for i in prefix:
            if not i in t.children:
                return False
            t = t.children[i]
        return True

    def search(self, word: str) -> bool:
        t = self.root
        for i in word:
            if not i in t.children:
                return False
            t = t.children[i]
        return t.isEnd
