#
# 345. Reverse Vowels of a String
#  

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        vowel_index = []
        vowel_char = []
        for i in range(len(s)):
            if s[i].lower() in vowels:
                vowel_index.append(i)
                vowel_char.append(s[i])
        
        new_s = list(s)
        for i in range(len(vowel_index)):
            idx = vowel_index[i]
            new_s[idx] = vowel_char[len(vowel_index)-1-i]

        return "".join(new_s)
