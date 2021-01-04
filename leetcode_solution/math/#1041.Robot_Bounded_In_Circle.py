#  1041. Robot Bounded In Circle (medium)
#  https://leetcode.com/problems/robot-bounded-in-circle/
#
class Solution:
    '''
      initially face to north, head = 0. "L" head + 1 and "R" head -1
                        (dx,dy)
                  north (0,1) 
      left (-1,0)             right (1,0)
                  south (0,-1)
    
      after every turn, determine (dx, dy) by head % 4.

      after running instructions 4 times, if not back to (0,0), return False otherwise True
    '''
    def isRobotBounded(self, instructions: str) -> bool:
                                
        turns = {0: (0, 1), 1: (-1, 0), 2: (0, -1), 3: (1, 0)}
            
        x, y = 0, 0
        dx, dy = 0, 1
        head = 0
        for _ in range(4):
            
            for move in instructions:
                if move == 'G':
                    x += dx
                    y += dy
                elif move == "L":
                    head += 1
                    dx, dy = turns[head % 4]
                else:
                    head -= 1
                    dx, dy = turns[head % 4]
                    
            if x == 0 and y == 0: return True
            
        return False
                    
            
        