#  79. Word Search (medium)
#  https://leetcode.com/problems/word-search/
#
#
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board and word:
            return False

        # 1. identify the coordinate (x, y) in board whose ch == word[0]
        ch_loc = []
        for i in range(len(board)):
            for j in range(len(board[0])): # initial character of word
                if board[i][j] == word[0]:
                    ch_loc.append((i, j))

        # 2. DFS search to see if the word exists. Remember to store visited sites, but need 
        #    to remove the visited sites for other DFS thread.
        self.is_word_exist = False
        def DFS(x, y, visited, word_index):
            if (not 0 <= x < len(board)) or (not 0 <= y < len(board[0])) or (x, y) in visited:
                return 

            if board[x][y] == word[word_index]:
                if word_index == len(word) - 1:
                    self.is_word_exist = True
                    return

                visited.add((x, y))
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if (x + dx, y + dy) not in visited:
                         DFS(x+dx, y+dy, visited, word_index + 1)
                visited.remove((x, y)) # NOTE, for DFS, we remove it otherwise "visited" always visits!

        for x, y in ch_loc:
            DFS(x, y, set({}), 0)
            if self.is_word_exist == True:
                return True

        return False
        
        