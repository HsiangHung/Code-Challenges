#  153. Find Minimum in Rotated Sorted Array (medium)
#  https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) <= 2: return min(nums)
        
        mid = len(nums) // 2
        
        if nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
            return nums[mid]
        elif nums[0] < nums[mid]:
            if nums[mid] > nums[-1]:
                return self.findMin(nums[mid+1:])
            else:
                return self.findMin(nums[:mid])
        else:
            return self.findMin(nums[:mid])
