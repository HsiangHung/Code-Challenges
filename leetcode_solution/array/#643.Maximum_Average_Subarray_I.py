# [#643] Maximum Average Subarray I
#
#  not find the mean value everytime. update the sum in each iteration
#
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        if k > len(nums): return float(sum(nums))/len(nums)
        
        max_sum = sum(nums[:k])
        current_sum = max_sum
        
        start, end = 1, k
        while end <= len(nums)-1:
            current_sum = current_sum + nums[end] - nums[start-1]
            max_sum = max(max_sum, current_sum)
            start += 1
            end += 1
            
        return float(max_sum)/k