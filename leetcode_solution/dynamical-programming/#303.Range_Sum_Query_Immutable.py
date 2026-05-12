## [Leetcode#303] Range Sum Query - Immutable
#
#
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if nums == []: 
            self.sum = None
            return
        
        self.sum = {0: nums[0]}
        if len(nums) >= 1:
            for i in range(1, len(nums)):
                self.sum[i] = self.sum[i-1] + nums[i]
                
        print self.sum

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i >= 1:
            return self.sum[j] - self.sum[i-1]
        else:
            return self.sum[j]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)