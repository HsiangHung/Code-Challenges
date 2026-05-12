# 47. Permutations II (medium)
# https://leetcode.com/problems/permutations-ii/
#
class DFSSolution:
    '''
    DFS solutions, need to sort first, and then divide and conque
    when duplicated number, skip until different one.
    run time beats 50%!
    '''
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        return self.DFS(nums)
        
    def DFS(self, nums):
        if len(nums) == 0: return []
        if len(nums) == 1: return [[nums[0]]]
        ans = []
        i = 0
        while i <= len(nums)-1:
            sol = self.permuteUnique(nums[:i] + nums[i+1:])
            for item in sol:
                ans.append([nums[i]]+item)
                
            i += 1
            while i <= len(nums)-1 and nums[i] == nums[i-1]:
                i += 1
                
        return ans


class DPSolution:
    '''
    DP solutions, runtime only beats 19%
    '''
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
            
    