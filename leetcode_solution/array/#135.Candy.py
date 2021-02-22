#  135. Candy (hard)
#  https://leetcode.com/problems/candy/ 
#
class Solution:
    '''
    https://www.cnblogs.com/grandyang/p/4575026.html 
    
    left to right and then right to left.
    if ratings[i] > ratings[i-1], candy[i] = candy[i-1]+1
    if ratings[i-1] > ratings[i] and candy[i-1] <= candy[i], candy[i-1] = candy[i] + 1
    e.g. [1,3,4,5,2]
    '''
    def candy(self, ratings: List[int]) -> int:
        
        ans = [1]*len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                ans[i] = ans[i-1] + 1
        
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i-1] > ratings[i] and ans[i-1] <= ans[i]:
                ans[i-1] = ans[i] + 1
        
        return sum(ans)
        
        