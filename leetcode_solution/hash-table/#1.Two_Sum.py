## [Leetcode#1] Two Sum
#
#  facebook, microsoft, uber, bloomberg.... many
#
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = [i]
            else:
                nums_dict[nums[i]].append(i)
            
        for num in nums:
            if target - num in nums_dict and num != target - num:
                return [nums_dict[num][0], nums_dict[target-num][0]]
            elif target - num == num and len(nums_dict[num]) > 1:
                return nums_dict[num]