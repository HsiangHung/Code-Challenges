#  78 Subsets (medium)
#  https://leetcode.com/problems/subsets/
#
#
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0: return []
        
        dp = {0: [], 1: [[x] for x in nums]}

        set_len = 2
        while set_len <= len(nums):
            
            dp[set_len] = []
            for num in nums:
                for subset in dp[set_len-1]:
                    if num > subset[-1]:
                        new_subset = subset + [num]
                        dp[set_len].append(new_subset)
            set_len += 1
        
        subsets = []
        for set_len in dp:
            subsets += dp[set_len]
        return [[]] + subsets