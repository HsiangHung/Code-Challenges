#  39. Combination Sum (medium)
#  https://leetcode.com/problems/combination-sum/  
#
# Uber, Snapchat
#
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if candidates == [] or min(candidates) > target: return []
        
        sol = []
        for num in candidates:
            if num == target:
                sol.append([num])
            else:
                sol_set = self.combinationSum(candidates, target-num)
                if len(sol_set) > 0:
                    for x in sol_set:
                        possible_sum = sorted([num]+x)
                        if possible_sum not in sol:
                            sol.append(possible_sum)
        return sol