#  79. Word Search (medium)
#  https://leetcode.com/problems/word-search/
#
#
#  This version passed 87/89 test cases, but time limit exceed
#
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        https://www.cnblogs.com/grandyang/p/4332313.html
        '''
        self.found = False
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == word[0]:
                    self.DFS(x, y, board, 0, word)
                    if self.found: return True
                    
        return False

    
    def DFS(self, x, y, board, i, word):
        
        if board[y][x] is True or board[y][x] != word[i]: return
        
        if i == len(word)-1 and board[y][x] == word[i]:
            self.found = True
            return
        
        char = board[y][x]
        board[y][x] = True
        
        if x > 0:
            self.DFS(x-1, y, board, i+1, word)
            
        if x < len(board[0])-1:
            self.DFS(x+1, y, board, i+1, word)
        
        if y > 0:
            self.DFS(x, y-1, board, i+1, word)
            
        if y < len(board)-1:
            self.DFS(x, y+1, board, i+1, word)

        board[y][x] = char  ## important, need to change back, otherwise wrong, see code from https://www.cnblogs.com/grandyang/p/4332313.html
