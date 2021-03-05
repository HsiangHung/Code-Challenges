## [Leetcode#297] Serialize and Deserialize Binary Tree
#
# Google, MS, FB, Amazon, Bloomberg, LinkedIn, Uber, Yahoo
#
#
# using BFS to traversal the tree
#
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return str([])
    
        ans = [root.val]
        queue = [root]
        while queue:
            node = queue.pop(0)
                        
            if node.left:
                queue.append(node.left)
                ans.append(node.left.val)
            else:
                ans.append(None)
                
            if node.right:
                queue.append(node.right)
                ans.append(node.right.val)
            else:
                ans.append(None)

        return str(ans)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data[1:-1].split(",")
        
        if data[0] == "": return None
        
        root = TreeNode(int(data[0]))
        stack = [root]
        for i in range(1, len(data), 2):
            
            if len(stack) > 0:
                node = stack.pop(0)
                left, right = data[i], data[i+1]
                if left != " None": 
                    node.left = TreeNode(int(left[1:]))
                    stack.append(node.left)

                if right != " None": 
                    node.right = TreeNode(int(right[1:]))
                    stack.append(node.right)
        
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))