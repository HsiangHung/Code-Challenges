## [#151] Reverse Words in a String
#
#
#
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "": return s
        
        reverse_words = []
        
        sub_s = ''
        for ch in s:
            if ch != " ":
                sub_s += ch
            else:
                if sub_s != '':
                    reverse_words.insert(0, sub_s)
                sub_s = ''
        
        if sub_s != '':
            reverse_words = [sub_s] + reverse_words
        
        if len(reverse_words) == 0:   ## case of input = "     "
            return ''
        elif len(reverse_words) == 1:  ## case of input = "aaab"
            return reverse_words[0]
        else:
            return ' '.join(reverse_words)