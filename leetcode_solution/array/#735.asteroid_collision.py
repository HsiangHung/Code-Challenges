#
# 735. Asteroid Collisiong
# 
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        1. if s[i] < 0 and s[i+1] > 0, no collides (e.g. [-1, 1])
        2. if s[i] > 0 (move right) and s[i+1] < 0 (move left), collides (e.g[5, -6])

        for case 2, need to keep update until collides, or one left
        [3,5,-6,2,-1,4]​​​​​​​ -> [3,-6,2,-1,4]​​​​​​​ -> [-6,2,-1,4]​​​​​​​ -> [-6,2,4] ​​​​​​​
        """
        if len(asteroids) <= 1:
            return asteroids

        ast = asteroids.copy()

        i = 0
        while ast and i < len(ast)-1:
            if ast[i] > 0 and ast[i+1] < 0:
                if abs(ast[i]) == abs(ast[i+1]):
                    x = ast.pop(i)
                    y = ast.pop(i)
                    i -= 1
                elif abs(ast[i]) > abs(ast[i+1]):
                    ast.pop(i+1)
                else:
                    while ast and 0 <= i < len(ast) and ast[i] > 0 and ast[i+1] < 0 and abs(ast[i]) < abs(ast[i+1]):
                        ast.pop(i)
                        i -= 1
            else:
                i += 1
            
            if i == -1: 
                i =0 # when check back, i could = -1, need to calibrated to 0
        
        return ast
