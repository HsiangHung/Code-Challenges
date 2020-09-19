# #162. Find Peak Element
#
#
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        
        peak = []
        
        i = 0
        while i <= len(nums)-1:
            if i == 0:
                if nums[0] > nums[1]:
                    peak.append(i)
            elif i == len(nums)-1:
                if nums[i-1] < nums[i]:
                    peak.append(i)
            else:
                if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                    peak.append(i)
            i += 1
        
        return peak[0]