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
        
        a, b, c = nums[0], nums[mid], nums[-1]
        
        if b == target: return mid
        if a  == target: return 0
        if c == target: return len(nums)-1
        
        if b > a:       # when pivot is on the left, i.e. [1,2,4,5,7,0,1]
            if  b > target > a:
                return self.search(nums[:mid], target)
            else:
                idx = self.search(nums[mid:], target)
                return mid + idx if idx != -1 else -1
        elif c > b:     # when pivot is on the right, i.e. [7,0,1,2,3,4,5]
            if c > target > b:
                idx = self.search(nums[mid:], target)
                return mid + idx if idx != -1 else -1
            else:
                return self.search(nums[:mid], target)
