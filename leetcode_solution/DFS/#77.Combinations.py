#  77. Combinations (medium)
#  https://leetcode.com/problems/combinations/
#
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        candidates = [i+1 for i in range(n)]
        return self.DFS(candidates, k)

    
    def DFS(self, candidates, k):
        if len(candidates) == 0: return []
        
        if k == 1:
            ans = []
            for x in candidates:
                ans.append([x])
            return ans 
        else:
            ans =set({})
            for i in range(len(candidates)):
                sol = self.DFS(candidates[i+1:], k-1)
                for x in sol:
                    ans.add(tuple([candidates[i]]+x))

            return [list(x) for x in ans]