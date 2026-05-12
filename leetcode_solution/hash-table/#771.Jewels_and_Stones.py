# [#771] Jewels and Stones
#
# Amazon  
#
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        stone_dict = {}
        for i in range(len(S)):
            stone_dict[S[i]] = stone_dict.get(S[i], 0) + 1
            
        return sum([stone_dict[stone] for stone in stone_dict if stone in set(list(J))])
                