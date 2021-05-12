#  1366. Rank Teams by Votes (medium)
#  https://leetcode.com/problems/rank-teams-by-votes/
#
class Solution:
    '''
    https://blog.csdn.net/qq_37821701/article/details/112131189
    '''
    def rankTeams(self, votes: List[str]) -> str:
        
        ranks = {v:[0]*len(votes[0])+[v] for v in votes[0]}
        for vote in votes:
            for i,c in enumerate(vote):
                ranks[c][i] -= 1;
        
        # e.g. ranks = {'A': [-5, 0, 0, 'A'], 'B': [0, -2, -3, 'B'], 'C': [0, -3, -2, 'C']} now

        tmp = list(votes[0])  ## ["A", "B", "C"]
        
        tmp.sort(key = lambda x:ranks[x]) 
        # so [-5,0,0,'A'] < [0,-3,-2,'C'] < [0,-2,-3,'B']. 
        # if {'A':[-1,-1,'A'], 'B':[-1,-1,'B']} -> [-1,-1,'A'] < [-1,-1,'B']
        return "".join(tmp)
