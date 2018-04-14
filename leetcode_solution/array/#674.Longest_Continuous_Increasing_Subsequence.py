# [#674] Longest Continuous Increasing Subsequence
#
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []: return 0
        
        max_seq, seq = 1, 1
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                seq += 1
            else:
                max_seq = max(max_seq, seq)
                seq = 1
                                
        return max(seq, max_seq)