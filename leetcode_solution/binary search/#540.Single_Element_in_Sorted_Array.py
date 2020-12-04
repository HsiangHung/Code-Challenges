#  540. Single Element in a Sorted Array (medium)
#  https://leetcode.com/problems/single-element-in-a-sorted-array/
#
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        '''
        TC O(logn) solution
        http://bookshadow.com/weblog/2017/03/11/leetcode-single-element-in-a-sorted-array/
        
        nums = left + right = [:mid] + [mid+1:]
        
        if left is even (right is odd):
            nums[mid] == nums[mid-1], meaning no unqie in the left, search nums[mid+1:] 
            nums[mid] != nums[mid-1], meaning the unqie in the left, search nums[:mid] (to make sure left odd)
            
        if left is odd (right is even):
            nums[mid] == nums[mid-1], meaning the unqie in the left, search nums[:mid+1]
            nums[mid] != nums[mid-1], meaning no unqie in the left, search nums[mid:] (to make sure right odd)
        '''
        if len(nums) == 1: return nums[0]
        if len(nums) == 3:
            return nums[0] if nums[1] == nums[2] else nums[2]
        
        mid = len(nums) // 2
        
        if len(nums[:mid+1]) % 2 == 1:
            if nums[mid] == nums[mid-1]:
                return self.singleNonDuplicate(nums[:mid+1])
            else:
                return self.singleNonDuplicate(nums[mid:])
        else:
            if nums[mid] == nums[mid-1]:
                return self.singleNonDuplicate(nums[mid+1:])
            else:
                return self.singleNonDuplicate(nums[:mid])