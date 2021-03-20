#  39. Combination Sum (medium)
#  https://leetcode.com/problems/combination-sum/  
#
# Uber, Snapchat
#
class Solution(object):
    '''
    e.g. target = 7, and candidates = [2,3,4,7], 
    [3,2,2] and [2,3,2] are solutions, but only show [2,2,3]
    '''
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0 or target <= 0: return []
        if min(candidates) > target: return []
        
        ans = []
        for i in range(len(candidates)):
            if candidates[i] == target:
                ans.append([candidates[i]])
            else:
                sol = self.combinationSum(candidates, target-candidates[i])
                for x in sol:
                    if candidates[i] <= x[0]:  ## to make sure non-repeated
                        comb = [candidates[i]] + x
                        ans.append(comb)
                
        return ans