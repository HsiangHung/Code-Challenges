#  287. Find the Duplicate Number (medium)
#  https://leetcode.com/problems/find-the-duplicate-number/
#
class Solution:
    '''
    https://www.cnblogs.com/grandyang/p/4843654.html 
    
    e.g. nums = [1,3,4,2,2], so n = 4, array = [1,2,3,4]
    
    i mid j
    1  2  4  # of nums = 3 for nums <= 2, go [1,2]
    1  1  2  # of nums = 1 for nums <= 1, go [2]
    
    time complexity > O(n) but < O(n^2). Space O(1)
    '''
    def findDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)-1
        
        return self.DFS(nums, 1, n)
        
    def DFS(self, nums, i, j):
        
        if i == j: return i
        
        mid = (j-i) // 2 + i
                
        ct = len([1 for x in nums if x <= mid])
        
        if j == i + 1:
            if ct > mid: 
                return i
            else:
                return j
        
        if ct > mid:
            return self.DFS(nums, i, mid)
        else:
            return self.DFS(nums, mid, j)
