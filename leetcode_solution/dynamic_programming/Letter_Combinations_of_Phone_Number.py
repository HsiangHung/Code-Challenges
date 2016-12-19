## [Leetcode#17] Letter Combinations of a Phone Number
##
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        import copy
        if digits == '': return []
        
        mapping = {'2': set({'a','b','c'}), '3': set({'d','e','f'}), '4': set({'g','h','i'}), \
                '5':set({'j','k','l'}),'6':set({'m','n','o'}), '7':set({'p','q','r','s'}), \
                '8':set({'t','u','v'}), '9':set({'w','x','y','z'})}
            
        comb_sets = {}
        for i in range(len(digits)):
            digit = digits[i]
            if i ==0: 
                comb_sets[i+1] = mapping[digit]
            else:
                comb_sets[i+1] = set({})
                lst = mapping[digit]
                for ch1 in comb_sets[i]:
                    for ch2 in lst:
                        new_ch = ch1+ch2
                        comb_sets[i+1].add(new_ch)
                        
        return list(comb_sets[len(digits)])