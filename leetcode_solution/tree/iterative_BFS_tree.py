# BFS for tree iterative traversal
#
#
class Solution(object):
    def BFSTrees(self, root):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not root: return []
        
        max_depth = self.get_max_depth(root)-1
        
        traversal = []
        
        nodeStack = [root]
        depth = 1
        num_node = 1
        
        while depth <=  max_depth:

            for i in range(num_node):
                node = nodeStack[0]
                del nodeStack[0]
            
                if node:
                    traversal.append(node.val)
                    #print node.val
                
                    if node.left != None and node.right != None:
                        nodeStack += [node.left, node.right]
                    elif node.left != None:
                        nodeStack += [node.left, None]
                    elif node.right != None:
                        nodeStack += [None, node.right]
                    else:
                        nodeStack += [None, None]
                    
                else:
                    traversal.append(0)
                    #print 0
                    nodeStack += [None, None]
                
            depth += 1
            num_node = num_node*2
        
        print traversal
            
        
    def get_max_depth(self, root):
        if not root.left and not root.right:
            return 0
        
        max_depth = 0
        if root.left:
            max_depth = max(self.get_max_depth(root.left)+1, max_depth+1)
            
        if root.right:
            max_depth = max(self.get_max_depth(root.right)+1, max_depth+1)
            
        return max_depth
        