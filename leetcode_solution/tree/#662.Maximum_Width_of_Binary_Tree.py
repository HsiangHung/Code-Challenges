# [#662] Maximum Width of Binary Tree
#
#
#
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #  horizontal axis evolution:
        #                            0          
        #              -1            0           1        
        #        -3          -1      0     1           3
        #    -7      -5    -3   -1   0   1    3     5      7 
        # -15 -13 -11 -9 -7 -5 -3 -1 0  1 3  5 7   9 11  13 15
        #
        if not root: return 0
        self.level_nodes = {0: set({0})}
        self.traversal(1, 0, root.left, root.right)
        max_width = max([max(self.level_nodes[depth])-min(self.level_nodes[depth]) for depth in self.level_nodes])
        return max_width/2+1
        
        
    def traversal(self, depth, x, left, right):
        if not left and not right:
            return
        
        if depth not in self.level_nodes:
            self.level_nodes[depth] = set({})

        if left:
            self.level_nodes[depth].add(x-1)
            self.traversal(depth+1, 2*(x-1), left.left, left.right)
            
        if right:
            self.level_nodes[depth].add(x+1)
            self.traversal(depth+1, 2*(x+1), right.left, right.right)
        
    def traversal(self, height, depth, root):
        if height <= 0: return
        
        if root is not None:
            node = str(root.val)
        else:
            node = ''
        
        if len(self.level_nodes) < depth:
            self.level_nodes.append([node])
        else:
            self.level_nodes[depth-1].append(node)
  
        if root and root.left:
            self.traversal(height-1, depth+1, root.left)
        else:
            self.traversal(height-1, depth+1, None)
            
        if root and root.right:
            self.traversal(height-1, depth+1, root.right)
        else:
            self.traversal(height-1, depth+1, None)
        
    
    def get_maximal_depth(self, root):
        if not root.left and not root.right: return 1
        depth = 0
        if root.left:
            depth = self.get_maximal_depth(root.left) + 1
        if root.right:
            depth = max(depth, self.get_maximal_depth(root.right)+1)
        return depth
    