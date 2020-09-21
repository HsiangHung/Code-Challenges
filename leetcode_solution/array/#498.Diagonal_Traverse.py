# #498. Diagonal Traverse
#
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        trick on boundary conditions, in particular on the lower left (0, n-1) 
        and upper right (m-1, 0) corners.
        '''
        
        if len(matrix) == 0 or len(matrix[0]) == 0: return matrix
        
        m, n = len(matrix[0]), len(matrix)
        
        if m == 1: ## when matrix is only a column vector, need to special care.
            return [x[0] for x in matrix]
        
        output = [matrix[0][0]]
        
        x, y = 1, 0
        direction = -1
        while x < m and y < n:
            
            output.append(matrix[y][x])
            
            x += direction
            y -= direction
            
            if x < 0 or y < 0 or x >= m or y >= n:
                direction *= -1
            
            if x < 0:
                if y > n-1:
                    y = n-1
                    x += 2
                else:
                    x = max(x, 0)
            elif y < 0:
                if x > m-1:
                    x = m-1
                    y += 2
                else:
                    y = max(y, 0)
            elif x > m-1:
                x = min(x, m-1)
                y += 2
            elif y > n-1:
                y = min(y, n-1)
                x += 2
                
        return output