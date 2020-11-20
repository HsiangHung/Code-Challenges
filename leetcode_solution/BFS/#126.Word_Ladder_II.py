# 126. Word Ladder II (hard)
# https://leetcode.com/problems/word-ladder-ii/
#
# DFS solution works, but "Time Limit Exceeded:
class Solution2:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        self.mapping = self.get_mapping(wordList)
        self.paths = []
        self.min_path = None
        self.DFS(beginWord, endWord, [beginWord], 1)
  
        if len(self.paths) == 0: return []
        
        return [x for x in self.paths if len(x) == self.min_path]
    
    
    def DFS(self, word, endWord, path, depth):
        if word == endWord: 
            self.paths.append(path)
            if self.min_path is None:
                self.min_path = depth
            else:
                self.min_path = min(self.min_path, depth)
            return
        
        if self.min_path is not None and depth >= self.min_path: return  # set up stop searching for shortest 
        
        for i in range(len(word)):
            new_word = word[:i] + "_" + word[i+1:]
            if new_word in self.mapping:
                for x in self.mapping[new_word]:
                    if x not in path:
                        self.DFS(x, endWord, path+[x], depth + 1)
        
    def get_mapping(self, wordList):
        mapping = {}
        for word in wordList:
            for i in range(len(word)):
                new_word = word[:i]+"_"+word[i+1:]
                if new_word not in mapping:
                    mapping[new_word] = set({word})
                else:
                    mapping[new_word].add(word)
        return mapping