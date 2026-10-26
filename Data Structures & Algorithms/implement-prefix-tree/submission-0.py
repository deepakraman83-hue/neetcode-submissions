class TrieNode():
  def __init__(self):
    self.children={}
    self.is_end_word=False

class PrefixTree:

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        current=self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch]=TrieNode()
            current=current.children[ch]
        current.is_end_word=True


    def search(self, word: str) -> bool:
        current=self.root
        for ch in word:
            if ch not in current.children:
                return False
            current=current.children[ch]
        return current.is_end_word

        

    def startsWith(self, word: str) -> bool:
        current=self.root
        for ch in word:
            if ch not in current.children:
                return False
            current=current.children[ch]
        return True
        