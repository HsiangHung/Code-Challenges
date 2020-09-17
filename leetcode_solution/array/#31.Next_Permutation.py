# #31. Next Permutation
#
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        https://www.youtube.com/watch?v=quAS1iydq7U
        case analysis: Time O(n), Space O(1)
        e.g [6,2,1,5,4,3,2,0] 
        find the strict decreasing sequence starting from right, [5,4,3,2,0] here
        switch 1 and the smallest number but greater than 1 in the sequence, which is 
        2. [6,2,1,5,4,3,2,0] -> [6,2,2,5,4,3,1,0] and then sort [5,4,3,1,0] as increasing
        -> [6,2,2,0,1,3,4,5]
        """
        
        if len(nums) <= 1: return nums
        
        i = len(nums)-1
        while nums[i-1] >= nums[i] and i >= 0:
            i -= 1
        
        if i <= 0:  ## like [3,2,1] or [1,1,1], no need to change (all non-increaing seq)
            nums[:] = nums[::-1]  ## NOTE: if here nums = nums[::-1] doesn't work
        else:
            swap_num1 = nums[i-1]

            j = len(nums)-1
            while nums[j] <= swap_num1:
                j -= 1

            swap_num2 = nums[j]

            nums[i-1], nums[j] = swap_num2, swap_num1
            nums[i:] = nums[i:][::-1]  # reverse the non-increasing sequence
