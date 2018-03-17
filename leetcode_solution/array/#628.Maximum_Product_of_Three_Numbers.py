#[#628] Maximum Product of Three Numbers
#
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 3: return nums[0]*nums[1]*nums[2]
        
        nums = sorted(nums)
        
        return max(nums[-1]*nums[-2]*nums[-3], nums[-1]*nums[0]*nums[1])
        #return max(max_val*secmax_val*thirdmax_val, max_val*min_val*secmin_val)