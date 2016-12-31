## Q1.4 replace SPACE with '%20'
##
## e.g. 'Mr John Smith  ' -> 'Mr%20John%20Smith'
#
#  Note there is a catch here. in the loop if we do s.insert(i,'%20')
#  the result becomes 'Mr%20%20JohnSmith' since during inserting
#  the size of s is increasing!
#
def replace(s):
    s = s.lstrip().rstrip().split(' ')
    print (s)
    for i in range(1, len(s)):
        s[i] = '20%'+s[i]
    return ''.join(s)

print (replace('Mr John Smith  '))