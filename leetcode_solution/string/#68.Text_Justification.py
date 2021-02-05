#  68. Text Justification (hard)
#  https://leetcode.com/problems/text-justification/
#
class Solution:
    '''
    Seems no quick algorithm: https://www.cnblogs.com/grandyang/p/4350381.html
    
    This problem is straightforward. prepare a "collect" to insert words:
    if num_chars + len(collect) - 1 (between words, need a sapce) + incoming word > maxWidth, we need to
    organize the current "collect", and then restart another new collect [word]

    I think it is labeled as hard because many cases needed to consider.
    '''
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        ans = []
        num_char, num_space, collect = 0, 0, []
        while len(words) > 0:
            word = words.pop(0)
            if num_char + len(collect) + len(word) <= maxWidth:
                collect.append(word)
                num_char += len(word)
                num_space += 1
            else:
                space = maxWidth - num_char
                                
                if len(collect) > 1:
                    avg_space = space // (len(collect)-1)  # by # of words in collect, find avg_space
                    space = space - avg_space*(len(collect)-1)
                    i = 0
                    while i < len(collect)-1: # first insert avg_spsce
                        collect.insert(i+1, " "*avg_space)
                        i += 2
                    
                    i = 0
                    while space > 0:  # if still space left, gradually fill from left to right
                        while i <= len(collect)-1 and collect[i] == " ":
                            i += 1
                        collect.insert(i+1, " ")
                        space -= 1
                        i += 2 
                else:
                    collect.append(" "*space)
                
                ans.append("".join(collect))
                num_char, num_space, collect = len(word), 1, [word]
                    
        if len(collect) > 0: # if the last line, readjust spaces. space between each words, and keep the remianing space in the end
            last_space = maxWidth - num_char - (len(collect)-1)
            i = 0
            while i < len(collect)-1:
                collect.insert(i+1, " ")
                i += 2

            collect.append(" "*last_space)
            ans.append("".join(collect))
        
        return ans
                
                
                
                
                
                
                
            