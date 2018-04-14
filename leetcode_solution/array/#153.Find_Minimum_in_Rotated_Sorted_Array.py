# [#153] Find Minimum in Rotated Sorted Array
#
#
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 3:
            return min(nums)
        
        #
        #   [1,2,4,5,6,7,0]
        #   check mid = 5, and 
        #   compare nums[mid] and start=left[0] of left=nums[:mid] 
        #                     and end=right[-1] of right=nums[mid+1:]
        #   recursion to left if start > nums[mid]
        #             to right if nums[mid] > end
        
        mid = len(nums) // 2 
        
        print nums[mid]
        if nums[mid] > nums[mid+1]:
            return nums[mid+1]
        elif nums[mid-1] > nums[mid]:
            return nums[mid]
        else:
            left, right = nums[:mid], nums[mid+1:]
            
            start, end = left[0], right[-1]
            
            if nums[mid] > end:
                return self.findMin(right)
            else:
                return self.findMin(left)
                