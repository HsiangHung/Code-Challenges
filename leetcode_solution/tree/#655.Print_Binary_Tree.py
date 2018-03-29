# [#655] Print Binary Tree
#
#
#
class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        # I feel this is very hard, I first do DFS to collect all nodes even None 
        # at each level. We can sweep to find maximal height to know height of the tree.
        # e.g. self.level_nodes = [[1],['',2], ['','','',3]....]
        # and insert one '' between each element for all levels
        # but lowest level  x -> x,
        #     second lowest x -> '', x, '' (2**0 '')
        #     third lowest  x -> '','','',x,'','',''  (2**0+2**1 '')
        #     four lowest   x -> '','',..'',x, '',... ''  (1+2+2**2 '') 
        #
        max_depth = self.get_maximal_depth(root)
        self.level_nodes = []
        self.traversal(max_depth, 1, root)
        return self.node_print()
    
    def node_print(self):
        self.level_nodes = self.level_nodes[::-1]
        num_space = 0
        for i in range(len(self.level_nodes)):
            lst = self.level_nodes.pop(0)
            
            new_lst = []
            for j in range(len(lst)):
                new_lst += ['']*num_space+[lst[j]]+['']*num_space+['']
                    
            num_space += 2**i
            new_lst.pop()
            self.level_nodes.append(new_lst)
                 
        return self.level_nodes[::-1]
        
        
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
    