# 1060. Missing Element in Sorted Array
#
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        '''
        first count number of missing numbers in the "nums" list
        if k > the number of missing numbers, the missing appears outside the list
        if not, search missing number within the "nums" list.
        e.g. nums = [4,7,9,10]. missing 5,6,8,
             if k= 5, then start from 11, 12
        '''
        num_within = nums[-1] - nums[0] - 1 - (len(nums) - 2)
        
        if k > num_within:
            return k - num_within + nums[-1]
        else:
            i = 0
            while i < len(nums) and k > 0:
                num_within = nums[i+1] - nums[i] - 1
                if k > num_within:
                    k -= num_within
                    i += 1
                else:
                    return k + nums[i]