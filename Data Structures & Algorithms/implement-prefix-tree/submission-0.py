class Trie:
    def __init__(self):
        self.child = [None]*26
        self.EndWord = False

class PrefixTree:

    def __init__(self):
        self.root = Trie()

    def insert(self, word: str) -> None:

        cur  = self.root
        for i in word:
            idx= ord(i)-ord('a')
            if cur.child[idx] is None:
                new_node = Trie()
                cur.child[idx] = new_node
            cur = cur.child[idx]
        cur.EndWord = True
        

    def search(self, word: str) -> bool:
        cur = self.root

        for i in word:
            idx = ord(i)-ord('a')
            if cur.child[idx]:
                cur = cur.child[idx]
            else:
                return False
        return cur.EndWord
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for i in prefix:
            idx = ord(i)-ord('a')
            if cur.child[idx]:
                cur = cur.child[idx]
            else:
                return False
        return True
        
        