## [Leetcode#791] Custom Sort String
#
#
#
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        # e.g. S = 'cba' and T = 'aabccccd'
        # should return 'ccccbaad'
        # so first find the characters in T which do NOT appear in S, (like 'd')
        # also prepare characters in T which appear in S in dictionary
        # and then reconstruct
        
        S_set = set(list(S))
        T_dict = {}
        miss_lst = []
        for ch in T:
            if ch not in S_set:
                miss_lst.append(ch)
            else:
                T_dict[ch] = T_dict.get(ch, 0) + 1
        
        string = ''
        for ch in S:
            if ch in T_dict:
                string += T_dict[ch]*ch

        if len(miss_lst) > 0:
            return string + ''.join(miss_lst)
        else:
            return string