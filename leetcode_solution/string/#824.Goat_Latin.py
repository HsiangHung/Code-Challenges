# #824. Goat Latin
#
class Solution:
    def toGoatLatin(self, S: str) -> str:
        
        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        
        S = S.split(" ")
        
        goatLatin = []
        for i, word in enumerate(S):
            if word[0] not in vowels:
                word = word[1:] + word[0]
                
            word = word + "ma" + "a"*(i+1)
            goatLatin.append(word)
            
        return " ".join(goatLatin)
