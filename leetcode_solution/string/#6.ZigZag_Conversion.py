# [#6] ZigZag Conversion
#
#
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # create list of list [[], [], [],...] and control row: 0 -> numRow-1, and back

        if numRows == 1: return s

        res = [[] for i in range(numRows)]

        i, row = 0, 0
        while i < len(s):
            for _ in range(numRows):
                if i == len(s):
                    break
                res[row].append(s[i])
                row += 1
                i += 1

            row -= 2
            for _ in range(numRows - 2):
                if i == len(s):
                    break
                res[row].append(s[i])
                row -= 1
                i += 1
            
            row = 0

        return "".join(["".join(x) for x in res])
