#  295. Find Median from Data Stream (hard)
#  https://leetcode.com/problems/find-median-from-data-stream/
#
class MedianFinder:
    '''
    https://www.youtube.com/watch?v=1LkOrc-Le-Y
    http://bookshadow.com/weblog/2015/10/19/leetcode-find-median-data-stream/
    
    worst case is O(n^2), n is for the number of data in stream, and insert sort O(n)
    using heap, binary tree (O(logn)), -> O(n*logn)
    
    if ordered numbers = [x1, x2, .... xn, xn+1, .... x2n]
    
    [x1...xn] forms max_heap (first half), and [xn+1,.... x2n] forms min_heap (second half)
    
    1. if even size of max_heap, 
         max_heap = [2, 6]; min_heap = [8, 10]
         * if num < 8, whatever num pushes to max_heap => max_heap = [2, 5, 6] or [2, 6, 7],
         * if num >= 8, pop minimum of min_heap to max_heap, and psuh to min_heap 
                       => max_heap = [2, 6, 8], min_heap = [9, 10]
    2. if odd size of max_heap, 
         max_heap = [2, 6, 7]; min_heap = [9, 10]
         * if num <= 7, pop maximum (7) of max_heap => max_heap = [2, 5, 6] or [2, 6, 7],
                        and push to min_heap = [7, 9, 10]
         * if num > 7, psuh to min_heap => max_heap = [2, 6, 7], min_heap = [8, 9, 10]
    
    '''
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []
        self.left = 0
        

    def addNum(self, num: int) -> None:
        if self.left == 0:
            heappush(self.max_heap, (-num, num))
            self.left = "odd"
        else:
            if self.left == "even":
                if num <= self.min_heap[0]:
                    heapq.heappush(self.max_heap, (-num, num))
                else:
                    x = heapq.heappop(self.min_heap)
                    heapq.heappush(self.max_heap, (-x, x))
                    heapq.heappush(self.min_heap, num)
                self.left = "odd"
            elif self.left == "odd":
                if num <= self.max_heap[0][1]:
                    _, x = heapq.heappop(self.max_heap)
                    heapq.heappush(self.min_heap, x)
                    heapq.heappush(self.max_heap, (-num, num))
                else:
                    heapq.heappush(self.min_heap, num)
                self.left = "even"
                
    def findMedian(self) -> float:
        if self.left == "even":
            a, b = self.max_heap[0][1], self.min_heap[0]
            return (a + b)/2
        else:
            return self.max_heap[0][1]
  