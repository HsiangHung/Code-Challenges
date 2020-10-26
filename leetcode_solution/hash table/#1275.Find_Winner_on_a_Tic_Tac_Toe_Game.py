# # 1275. Find Winner on a Tic Tac Toe Game
#
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        '''
        https://blog.csdn.net/u013894776/article/details/104101776
        if all 1 or -1 (1) in a row (2) in a col (3) all diagonal, someone wins
        '''
        
        rows, cols = {i: 0 for i in range(3)}, {i: 0 for i in range(3)}
        diag1, diag2 = 0, 0
        
        point = {0: -1, 1: 1}
        
        for i in range(len(moves)):
            
            row, col = moves[i][0], moves[i][1]
            rows[row] += point[i % 2]
            cols[col] += point[i % 2]
            
            if row == col: diag1 += point[i % 2]
            if row + col == 2: diag2 += point[i % 2]
                
            if abs(rows[row]) == 3 or abs(cols[col]) == 3 or abs(diag1) == 3 or abs(diag2) == 3:
                return "A" if i % 2 == 0 else "B"
            elif i == 8: 
                return "Draw"
            
        return "Pending"