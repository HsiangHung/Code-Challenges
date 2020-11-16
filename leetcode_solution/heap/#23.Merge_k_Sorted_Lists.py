# # 23. Merge k Sorted Lists
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
        from heapq import heappush, heappop
        
        if len(lists)==0: return
        
        heap = []
        curNode = root = ListNode(0) # dummy
        count = 0
        for node in lists:
            if node:
                count += 1
                heappush(heap, (node.val, count, node))
        
        
        while heap:
            value, _, node = heappop(heap)

            curNode.next = ListNode(value)
            curNode = curNode.next
            if node.next:
                count += 1
                heappush(heap,(node.next.val, count, node.next))

        return root.next
