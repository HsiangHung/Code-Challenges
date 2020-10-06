# # 1305. All Elements in Two Binary Search Trees
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        '''
        find inorder list for each tree, respectively and merge the sorted lists.
        '''
        if not root1 and not root2: return []
        
        if not root1: return self.DFS(root2)
        if not root2: return self.DFS(root1)
       
        inorder1, inorder2 = self.DFS(root1), self.DFS(root2)
        
        print (inorder1, inorder2)
        
        i, j, output = 0, 0, []
        while i < len(inorder1) and j < len(inorder2):
            if inorder1[i] <= inorder2[j]:
                output.append(inorder1[i])
                i += 1
            else:
                output.append(inorder2[j])
                j += 1
        
        if i == len(inorder1) - 1 and j == len(inorder2) - 1:
            return output
        elif i == len(inorder1):
            return output + inorder2[j:]
        elif j == len(inorder2):
            return output + inorder1[i:]
            
    def DFS(self, root):
        if not root: return []
        inorder = self.DFS(root.left) + [root.val] + self.DFS(root.right)
        return inorder
        
        
        