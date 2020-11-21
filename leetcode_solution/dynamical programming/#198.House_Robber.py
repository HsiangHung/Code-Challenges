#  198. House Robber (easy)
#  https://leetcode.com/problems/house-robber/
#
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []: return 0
        if len(nums) <= 2: return max(nums)
        
        dp = {0: nums[0], 1: max(nums[0], nums[1])}
        house = 2
        while house < len(nums):
            dp[house] = max(nums[house]+dp[house-2], dp[house-1])
            house += 1
            
        return dp[len(nums)-1]