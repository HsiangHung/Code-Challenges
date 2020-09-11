# #40. Combination Sum II
#
class Solution:
    def __init__(self):
        self.sol_set = []
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        for num in candidates:
            if num > target:
                candidates.remove(num)
        
        self.DFS(candidates, [], target)
        
        return self.sol_set
        
        
    def DFS(self, candidates, sol_set, target):
        
        if target == 0 and len(sol_set) > 0:
            if sorted(sol_set) not in self.sol_set:
                self.sol_set.append(sorted(sol_set))
            return
        elif target < 0:
            return
            
        for i in range(len(candidates)):
            self.DFS(candidates[i+1:], sol_set+[candidates[i]], target-candidates[i])
            