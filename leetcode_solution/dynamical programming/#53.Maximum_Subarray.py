# 53 Maximum Subarray (easy)
# https://leetcode.com/problems/maximum-subarray/
#
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = {0: nums[0]}
        maxsubarray = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            maxsubarray = max(maxsubarray, dp[i])
            
        return maxsubarray