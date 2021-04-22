#  81. Search in Rotated Sorted Array II (medium)
#  https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
#
class Solution:
    '''
    http://bangbingsyb.blogspot.com/2014/11/leetcode-search-in-rotated-sorted-array.html

    eg1: nums = [2,2,2,0,1], target = 0
    eg2: nums = [1,0,1,1,1,1], target = 0

    while start == mid, search nums[1:]
          mid == end, search nums[:-1] 
    worse time complexity could be O(n)
    '''
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) <= 3:  # if only three elements are left, directly check
            if target not in nums: return False
            return True
        
        mid = len(nums) // 2
        
        a, b, c = nums[0], nums[mid], nums[-1]
        
        if target in (a, b, c): return True
        
        # ----- here is the different part compared to #33, start
        if b == c:
            return self.search(nums[:-1], target)
        elif a == b:
            return self.search(nums[1:], target)
        # ----- here is the different part compared to #33, end
        
        if a < b:       # when pivot is on the left, i.e. [1,2,4,5,7,0,1]
            if  a <= target < b:
                return self.search(nums[:mid], target)
            else:
                return self.search(nums[mid:], target)
        elif b < c:     # when pivot is on the right, i.e. [7,0,1,2,3,4,5]
            if b <= target < c:
                return self.search(nums[mid:], target)
            else:
                # print (nums[:mid])
                return self.search(nums[:mid], target)