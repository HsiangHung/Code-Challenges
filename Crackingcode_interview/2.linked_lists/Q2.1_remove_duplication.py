## Q2.1: remove unsorted duplicated linked-list
#
# (a) using additional space O(n) with time O(n)  
# (b) brute force for space O(1) but time O(n^2)
#
# (a) -----------------------------------------------
def remove_dupNode_a(head):
    link_set = set({})
    node = head.next
    prev = head
    while node != None:
        if node.val in link_set:
            nextNode =node.next
            prev.next = nextNode
            node = nextNode
        else:
            link_set.add(node.val)
            prev = node
            node = node.next


# (b) -----------------------------------------------
def remove_dupNode_b(head):
    nodeA = head
    while nodeA != None:
        
        #print (nodeA.val)
        
        nodeB = nodeA.next
        prev = nodeA
        
        while nodeB != None:
            if nodeB.val == nodeA.val:
                nodeBNext = nodeB.next
                prev.next = nodeBNext
                nodeB = nodeBNext
            else:
                prev= nodeB
                nodeB = nodeB.next
                
            
        nodeA = nodeA.next
    
    

    
remove_dupNode_b(A)

## print test function: -----

node = A
while node.next != None:
    print(node.val)
    node = node.next
print(node.val)