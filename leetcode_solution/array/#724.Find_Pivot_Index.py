# [#724] Find Pivot Index
#
# Coupang, radius
#
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3: return -1
        
        left = 0
        right = sum(nums[1:])
        for i in range(len(nums)-1):
            if left == right:
                return i
            else:
                left += nums[i]
                right -= nums[i+1]
                
        if left == 0: return len(nums)-1
                
        return -1