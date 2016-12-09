## Q2.2: last-k element of the linked list
#
def last_k(head, k):
    node = head
    length = 1
    while node.next != None:
        if length == k: node_k = node
        length +=1        
        node = node.next
    
    return node_k.val
    
print (last_k(A, 1))