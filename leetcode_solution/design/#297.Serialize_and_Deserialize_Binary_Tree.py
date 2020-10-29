# #297. Serialize and Deserialize Binary Tree
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return str([])
        
        self.data = [root.val]
        self.BFS([root])
        i = len(self.data)-1
        while self.data[i] == None:
            self.data.pop()
            i -= 1
        return str([x for x in self.data])
        

    def BFS(self, stack):
        new_stack = []
        while len(stack) > 0:
            node = stack.pop(0)
            if node: 
                left, right = node.left, node.right
                new_stack += [left, right]
                self.data += [left.val] if left else [None]
                self.data += [right.val] if right else [None]
        if len(new_stack) > 0: self.BFS(new_stack)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if data == "[]": return None
        
        data = data[1:-1].split(",")
        
        if len(data) == 0: return None
        
        val = data.pop(0)
        root = TreeNode(val=int(val))
        self.BFS2(data, [root])
        return root
        
    def BFS2(self, data, stack):
            
        if len(data) == 0: return
                    
        new_stack = []
        while len(stack) > 0:
            node = stack.pop(0)
            if node: 
                if len(data) > 0:
                    val = data.pop(0)[1:]
                    if val != "None": 
                        node.left = TreeNode(val=int(val))
                        new_stack.append(node.left)
                    else:
                        new_stack.append(None)
                    
                if len(data) > 0:
                    val = data.pop(0)[1:]
                    if val != "None": 
                        node.right = TreeNode(val=int(val))
                        new_stack.append(node.right)
                    else:
                        new_stack.append(None)

        if len(new_stack) > 0: self.BFS2(data, new_stack)


            
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))