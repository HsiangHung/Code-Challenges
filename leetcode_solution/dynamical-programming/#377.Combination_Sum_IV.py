#  377. Combination Sum IV (medium)
#  https://leetcode.com/problems/combination-sum-iv/
#
class Solution:
    '''
    https://www.cnblogs.com/grandyang/p/5705750.html
    '''
    def combinationSum4(self, nums: List[int], target: int) -> int:
        min_val = min(nums)     
        if min_val > target: return 0
        
        nums = [x for x in nums if x <= target]
        
        dp = {0: 1, min_val: 1}
        n = min_val
        while n < target:
            n += 1
            for x in nums:
                if n - x in dp:
                    dp[n] = dp.get(n, 0) + dp[n-x]            
            
        return dp[target]