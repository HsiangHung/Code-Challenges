## [Leetcode#213] House Robber II
#
# microsfot
#
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []: return 0
        if len(nums) <= 3: return max(nums)
        
        isFirstRob = False
        if max(nums[:3]) == nums[0]: 
            isFirstRob = True
            
        dp1 = {1: nums[0], 2: max(nums[0], nums[1]), 3: max(nums[0]+nums[2], nums[1])} ## consider first in dp 
        dp2 = {1: 0, 2: nums[1], 3: max(nums[1:3])}                                    ## not consider first in dp
        
        step = 4
        while step < len(nums):
            dp1[step] = max(dp1[step-1], dp1[step-2]+nums[step-1])
            dp2[step] = max(dp2[step-1], dp2[step-2]+nums[step-1])
            step += 1

        return max(dp1[len(nums)-1], dp2[len(nums)-1], dp2[len(nums)-2]+nums[step-1])
        