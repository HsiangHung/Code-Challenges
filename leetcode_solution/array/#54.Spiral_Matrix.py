#  54. Spiral Matrix (medium)
#  https://leetcode.com/problems/spiral-matrix/
#
class Solution:
    '''
    4-directions to rotate. only hit boundary or visited (x,y), make turn
    '''
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
                
        if len(matrix) == 0 or len(matrix[0]) == 0: return []
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ans = [matrix[0][0]]
        
        x, y = 0, 0
        
        i = 0
        dx, dy = directions[i]
        visited = set({(x, y)})
        for _ in range(len(matrix)*len(matrix[0])):
            
            if len(visited) == len(matrix)*len(matrix[0]):
                return ans
            
            x2, y2 = x+dx, y+dy
            
            if (not len(matrix[0]) > x2 >= 0) or (not len(matrix) > y2 >= 0) or (x2, y2) in visited:
                i += 1
                dx, dy = directions[i % 4]
                x2, y2 = x+dx, y+dy
            
            ans.append(matrix[y2][x2])
            visited.add((x2, y2))
            
            x, y = x2, y2
