## [Leetcode80] Remove Duplicates from Sorted Array II
##
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        just need a O(1) space to record duplication index.
        if the index >=2, means repeat more than one time.
        '''
        duplicate = 0
        index = 0
        for i in range(len(nums)):
            if duplicate == 0:
                duplicate = 1
                index += 1
            else:
                if nums[index] == nums[index-1]:
                    if duplicate == 1:
                        duplicate = 2
                        index += 1
                    elif duplicate >= 2:
                        nums.pop(index)
                else:
                    duplicate = 1
                    index += 1
            

        return len(nums)