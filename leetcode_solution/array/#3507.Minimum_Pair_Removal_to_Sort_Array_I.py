"""
[Leetcode 3507.] Minimum Pair Removal to Sort Array I
https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/description/?envType=problem-list-v2&envId=doubly-linked-list
"""
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        if not nums:
            return 0

        def pair_adj(nums):
            i, non_desc = 0, True
            min_adj_sum, min_adj_sum_index = 10**5, 0

            while i < len(nums) - 1:
                if nums[i] + nums[i+1] < min_adj_sum:
                    min_adj_sum = nums[i] + nums[i+1]
                    min_adj_sum_index = i
                if nums[i+1] < nums[i]:
                    non_desc = False 
                i += 1
            
            return non_desc, min_adj_sum_index, min_adj_sum

        non_desc, min_adj_sum_index, min_adj_sum = pair_adj(nums)
        replacement = 0
        while not non_desc:
            nums.pop(min_adj_sum_index + 1)
            nums.pop(min_adj_sum_index)
            nums.insert(min_adj_sum_index, min_adj_sum)
            non_desc, min_adj_sum_index, min_adj_sum = pair_adj(nums)
            replacement += 1

        return replacement


