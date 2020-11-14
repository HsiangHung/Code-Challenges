# 127. Word Ladder
#
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        http://bookshadow.com/weblog/2015/08/17/leetcode-word-ladder/
        BFS trick: always save as paths and number of steps BFS=[("hot", 2)], ....
        pop(0) always first and then append more possible combination
        always need a set to record visited nodes or paths etc
        '''
        mapping = self.get_mapping(wordList)
        
        BFS = [(beginWord, 1)]
    
        visited = set({})
    
        while BFS:
            word, num_changes = BFS.pop(0)
            
            if word == endWord: return num_changes
            
            for i in range(len(word)):
                new_word = word[:i]+"_"+word[i+1:]
                if new_word in mapping:
                    for x in mapping[new_word]:
                        if x not in visited:
                            BFS.append((x, num_changes + 1))
                            visited.add(x)
        
        return 0
        
        
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