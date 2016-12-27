## [Leetcode#78] Subsets
##
## e.g. nums = [1,2,3], gives [[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]
##
## Here I used dynamic programming
##
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dp = {}
        dp[0] = [[]]
        dp[1] = [[x] for x in nums]
        
        n = len(nums)
        
        i = 2
        while i <= n:
            dp[i] = []
            for ch1 in dp[i-1]:
                for ch2 in nums:
                    new_ch = ch1[:]
                    if ch2 not in new_ch:
                        new_ch.append(ch2)
                        new_ch = sorted(new_ch)
                        if new_ch not in dp[i]: dp[i].append(new_ch)
            i +=1
            
        subset = []
        for key in dp:
            for ch in dp[key]:
                subset.append(ch)
                
        return subset
        