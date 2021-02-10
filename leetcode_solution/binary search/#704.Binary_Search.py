#  704. Binary Search (easy)
#  https://leetcode.com/problems/binary-search/
#
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return -1
        if len(nums) == 1: return 0 if nums[0] == target else -1
        
        mid = len(nums) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            idx = self.search(nums[:mid], target)
            return idx if idx >= 0 else -1
        else:
            idx = self.search(nums[mid+1:], target)
            return mid + 1 + idx if idx >= 0 else -1