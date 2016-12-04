## [Leetcode#144] Binary Tree Preorder Traversal
##  using iteration to run preorder! (my favorite)
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ## meet a new node, say A, we push the node twice in stack: stack=[...B,B,] -> stack=[...B,B,A,A]
        ## if stack = [...B,B,A,A] goes left and pop A => stack=[..B,B,A]
        ## if stack = [...B,B,A] goes right and pop A => stack=[..B,B]
        ## then we know it goes back to it parent B
        ## e.g. [1,2,3,4]: 
        ## initial stack = [1,1]:1.left =2 then s=[1,2,2]
        ## [1,2]: 2.left=4 then s=[1,2,4,4] 
        ## [1,2,4,4]: 4.left=None -> s=[1,2,4] -> 4.right=None ->  s=[1,2]
        ## [1,2] -> 2.right=None then [1]
        ## [1]: 1.right=3 then [3,3]
        ## [1,3,3]: 3.left =None then [1,3]; 3.right then [1] 
        if not root: return []
        
        stack = [root, root]
        preorder = [root.val]
        
        while len(stack) != 0:
            #print [x.val for x in stack]
            root = stack[len(stack)-1]
            
            if len(stack)>1 and stack[len(stack)-1] == stack[len(stack)-2]:
                stack.pop()
                if root.left != None:
                    preorder.append(root.left.val)
                    stack.append(root.left)
                    stack.append(root.left)
            elif len(stack)==1 or stack[len(stack)-1] != stack[len(stack)-2]:
                stack.pop()
                if root.right != None:
                    preorder.append(root.right.val)
                    stack.append(root.right)
                    stack.append(root.right)
        return preorder