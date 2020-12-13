#  212. Word Search II (hard)
#  https://leetcode.com/problems/word-search-ii/
#
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
        similar 79. word search, but here multiple words to check.
        '''
        m, n = len(board[0]), len(board)
        
        ans = set({})
        for word in words:

            for y in range(n):
                for x in range(m):

                    if board[y][x] in word:
                        self.found = False
                        self.DFS(m, n, x, y, board, word)
                        if self.found: 
                            ans.add(word)
                            break            ## trick, once found this word, stop iteration for next word

        return list(ans)
                    
    def DFS(self, m, n, x, y, board, word):                        
        if board[y][x] is True or board[y][x] != word[0]: return
        
        if len(word) == 1 and board[y][x] == word[0]:
            self.found = True
            return
        
        char = board[y][x]
        board[y][x] = True
                
        if x > 0:
            self.DFS(m, n, x-1, y, board, word[1:])
            
        if y > 0:
            self.DFS(m, n, x, y-1, board, word[1:])
       
        if x < m-1:
            self.DFS(m, n, x+1, y, board, word[1:])
       
        if y < n-1:
            self.DFS(m, n, x, y+1, board, word[1:])
       
        board[y][x] = char