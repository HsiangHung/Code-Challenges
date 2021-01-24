# 126. Word Ladder II (hard)
# https://leetcode.com/problems/word-ladder-ii/
#
# The BFS + heap solution works, but "Time Limit Exceeded": only 21/39 test cases passed.
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        if endWord not in wordList: return []
        
        wordList_dict = {}
        for word in wordList:
            for i in range(len(word)):
                new_word = word[:i]+"_"+word[i+1:]
                if new_word not in wordList_dict:
                    wordList_dict[new_word] = set([word])
                else:
                    wordList_dict[new_word].add(word)                    
             
        heap = [(0, [beginWord], set([beginWord]))] # here also store set, for juding if word appeared.
            
        min_step = None
        ans = []
        while heap:

            step, path, wordSet = heapq.heappop(heap)
                  
            if path[-1] == endWord:
                if not min_step: 
                    min_step = step
                    ans.append(path)
                elif step == min_step:
                    ans.append(path)
                # note, here skip if step > min_step, we only need shortest transformation
                    
            if min_step is not None and step >= min_step: continue
            
            word = path[-1]
            for i in range(len(word)): 
                new_word = word[:i]+"_"+word[i+1:]
                
                if new_word in wordList_dict:
                    for x in wordList_dict[new_word]:
                        if x not in path:
                            wordSet2 = set(path+[x])
                            heapq.heappush(heap, (step+1, path+[x], wordSet2))

        return ans
    