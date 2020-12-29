#  403. Frog Jump (hard)
#  https://leetcode.com/problems/frog-jump/ 
#
class Solution:
    '''
    Using dynamical programming. Use DFS or BFS will time exceed.
    
    at each iteration i, stone unit = stones[i], infer and store what possible next units, i.e.
    
    dp[stone unit] = {previous possible units}
    
    e.g. [0,1,3,5,6,8,12,17]
    
    initially dp = {0: set([0]), 1: set([0])}
    
    i stones[i]  dp   
    1   1        {0: {0}, 1: {0}}
    2   3        {0: {0}, 1: {0}, 3: {1}}
    3   5        {0: {0}, 1: {0}, 3: {1}, 5: {3}, 6: {3}}
    4   6        {0: {0}, 1: {0}, 3: {1}, 5: {3}, 6: {3, 5}, 8: {5}}
    5   8        {0: {0}, 1: {0}, 3: {1}, 5: {3}, 6: {3, 5}, 8: {5, 6}}
    6  12        {0: {0}, 1: {0}, 3: {1}, 5: {3}, 6: {3, 5}, 8: {5, 6}, 12: {8}}
    7  17        {0: {0}, 1: {0}, 3: {1}, 5: {3}, 6: {3, 5}, 8: {5, 6}, 12: {8}, 17: {12}}
    
    we see the last stone unit appearing in dp, so return True
    
    if at i and stones[i] not in dp, go next i+1, ....
    '''
    def canCross(self, stones: List[int]) -> bool:
        
        if stones[1]-stones[0] > 1: return False
        
        stones_set = set(stones)
        
        dp = {0: set([0]), 1: set([0])}
   
        i = 1
        while i <= len(stones)-1:
            if stones[i] in dp:
                
                for prev in dp[stones[i]]:
                    jump = stones[i]-prev
                    nexts = [stones[i]+jump+x for x in [-1, 0, 1]]
                    for next in nexts:
                        if next in stones_set and next != stones[i]:
                            if next in dp:
                                dp[next].add(stones[i])
                            else:
                                dp[next] = set([stones[i]])
            
            i += 1
            # print (i, dp)
        
        return stones[-1] in dp
