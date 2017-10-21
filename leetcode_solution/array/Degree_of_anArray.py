## [Leetcode#697] Degree of an Array
##
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_pos = {}
        for i in range(len(nums)):
            if nums[i] not in num_pos:
                num_pos[nums[i]] = [i]
            else:
                num_pos[nums[i]].append(i)
                
        max_freq = max([len(num_pos[num]) for num in num_pos])
                
        min_degree = len(nums)
        for num in num_pos:
            freq = len(num_pos[num])
            if freq == max_freq:
                min_degree = min(min_degree, num_pos[num][-1]-num_pos[num][0]+1)
            
        return min_degree
        