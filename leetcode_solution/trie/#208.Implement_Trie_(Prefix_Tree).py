# #208. Implement Trie (Prefix Tree)
# 
# https://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python
# https://blog.csdn.net/lisonglisonglisong/article/details/45584721
#
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for letter in word:
            current = current.setdefault(letter, {})
        current.setdefault("_end")
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
            
        if "_end" not in current:
            return False
        
        return True
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for letter in prefix:
            if letter not in current:
                return False
            current = current[letter]
        
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)