## Q1.5 Compressed string
##
## e.g. 'aabccccgdjjjhhh' -> 'a2b1c4g1d1j3h3'
#

def compression_string(s):
    repeat = 1
    compress_str = s[0]
    for i in range(1,len(s)):
        
        if s[i] == s[i-1]: 
            repeat += 1
        elif s[i] != s[i-1]:
            compress_str += str(repeat)+s[i]
            repeat = 1

    compress_str += str(repeat)  
            
    return compress_str


print (compression_string('aabccccgdjjjhhh'))