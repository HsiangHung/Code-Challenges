# [#561] Array Partition I
#
#
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        
        return sum([nums[i] for i in range(0, len(nums), 2)])
        