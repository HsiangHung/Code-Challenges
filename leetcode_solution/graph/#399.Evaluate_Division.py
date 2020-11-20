# 399. Evaluate Division (medium)
# https://leetcode.com/problems/evaluate-division/
#
#
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        using graph, 
        http://bookshadow.com/weblog/2016/09/11/leetcode-evaluate-division/
        when creating graph, running through all possible edges
        then we can easily perform queries.
        '''
        edges = {}
        for eq, val in zip(equations, values):
            if eq[0] in edges:
                edges[eq[0]][eq[1]] = val
            else:
                edges[eq[0]] = {eq[1]: val}
            
            if eq[1] in edges:
                edges[eq[1]][eq[0]] = 1/val
            else:
                edges[eq[1]] = {eq[0]: 1/val}
        
        for x in edges:
            edges[x][x] = 1.0
            for n1 in edges:
                for n2 in edges:
                    if x in edges[n1] and x in edges[n2]:
                        edges[n1][n2] = edges[n1][x]*edges[x][n2]
                        
        ans = []
        for query in queries:
            a, b = query[0], query[1]
            ans.append(edges[a][b] if a in edges and b in edges[a] else -1)
            
        return ans