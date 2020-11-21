# 47. Permutations II (medium)
# https://leetcode.com/problems/permutations-ii/
#
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        the part different from Permutations I is here we have duplciated number.
        Everytime when building combination, check if exists duplications.
        '''
        dp = {1: [[nums[0]]]}
        
        i = 1
        while i <= len(nums)-1:
            i += 1
            
            dp[i] = []
            
            for x in dp[i-1]:
                for j in range(len(x)):
                    if x[:j]+[nums[i-1]]+x[j:] not in dp[i]: # here is different from no-duplicated number. you always need to check if there is duplicated combination
                        dp[i].append(x[:j]+[nums[i-1]]+x[j:])
                    
                if x+[nums[i-1]] not in dp[i]:               
                    dp[i].append(x+[nums[i-1]])
        
        return dp[len(nums)]
            
    