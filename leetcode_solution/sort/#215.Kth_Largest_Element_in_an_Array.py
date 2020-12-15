# #215. Kth Largest Element in an Array
#
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        queue = []
        for num in nums:
            queue = self.isKth(queue, num, k)
        
        return queue[0]
                
                
    def isKth(self, queue, num, k):
        if queue == []:
            queue.append(num)
        else:
            queue = self.InsertNum(queue, num, k)
        
        return queue[-k:]
    
    
    def InsertNum(self, queue, num, k):
        if num >= queue[-1]:
            queue.append(num)
        elif num < queue[0]:
            queue.insert(0, num)
        elif queue[0] < num < queue[-1]:
            i = 1
            while i < len(queue)-1 and num > queue[i]:
                i += 1
            queue.insert(i, num)
                
        return queue