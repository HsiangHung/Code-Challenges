#  997. Find the Town Judge (easy)
#  https://leetcode.com/problems/find-the-town-judge/
#
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        if N == 1: return 1
        
        trusted = {}
        trusting = set({})
        for a, b in trust:
            trusted[b] = trusted.get(b, []) + [a]
            trusting.add(a)
            
        for judge in trusted:
            if len(set(trusted[judge])) == N-1 and judge not in trusting: 
                return judge
            
        return -1