# [#717] 1-bit and 2-bit Characters
#
#
#
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        
        index = 0
        while index < len(bits)-2:
            if bits[index] == 0:
                index += 1
            else:
                index += 2
                
        if index == len(bits)-1:
            return True
        elif index == len(bits)-2:
            if bits[index] == 0:
                return True
            else:
                return False