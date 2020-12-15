# 23. Merge k Sorted Lists (hard)
# https://leetcode.com/problems/merge-k-sorted-lists/
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        '''
        Use Min heap: https://www.youtube.com/watch?v=ptYUCjfNhJY
        https://docs.python.org/3.0/library/heapq.html
        
        code:
        https://leetcode.com/problems/merge-k-sorted-lists/discuss/10511/10-line-python-solution-with-priority-queue (python3)
        https://zhuanlan.zhihu.com/p/93347320 (python2)
        https://statyang.wordpress.com/python-practice-49-merge-k-sorted-lists/ (python2)
        
        time complexity O(n*log(k)), space O(k)
        k: number of lists, n is total number of all k nodes
        '''
        if len(lists) == 0: return None

        dummy_head = ListNode(val=-1)
        
        heap = []
        count = 0
        for node in lists:
            if node:
                count += 1
                heapq.heappush(heap, (node.val, count, node))  # (value1, value2, object)
    
        # e.g. lists = [1->4->5, 1->3->4, 2->6]
        # now heap has [1,1,2]

        curr = dummy_head
        while heap:
            
            val, _, node = heapq.heappop(heap)   # the minHeap pop out minimum value = val
            
            curr.next = node
            if node.next is not None:
                node = node.next
                count += 1
                heapq.heappush(heap, (node.val, count, node)) # after popout a node, insert node.next
                
            curr = curr.next
                
        
        return dummy_head.next
      
                
