#  547. Friend Circles (medium)
#  https://leetcode.com/problems/friend-circles/
#
#
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        Lrow = len(M)
        Lcol = len(M[0])
        
        # This is the problem different from number of islands.
        # it is equivalent to find which row or col indices have unique 
        
        n_circles = 0
        for row in range(Lrow):
            if M[row][row] == 1:
                n_circles += 1
                self.DFS(Lrow, Lcol, row, M)

        return n_circles
            
    def DFS(self, Lrow, Lcol, row, M):
        
        if M[row][row] == 0: return
        
        M[row][row] = 0
        for col in range(Lcol):
            if M[row][col] == 1:
                self.DFS(Lrow, Lcol, col, M)