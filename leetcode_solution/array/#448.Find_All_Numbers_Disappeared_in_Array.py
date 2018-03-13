# [#448] Find All Numbers Disappeared in an Array
#
# without extra O(n) space and time complexity O(n)
#
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_len = len(nums)
        nums = set(nums)
        missing_nums = []
        for i in range(1, nums_len+1):
            if i not in nums:
                missing_nums.append(i)
                
        return missing_nums