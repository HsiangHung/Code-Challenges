#  240. Search a 2D Matrix II (medium)
#  https://leetcode.com/problems/search-a-2d-matrix-ii/
#
class Solution:
    '''
    somehow, using BFS in this problem cannot pass all test cases in Leetcode
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0: return False
        
        midx, midy = len(matrix[0]) // 2, len(matrix) // 2
        return self.DFS(midx, midy, matrix, target, set({}))
        
    
    def DFS(self, x, y, matrix, target, visited):
        if matrix[y][x] == target: return True
        if (x, y) in visited: return False
    
        visited.add((x, y))
        
        found = False
        if matrix[y][x] > target:
            if x > 0 and (x-1, y) not in visited:
                found = found or self.DFS(x-1, y, matrix, target, visited)

            if y > 0 and (x, y-1) not in visited:
                found = found or self.DFS(x, y-1, matrix, target, visited)

        if matrix[y][x] < target:
            if x < len(matrix[0])-1 and (x+1, y) not in visited:
                found = found or self.DFS(x+1, y, matrix, target, visited)

            if y < len(matrix)-1 and (x, y+1) not in visited:
                found = found or self.DFS(x, y+1, matrix, target, visited)

        return found