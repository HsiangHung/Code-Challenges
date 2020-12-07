#  494. Target Sum (medium)
#  https://leetcode.com/problems/target-sum/
#  
#  Google, facebook 
#
#
#############################################################################

class Solution2:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        '''
        using tree to find the number of combination is too slow.
        Using dynamic programming is faster.
        e.g. if nums = [1,1,1,1,1...]
        dp = {1:1, -1:1}, {2:1, 0:2, -2:1}, {3:1, 1:3, -1:3, -3:1}, {4:1, 2:4, 0:6, -2:4, -4:1}.....
        think from this sequence

        Need to consider the corner case like:
        [0,0,0,0,0,0,0,0,1], target = 1
        '''
        if nums[0] != 0:
            dp = {0: {nums[0]: 1, -nums[0]: 1}}
        else:
            dp = {0: {0: 2}}
                
        index = 1
        while index < len(nums):
            
            combine_sum = {}
            for x in dp[index-1]:
                combine_sum[x+nums[index]] = combine_sum.get(x+nums[index], 0) + dp[index-1][x]
                combine_sum[x-nums[index]] = combine_sum.get(x-nums[index], 0) + dp[index-1][x]      
            
            dp[index] = combine_sum
            index += 1
            
        if S in dp[len(nums)-1]:
            return dp[len(nums)-1][S]
        else:
            return 0


#############################################################################

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
