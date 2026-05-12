#  213. House Robber II (medium)
#  https://leetcode.com/problems/house-robber-ii/
# 
#
class Solution(object):
    '''
    two dp array: 'dp' includes first element, and 'no_first' not includes first elements
    
    eventually compare max(no_first[-2] + nums[-1], no_first[-1], dp[-1])
    '''
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) <= 2: return max(nums)
        
        dp = [nums[0], max(nums[:2])]
        no_first = [0, nums[1]]
        
        for i in range(2, len(nums)-1):
            dp.append(max(dp[i-2]+nums[i], dp[i-1]))
            no_first.append(max(no_first[i-2]+nums[i], no_first[i-1]))
            
        return max(no_first[-2]+nums[-1], no_first[-1], dp[-1])