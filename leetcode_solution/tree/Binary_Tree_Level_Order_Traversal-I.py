## [Leetcode#102] Binary Tree Level Order Traversal
##
## e.g. Given binary tree [3,9,20,null,null,15,7]
##      we will have [[3],[9,20],[15,7]]
##      then 3, 9->20, 15->7
##
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return []
        
        self.levels = []
        self.traverse(root, 1)
        return self.levels
        self.create_linkedLists()
        
        
    def traverse(self, root, depth):
        if len(self.levels) < depth: 
            self.levels.append([root.val])
        else:
            self.levels[depth-1].append(root.val)
        
        if root.left == None and root.right == None: return
    
        if root.left != None: self.traverse(root.left, depth+1)
        if root.right != None: self.traverse(root.right, depth+1)
    
    
    def create_linkedLists(self):
        for depth in range(len(self.levels)):
	    	head = self.levels[depth][0]
    		print (head.val)
    		while node.next != None:
       			node = node.next
        		print (node.val)
    			print ('------')