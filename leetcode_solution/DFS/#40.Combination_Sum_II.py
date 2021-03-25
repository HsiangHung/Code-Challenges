#  40. Combination Sum II (medium)
#  https://leetcode.com/problems/combination-sum-ii/
#
class Solution:
    '''
    the number can be repeated, but if same number, skip: i -> i+1
    set up a sethash to avoid duplication
    '''
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:        
        candidates = sorted(candidates)
        return self.DFS(candidates, target)
    
    def DFS(self, candidates, target):
        if len(candidates) == 0 or target <= 0: return []
                
        ans = []
        i = 0
        while i <= len(candidates)-1 and candidates[i] <= target:
            if candidates[i] == target:
                ans.append([candidates[i]])
            else:
                sol = self.DFS(candidates[i+1:], target-candidates[i])
                for x in sol:
                    if x[0] >= candidates[i]:
                        ans.append([candidates[i]]+x)
            i += 1
            while i <= len(candidates)-1 and candidates[i] == candidates[i-1]: # trick, need to move index
                i += 1
            
        ans = set([tuple(x) for x in ans])
        return [list(x) for x in ans]