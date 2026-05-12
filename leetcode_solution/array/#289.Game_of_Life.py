"""
289. Game of Life
"""
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def judge_live(x, y, arr):
            live, dead = 0, 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    if 0 <= y + dy < len(arr) and 0 <= x + dx < len(arr[0]):
                        if arr[y+dy][x+dx] == 1:
                            live += 1
    
            if arr[y][x] == 1:
                return 1 if live in (2, 3) else 0
            else:
                return 1 if live == 3 else 0

        board_copy = [row[:] for row in board]
        # NOTE if using board_copy = board.copy(), whenever update in board also impacts board_copy
        # therefore we got wrong answer.

        for y in range(len(board)):
            for x in range(len(board[0])):
                update = judge_live(x, y, board_copy)
                board[y][x] = update
