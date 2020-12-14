# 133 Clone Graph (medium)
# https://leetcode.com/problems/clone-graph/
# 
# Uber
#
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.visited = {}
    
    def cloneGraph(self, node):
        '''
        ref: https://www.jiuzhang.com/solution/clone-graph/#tag-highlight-lang-python
        '''        
        if not node: return
        if node in self.visited: return self.visited[node]
        
        node2 = Node(val=node.val)
        self.visited[node] = node2
                
        for neighbor in node.neighbors:
            node2.neighbors.append(self.cloneGraph(neighbor))
                
        return node2
        