## [Leetcode#657] Judge Route Circle
##

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        moves_dict = {'L':0, 'R':0, 'U':0, 'D':0}
        for move in list(moves):
            moves_dict[move] += 1
            
        return moves_dict['L'] == moves_dict['R'] and moves_dict['U'] == moves_dict['D']
            
        