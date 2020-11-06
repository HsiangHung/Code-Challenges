# #138. Copy List with Random Pointer
#
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        '''
        need to store the pointer location.
        The copyed node is saved in a list, and original node is saved as 
        (key=node, value=node's rank)
        '''
        if not head: return head
        
        link, copy_link = {}, []
        
        copy_head = Node(head.val)        
        node, copy = head, copy_head
        idx = 0
        while node.next != None:
            copy2 = Node(node.next.val)
            copy.next = copy2
            copy_link.append(copy)
            link[node] = idx
            node, copy = node.next, copy2
            idx += 1
            
        copy_link.append(copy)
        link[node] = idx
        

        node, copy = head, copy_head
        for i, node in enumerate(link):
            if node.random is not None:
                copy_link[i].random = copy_link[link[node.random]]          
            node = node.next
            
            
        return copy_head
            