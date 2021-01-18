#  90. Subsets II (medium)
#  https://leetcode.com/problems/subsets-ii/
#
class Solution:
    '''
    first find the possible array index combination, and then use tuple to store [1,2,2] as (1,2,2)
    '''
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return [[]]
        
        nums_dict = {}
        for i, num in enumerate(nums):
            nums_dict[i] = num
            
        dp = {0: [[]]}
        
        i = 1
        while i <= len(nums):
            dp[i] = []
            for x in dp[i-1]:
                for j in range(len(nums)):
                    if j not in x:
                        new_x = sorted(x + [j])
                        if new_x not in dp[i]: dp[i].append(new_x)
            i += 1
            
        ans = []
        for i in dp:
            subset = set({})
            for arr in dp[i]:
                subset.add(tuple(sorted([nums_dict[y] for y in arr])))
            ans += list(subset)
                
        return ans