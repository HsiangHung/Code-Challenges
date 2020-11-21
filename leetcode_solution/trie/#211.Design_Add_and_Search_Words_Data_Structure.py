# 211. Design Add and Search Words Data Structure (medium)
# https://leetcode.com/problems/design-add-and-search-words-data-structure/
#
class WordDictionary:
    '''
    https://blog.csdn.net/fuxuemingzhu/article/details/79390052
    for ".", we need to BFS and search through to see if words.
    '''    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        current = self.root
        for letter in word:
            current[letter] = current.setdefault(letter, {})
            current = current[letter]
        
        current.setdefault("_end")
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """        
        current = self.root
        for i in range(len(word)):
            if word[i] != ".":
                if word[i] not in current:
                    return False
                current = current[word[i]]
            else:
                isFind = False
                for char in current:
                    isFind = isFind or self.DFS(word[i+1:], current[char])
                return isFind
        
        if "_end" not in current:
            return False
        
        return True
    
    
    def DFS(self, word, current):
        
        if current is None:
            if word is not None:
                return False
            else:
                return True
        
        for i in range(len(word)):
            if word[i] != ".":
                if word[i] not in current:
                    return False
                current = current[word[i]]
            else:
                isFind = False
                for char in current:
                    isFind = isFind or self.DFS(word[i+1:], current[char])
                return isFind
                
        if "_end" not in current:
            return False
        
        return True
        