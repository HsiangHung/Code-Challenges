#  34. Find First and Last Position of Element in Sorted Array (medium)
#  https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
#
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1, -1]
        return [self.left(nums, target), self.right(nums, target)]
        
        
    def left(self, nums, target):
        if len(nums) <= 3:
            if target not in nums: return -1
            for i in range(len(nums)):
                if nums[i] == target: return i
        
        mid = len(nums) // 2
        if nums[mid-1] < target and nums[mid] == target:
            return mid
        elif nums[mid] < target and nums[mid+1] == target:
            return mid+1
        else:
            if nums[mid] >= target:
                x = self.left(nums[:mid], target)
                return x if x != -1 else -1
            else:
                x = self.left(nums[mid+1:], target)
                return mid + x + 1 if x != -1 else -1
        
    def right(self, nums, target):
        if len(nums) <= 3:
            if target not in nums: return -1
            for i in range(len(nums)-1, -1, -1):
                if nums[i] == target: return i
        
        mid = len(nums) // 2
        if nums[mid] == target and nums[mid+1] > target:
            return mid
        elif nums[mid-1] == target and nums[mid] > target:
            return mid-1
        else:
            if nums[mid] > target:
                x = self.right(nums[:mid], target)
                return x if x != -1 else -1
            else:
                x = self.right(nums[mid+1:], target)
                return mid + x + 1 if x != -1 else -1