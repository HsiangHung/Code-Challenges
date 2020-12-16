# 138. Copy List with Random Pointer (medium)
# https://leetcode.com/problems/copy-list-with-random-pointer/
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
        if not head: return None
        
        head2 = Node(head.val)     
        n1, n2 = head, head2 
        visited, randoms = {}, {}
        while n1.next:
            nn1 = n1.next
            nn2 = Node(nn1.val)
            n2.next = nn2
                        
            randoms[n1] = n1.random
            visited[n1] = n2
            
            n1, n2 = nn1, nn2
        
        visited[n1] = n2
        randoms[n1] = n1.random
        
        for n1 in randoms:
            n2 = visited[n1]
            if randoms[n1] in visited:
                n2.random = visited[randoms[n1]] 
            
        return head2
            