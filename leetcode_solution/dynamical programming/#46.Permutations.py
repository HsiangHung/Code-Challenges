#  46. Permutations (medium)
#  https://leetcode.com/problems/permutations/
#
#  Microsoft, LinkedIn
#
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dp = {0: [[nums[0]]]}
        
        it = 1
        while it < len(nums):
             
            dp[it] = []
            for x in dp[it-1]:
                for i in range(len(x)+1): # note, loop through to len(x)+1
                    dp[it].append(x[:i]+[nums[it]]+x[i:])

            it += 1
        
        return dp[len(nums)-1]