#  353. Design Snake Game (medium)
#  https://leetcode.com/problems/design-snake-game/
#
class SnakeGame:
    '''
    https://www.cnblogs.com/grandyang/p/5558033.html 
    
    everytime when the snakes eats, length += 1
    '''
    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.position = [(0, 0)]
        self.food = food
        self.width, self.height = width, height
        self.moves = {"U":(0, -1), "L": (-1, 0), "R": (1, 0), "D": (0, 1)}
        
        self.score = 0

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """

        x = self.position[0][0] + self.moves[direction][0]
        y = self.position[0][1] + self.moves[direction][1]  
                
        if (not self.width > x >= 0) or (not self.height > y >= 0) or (x, y) in self.position[:-1]:
            return -1
        
        self.position.insert(0, (x, y))
        
        if len(self.food) > 0 and [y, x] == self.food[0]:
            self.score += 1
            self.food.pop(0)
        else:
            self.position.pop()
           
        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)