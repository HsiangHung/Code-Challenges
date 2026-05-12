#  119. Pascal's Triangle II (easy)
#  https://leetcode.com/problems/pascals-triangle-ii/
#
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        
        ans = [1,1]
        while len(ans) <= rowIndex:
            new = []
            for i in range(1, len(ans)):
                new.append(ans[i-1]+ans[i])
            ans = [1]+new+[1]

        return ans