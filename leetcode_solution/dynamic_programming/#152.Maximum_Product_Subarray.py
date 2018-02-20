## [Leetcode#152] Maximum Product Subarray
#
#
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxdp = {0: nums[0]}
        mindp = {0: nums[0]}
        maxproduct = nums[0]
        for i in range(1, len(nums)):
            maxdp[i] = max(maxdp[i-1]*nums[i], mindp[i-1]*nums[i], nums[i])
            mindp[i] = min(maxdp[i-1]*nums[i], mindp[i-1]*nums[i], nums[i])
            maxproduct = max(maxproduct, maxdp[i])
            
        return maxproduct
        