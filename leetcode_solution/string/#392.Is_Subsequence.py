# [#392] Is Subsequence
# 
#  Pinterest
#
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # trick: first make sure characters in s also exist in t
        # e.g. s = "leeeeetcode", there must at least 5 "e" in t. Otherwise it is False
        # also, each character in s needs to find the index in t with ascending order
        #
        s_dict = {}
        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1

        # second, we only care about characters which exist in s. If not, they are just useless.
        t_dict = {}
        for i in range(len(t)):
            if t[i] in s_dict:
                if t[i] in t_dict:
                    t_dict[t[i]].append(i)
                else:
                    t_dict[t[i]] = [i]
    
        # check t string has enough characters to host each character in t.
        for s_ch in s_dict:
            if s_ch not in t_dict or s_dict[s_ch] > len(t_dict[s_ch]):
                return False
                
        index = None
        for ch in s:
            if ch not in t_dict: return False
            
            if index == None:
                index = t_dict[ch].pop(0)  ## each time find the index, needs to pop out the minimum index
            else:
                if t_dict[ch][0] > index:
                    index = t_dict[ch].pop(0)  ## each time find the index, needs to pop out the minimum index
                else:
                    isThereIndex = False
                    for i in range(len(t_dict[ch])):
                        if t_dict[ch][i] > index:
                            isThereIndex = True
                            break
                    if not isThereIndex: return False
                    t_dict[ch] = t_dict[ch][i+1:]

        return True
                   
       