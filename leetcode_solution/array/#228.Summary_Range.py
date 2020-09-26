# # 228. Summary Range
#
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if nums == []: return []
        
        output = []
        
        ranges = []
        for i in range(len(nums)):
            if ranges == []:
                ranges.append(nums[i])
            else:
                if nums[i] == nums[i-1]+1:
                    ranges.append(nums[i])
                else:
                    if len(ranges) > 1:
                        output.append(str(ranges[0])+"->"+str(ranges[-1]))
                    elif len(ranges) == 1:
                        output.append(str(ranges[0]))
                    ranges = [nums[i]]
        
        if len(ranges) > 1:
            output.append(str(ranges[0])+"->"+str(ranges[-1]))
        else:
            output.append(str(ranges[0]))
            
        return output
        