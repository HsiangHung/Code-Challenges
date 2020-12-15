#  378. Kth Smallest Element in a Sorted Matrix (medium)
#  https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
#
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        '''
        http://bookshadow.com/weblog/2016/08/01/leetcode-kth-smallest-element-in-a-sorted-matrix/
        '''
        heap = [(matrix[0][0], 0, 0)]
        visited = set({(0, 0)})
        
        for _ in range(k):
            
            val, i, j = heapq.heappop(heap)
            
            if i < len(matrix)-1 and (i+1, j) not in visited:
                visited.add((i+1, j))
                heapq.heappush(heap, (matrix[i+1][j], i+1, j))
                
            if j < len(matrix[0])-1 and (i, j+1) not in visited:
                visited.add((i, j+1))
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
                
        return val            