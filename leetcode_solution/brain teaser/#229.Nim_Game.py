## [#229] Nim Game
#   
#  Nim Game
#
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ## for player 1 to win, the number of stones need to be 5,6,7,9,10,11...
        ## as long as the number of stones is 4*intger, player 1 definitely will lose.
        
        return not (n % 4 == 0)