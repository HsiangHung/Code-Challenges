# [#760] Find Anagram Mappings
#
#
#
class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        B_dict = {}
        for i in range(len(B)):
            if B[i] not in B_dict:
                B_dict[B[i]] = [i]
            else:
                B_dict[B[i]].append(i)
                
        mapping = []
        for num in A:
            index = B_dict[num].pop()
            mapping.append(index)
            
        return mapping