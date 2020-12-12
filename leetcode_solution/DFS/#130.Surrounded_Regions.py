#  130. Surrounded Regions (medium)
#  https://leetcode.com/problems/surrounded-regions/
#
class Solution:
    '''
    as long as "O"s extend to the boarder, we cannot find flip.
    So only look for "O" extends to the boarder; otherwise change to "X".
    '''
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == []: return
        
        unchanged_O = set({})
                
        for y in [0, len(board)-1]:
            for x in range(len(board[0])):
                if board[y][x] == "O":
                    self.DFS(x, y, unchanged_O, board)
        
        for x in [0, len(board[0])-1]:
            for y in range(1, len(board)-1):
                if board[y][x] == "O":
                    self.DFS(x, y, unchanged_O, board)
                
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == "O" and (x,y) not in unchanged_O:
                    board[y][x] = "X"                    
                    
    def DFS(self, x, y, unchanged_O, board):
        if board[y][x] == "X" or (x, y) in unchanged_O: return
        
        unchanged_O.add((x, y))
        
        if x > 0:
            self.DFS(x-1, y, unchanged_O, board)
            
        if x < len(board[0])-1:
            self.DFS(x+1, y, unchanged_O, board)
            
        if y > 0:
            self.DFS(x, y-1, unchanged_O, board)
            
        if y < len(board)-1:
            self.DFS(x, y+1, unchanged_O, board)
