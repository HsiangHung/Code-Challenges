# #348. Design Tic-Tac-Toe
#
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.row = {i: 0 for i in range(n)}
        self.col = {i: 0 for i in range(n)}
        self.diag1, self.diag2 = 0, 0
        self.size = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        
        point = {1: -1, 2: 1} # player=1, point=x; player=2, point=o
        
        self.row[row] += point[player]
        self.col[col] += point[player]
                
        if row == col: self.diag1 += point[player]
        if row + col == self.size-1: self.diag2 += point[player]
            
        if abs(self.row[row]) == self.size or abs(self.col[col]) == self.size or abs(self.diag1) == self.size or abs(self.diag2) == self.size:
            return player
        else:
            return 0
        

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)