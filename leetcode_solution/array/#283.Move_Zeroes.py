#
# 283. Move Zeroes
#
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n_non_zero = len([x for x in nums if x != 0])
        # doing this can save time to run num_non_zero only
        # e.g [0, 0, 1, 0, 0, 0, 0, 0, 0....] we only need to run until 1 once.

        i = 0
        while i < n_non_zero:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i += 1
