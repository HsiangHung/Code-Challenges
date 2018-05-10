## [Leetcode#133] Clone Graph
##
## Uber
##
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.dict = {}
    
    def cloneGraph(self, node):
        '''ref: https://www.jiuzhang.com/solution/clone-graph/#tag-highlight-lang-python'''
        if not node: return None
        if node.label in self.dict: return self.dict[node.label]
        
        newNode = UndirectedGraphNode(node.label)
        neighbors = node.neighbors
        
        self.dict[node.label] = newNode
        
        for neighbor in neighbors:
            newNode.neighbors.append(self.cloneGraph(neighbor))
                
        print newNode.neighbors
        
        return newNode
        
        
        