#  532. K-diff Pairs in an Array (medium)
#  https://leetcode.com/problems/k-diff-pairs-in-an-array/
#
class Solution:
    '''
    unique pairs, 
    so if k == 0, ad hoc: count # of num which appears > 1 time. 
    otherwise use two pointer. Make sure if repeated number, move on i or j
    '''
    def findPairs(self, nums: List[int], k: int) -> int:
        
        if k == 0:
            num_dict = {}
            for num in nums:
                num_dict[num] = num_dict.get(num, 0) + 1
            return len([num for num in num_dict if num_dict[num] > 1])
        
        nums = sorted(nums)
        
        ans = 0
        i, j = 0, 1
        while i <= len(nums)-1 and j <= len(nums)-1:
            if nums[j] - nums[i] == k:
                ans += 1
                i = self.dedup(i+1, nums)
            elif nums[j] - nums[i] > k:
                i = self.dedup(i+1, nums)
            else:
                j = self.dedup(j+1, nums)
                    
        return ans
    
    def dedup(self, i, nums):
        while i <= len(nums) -1 and nums[i] == nums[i-1]:
            i += 1
        return i