#  973. K Closest Points to Origin (medium)
#  https://leetcode.com/problems/k-closest-points-to-origin/
#
class Solution:
    '''
    using heap, this can turn to O(n + logK)
    '''
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        for data in points:
            x, y = data[0], data[1]
            heapq.heappush(heap, (self.distance(x, y), x, y))
            
        ans = []
        for _ in range(k):
            _, x, y = heapq.heappop(heap)
            ans.append([x, y])
            
        return ans
            
    def distance(self, x, y):
        return x**2 + y**2