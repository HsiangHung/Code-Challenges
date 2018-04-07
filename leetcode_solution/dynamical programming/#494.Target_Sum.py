# [# 494] Target Sum
#  
#  Google, facebook 
#
#
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if nums == []: return 0
        #return self.DFS(-1, nums, 0, S)
        
        '''This problems needs to considers the following dynamical programming approach
           to solve. Otherwise still exceed time limit.
           ref: http://bookshadow.com/weblog/2017/01/22/leetcode-target-sum/
           This turns to time complexity O(n*l) 
        '''
        
        
        dp = {0: 1}
        for x in nums:
            ndp = {}
            for possible_sum in dp.keys():
                for sgn in [1, -1]:
                    if possible_sum+sgn*x in ndp:
                        ndp[possible_sum+sgn*x] += dp[possible_sum]
                    else:
                        ndp[possible_sum+sgn*x] = dp[possible_sum]
            dp= ndp
            #print dp
        
        if S not in dp: return 0
        return dp[S]
        
        
    
    def DFS(self, depth, nums, sum, S):
        '''this method regards the problem as a binary tree, 
         "+" like left and "-" like right. The time complexity is O(2**n).
         But this method will exceed the time
        '''
        if depth == len(nums)-1:
            if sum == S:
                return 1
            else:
                return 0
        
        return self.DFS(depth+1, nums, sum+nums[depth+1], S)+self.DFS(depth+1, nums, sum-nums[depth+1], S)