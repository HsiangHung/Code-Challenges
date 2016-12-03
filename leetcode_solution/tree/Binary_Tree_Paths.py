## [Leetcode#257] Binary Tree Paths
## Given a binary tree, return all root-to-leaf paths.
## e.g. input: [5,4,8,11,null,13,6,7,2,null,null,null,1]
## `7->11->4->5`, `2->11->4->5`, `13->8->5`, `1->6->8->5`

#class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None        

class Solution(object):
    def findAllPath(self, root):
        """
        :type root: TreeNode
        """ 
        self.traverse(root, str(root.val))

    def traverse(self, node, path):
        if node.left == None and node.right == None:
            print (path)
            return

        if node.left != None:
            self.traverse(node.left, str(node.left.val)+'->'+path)
                
        if node.right != None:
            self.traverse(node.right, str(node.right.val)+'->'+path)





