# 74. Search a 2D Matrix
#
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        This problem I used DFS. 
        if matrix[y][x] == target return True
        if matrix[y][x] > target, search matrix[y-1][x] and matrix[y][x-1] if x, y > 1
        if matrix[y][x] < target, search matrix[y+1][x] and matrix[y][x+1] if x, y < bound
        
        but remember to update matrix[y][x] to "a" if it has been searched, such that no unlimited DFS.
        '''
        if len(matrix) == 0 or len(matrix[0]) == 0: return False
        
        x, y = len(matrix[0]) // 2, len(matrix) // 2
        return self.DFS(x, y, matrix, target)
        
    def DFS(self, x, y, matrix, target):
        
        if matrix[y][x] == "a": return False
        
        if matrix[y][x] == target: 
            return True
        elif matrix[y][x] > target: 
            matrix[y][x] = "a"  ## important for this update, otherwise unlimited search
            if x > 0:
                if self.DFS(x-1, y, matrix, target): return True
            
            if y > 0:
                if self.DFS(x, y-1, matrix, target): return True

            return False
        else:
            matrix[y][x] = "a" ## important for this update, otherwise unlimited search
            if y < len(matrix)-1:
                if self.DFS(x, y+1, matrix, target): return True
            
            if x < len(matrix[0])-1:
                if self.DFS(x+1, y, matrix, target): return True
   
            return False
    
   