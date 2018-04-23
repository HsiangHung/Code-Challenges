## [#581] Shortest Unsorted Continuous Subarray
#
#  Google
#
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        start, end = None, None
        for i in range(len(sorted_nums)):
            if nums[i] != sorted_nums[i] and start == None:
                start = i
                break
                
        for i in range(len(sorted_nums)-1, -1, -1):
            if end == None and nums[i] != sorted_nums[i]:
                end = i
                break
    
        if start == None and end == None: return 0
        return end-start+1