## [#169] Majority Element
#   
#  zenefit, Adobe
#
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = {}
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1
            
        return [x for x in num_dict if num_dict[x] > len(nums)/2][0]