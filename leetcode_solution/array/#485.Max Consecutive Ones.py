# [#485] Max Consecutive Ones
#
#
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0] == 1:
            seq = 1
        else:
            seq = 0

        max_seq = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                if nums[i] == 1:
                    seq += 1
            else:
                if nums[i] == 1:
                    seq = 1
                else:
                    max_seq = max(max_seq, seq)
                    seq = 0
                    
        return max(max_seq, seq)