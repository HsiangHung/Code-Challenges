# [# 287] Find the Duplicate Number
#  
#  Bloomberg  
#
# use the clever approach: https://segmentfault.com/a/1190000003817671
#  or https://leetcode.com/articles/find-the-duplicate-number/
#
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        slow = nums[0]
        fast = nums[nums[0]]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return fast
        