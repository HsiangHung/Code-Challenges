# # 209. Minimum Size Subarray Sum
#
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        '''
        use dual pointer starting from i=j=0, 
        if subarray < s, move j toward right; if subarray >= s, move i toward right
        https://medium.com/@lenchen/leetcode-209-minimum-size-subarray-sum-ab92c2de4e94
        '''
        if nums == []: return 0
        
        min_size = 2**31
        
        i , j = 0, 0
        sum_sub, size_sub =nums[i], 1
        while i <= len(nums)-1 and j <= len(nums)-1:
            if sum_sub >= s:
                min_size = min(min_size, size_sub)
                size_sub -= 1
                sum_sub -= nums[i] 
                i += 1
            else:
                j += 1
                if j <= len(nums)-1:
                    size_sub += 1
                    sum_sub += nums[j]
                
        
        if min_size == 2**31:
            return 0
        else:
            return min_size
            
            