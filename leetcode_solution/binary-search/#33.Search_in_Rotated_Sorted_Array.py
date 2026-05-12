#  33. Search in Rotated Sorted Array (medium)
#  https://leetcode.com/problems/search-in-rotated-sorted-array/   
#
#  Facebook, LinkedIn, Microsoft, Bloomberg, Uber
#
dclass Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) <= 3:  # if only three elements are left, directly check
            if target not in nums: return -1
            return [i for i in range(len(nums)) if nums[i] == target][0]
        
        mid = len(nums) // 2
        
        if nums[mid] == target:
            return mid
        else:
            if nums[0] < nums[mid]:  # pivot is on right hand side, e.g. [2,4,5,6,7,0,1]
                if nums[0] <= target < nums[mid]:
                    return self.search(nums[:mid], target)
                else:
                    x = self.search(nums[mid+1:], target)
                    return x + mid + 1 if x != -1 else -1
            else:                    # pivot is on left hand side, e.g. [7,0,1,2,4,5,6]
                if nums[mid] < target <= nums[-1]:
                    x = self.search(nums[mid+1:], target)
                    return x + mid + 1 if x != -1 else -1
                else:
                    return self.search(nums[:mid], target)
