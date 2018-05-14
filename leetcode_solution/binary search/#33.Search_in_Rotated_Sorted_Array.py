## [#33] Search in Rotated Sorted Array
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
        if len(nums) == 0: return -1
        
        if len(nums) == 1:
            if nums[0] != target: return -1
            return 0
        
        mid = len(nums) // 2
        head, end = nums[0], nums[-1]
        if nums[mid] == target:
            return mid
        elif head == target:
            return 0
        elif end == target:
            return len(nums)-1
        
        if head > nums[mid]:  # when pivot is on left hand side, i.e. [7,0,1,2,3,4,5]
            if nums[mid] < target < end:
                offset, index = mid+1, self.search(nums[mid+1:], target)
            else:
                offset, index = 0, self.search(nums[: mid], target)
        elif nums[mid] > end:  # when pivot is on right hand side, i.e. [2,3,4,5,7,0,1]
            if head < target < nums[mid]:
                offset, index = 0, self.search(nums[: mid], target)
            else:
                offset, index = mid+1, self.search(nums[mid+1:], target)
        else:   # when the list is in order without any rotation, i.e. [0,1,2,...5,7]
            if nums[mid] > target:
                offset, index = 0, self.search(nums[: mid], target)
            else:
                offset, index = mid+1, self.search(nums[mid+1:], target)

        if index < 0: return -1
        return offset + index