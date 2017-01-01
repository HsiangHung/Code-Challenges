## Q2.2: last-k element of the linked list
#
def last_k(head, k):
    length = 1
    node = head
    k_node = None
    while node.next != None:
        if length == k:
            k_node = head
        elif length > k:
            k_node = k_node.next
        length += 1
        node = node.next
    if k_node != None: 
        k_node =k_node.next
        return k_node.val
    return 'NO SUCH NODE'

    
print (last_k(A, 1))