## Q1.5 Compressed string
##
## e.g. 'aabccccgdjjjhhh' -> 'a2b1c4g1d1j3h3'
#

def compression_string(s):
    repeat = 1
    new_str = ''
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            new_str += s[i-1]+str(repeat)
            repeat = 1
        else:
            repeat +=1
    new_str += s[len(s)-1]+str(repeat)
    if len(new_str) > len(s): return s
    return new_str


print (compression_string('aabccccgdjjjhhh'))