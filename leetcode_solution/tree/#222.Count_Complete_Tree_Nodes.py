# [#222] Count Complete Tree Nodes
#
#
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        max_depth = self.get_depth(root)
        
        total_numNodes, level_numNodes = 0, 1
        for h in range(max_depth-1):
            total_numNodes += level_numNodes
            level_numNodes *= 2
            
        return total_numNodes + self.traversal(1, max_depth, root)[0]
        
        
    def traversal(self, depth, max_depth, root):
        '''This method doing DFS search until the leaf node's depth is no longer equal to the max depth
           since a complete binary tree must fill each level; except in the last level fills leftmost nodes only
        '''
        if not root.left and not root.right: 
            if depth == max_depth:
                return 1, True
            else:
                return 0, False
        
        numNodes_lastLevel = 0
        if root.left:
            numNodes, isDFS = self.traversal(depth + 1, max_depth, root.left)
            numNodes_lastLevel += numNodes            

        if not isDFS: return numNodes_lastLevel, False
        
        if root.right:
            numNodes, isDFS = self.traversal(depth + 1, max_depth, root.right)
            numNodes_lastLevel += numNodes

        return numNodes_lastLevel, isDFS
            
    
    def get_depth(self, root):
        if not root.left and not root.right: return 1
        if root.left:
            return self.get_depth(root.left) + 1
        
    def naiveCountNodes(self, root):
        """
        This naive node-count method will definitely exceed the time limit. 
        """
        if not root: return 0
        numNode = 1
        if root.left: numNode += self.countNodes(root.left)
        if root.right: numNode += self.countNodes(root.right)
        return numNode
    
