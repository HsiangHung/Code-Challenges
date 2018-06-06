## [Leetcode#75] Sort Colors
#
# FB, MS
#
#
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #
        # idea: always move '0' to head, and pull '2' to the end.
        #       if '1', just move the pointer without doing anything
        #
        nums_len = len(nums)
        idx = 0
        for i in range(nums_len):
            if nums[idx] == 0 and idx > 0:
                nums.pop(idx)
                nums.insert(0, 0)
                idx += 1
            elif nums[idx] == 2 and idx < nums_len-1:
                nums.pop(idx)
                nums.append(2)
            else:
                idx += 1
          