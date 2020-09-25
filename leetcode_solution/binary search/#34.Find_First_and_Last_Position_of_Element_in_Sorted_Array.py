# # 34. Find First and Last Position of Element in Sorted Array
#
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 0: return [-1, -1]
                    
        self.range = set({})
        
        self.search(nums, target, 0)
        
        if len(self.range) == 0: return [-1, -1]
        
        return [min(self.range), max(self.range)]
        
        
    def search(self, nums, target, offset):
        
        if nums == []: return
        
        if len(nums) == 1:
            if nums[0] == target: self.range.add(offset) ## trick, need to consider one nums
            return

        if len(nums) == 2:       
            if nums[0] == target: self.range.add(offset)  ## need to consider two nums too
            if nums[1] == target: self.range.add(offset+1)
            return
        
        middle = int(len(nums)/2)
        if nums[middle] == target:
            self.range.add(offset + middle)
            if nums[middle-1] == target:     # if nums[middle-1], also need to search left
                self.search(nums[: middle], target, offset)

            if nums[middle+1] == target:     # if nums[middle+1], also need to search right
                self.search(nums[middle+1:], target, offset+middle+1)

        elif nums[middle] > target:
            self.search(nums[: middle], target, offset)
        elif nums[middle] < target:
            self.search(nums[middle:], target, offset+middle)
