## [Leetcode#565] Array Nesting
#
#
#
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums_appear = set({})
        ## note: not just simply run resurrsion, time will exceed.
        ## as long as the num appeared, we got to save and not need to do DFS.
        
        max_len = -float('inf')
        for i in range(len(nums)):
            if nums[i] not in self.nums_appear:
                max_len = max(max_len, self.DFS(nums[i], nums, set({})))        
            
        return max_len
            
            
    def DFS(self, num, nums, nums_set):
        if num in nums_set: return len(nums_set)
        nums_set.add(num)
        self.nums_appear.add(num)
        return self.DFS(nums[num], nums, nums_set)