#  153. Find Minimum in Rotated Sorted Array (medium)
#  https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return min(nums)
        
        mid = len(nums) // 2
        
        if nums[mid+1] < nums[mid]: return nums[mid+1]
        
        if nums[mid] < nums[0]:
            return self.findMin(nums[:mid+1])
        elif nums[-1] < nums[mid]:
            return self.findMin(nums[mid:])
        elif nums[0] < nums[mid] < nums[-1]:
            return nums[0]
