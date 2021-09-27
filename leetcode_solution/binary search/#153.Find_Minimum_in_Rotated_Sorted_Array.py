#  153. Find Minimum in Rotated Sorted Array (medium)
#  https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 3: return min(nums)
        
        mid = len(nums) // 2
        
        if  nums[mid] < nums[mid+1] and nums[mid-1] > nums[mid]:
            return nums[mid]
        else:
            if nums[mid] < nums[-1]:  # pivot is on left hand side
                return self.findMin(nums[:mid+1])
            else:                     # pivot is on right hand side
                return self.findMin(nums[mid:])
