#  46. Permutations (medium)
#  https://leetcode.com/problems/permutations/
#
#  Microsoft, LinkedIn
#
class DFSSolution:
    '''
    DFS solution, runtime beats 60%, but code also looks concise
    https://www.cnblogs.com/grandyang/p/4358848.html
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return []
        if len(nums) == 1: return [[nums[0]]]
        
        ans = []
        for i in range(len(nums)):            
            sol = self.permute(nums[:i] + nums[i+1:])
            for item in sol:
                ans.append([nums[i]] + item)

        return ans
            


class DPSolution(object):
    '''
    dynamical programming solutions, runtime beats 89%
    '''
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dp = {0: [[nums[0]]]}
        
        it = 1
        while it < len(nums):
             
            dp[it] = []
            for x in dp[it-1]:
                for i in range(len(x)+1): # note, loop through to len(x)+1
                    dp[it].append(x[:i]+[nums[it]]+x[i:])

            it += 1
        
        return dp[len(nums)-1]