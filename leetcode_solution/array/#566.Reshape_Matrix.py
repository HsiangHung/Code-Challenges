# [#566] Reshape the Matrix
#
#
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) == r: return nums
        if r*c != len(nums)*len(nums[0]): return nums
        
        reshape_nums = []
        reshape_row = []
        for row in nums:
            for col in row:
                reshape_row.append(col)
                if len(reshape_row) == c:
                    reshape_nums.append(reshape_row)
                    reshape_row = []
                
        return reshape_nums