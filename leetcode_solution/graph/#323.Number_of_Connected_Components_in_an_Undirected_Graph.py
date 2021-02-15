#  323. Number of Connected Components in an Undirected Graph (medium)
#  https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
#
class Solution:
    '''
    graph problem. establish edges, and then DFS to update labels on each nodes.
    
    NOTE, at the first glance, we can use merge set-union to do it.
    But first always sorted edges based on a on [a, b], and make sure a < b.
    '''
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        edges_dict = {}
        for i in range(len(edges)):
            edges_dict[edges[i][0]] = edges_dict.get(edges[i][0], []) + [edges[i][1]]
            edges_dict[edges[i][1]] = edges_dict.get(edges[i][1], []) + [edges[i][0]]
            
        labels = [-1]*n
        tag = -1
        for i in range(n):
            if labels[i] == -1:
                tag += 1
                self.DFS(i, tag, labels, edges_dict)
                
        return len(set(labels))
    
    
    def DFS(self, i, tag, labels, edges_dict):
        if labels[i] != -1: return
        
        labels[i] = tag
        
        if i in edges_dict:
            for j in edges_dict[i]:
                self.DFS(j, tag, labels, edges_dict)
                
                
                
    