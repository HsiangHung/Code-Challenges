## Q5.7: An array A = [0,1,2....n], but one element is missing
#  The elements are represented in binary, so to find the missing element,
#  we may need to go over all bits. Can we do time complexity O(n) way?
#
#  idea: search the first bit, 0,1,0,1.. 1,1,1 mean missing here
#
#  0:  0000
#  1:  0001
#  2:  0010
#  3:  0011
#  4:  0100  xx assume 4 is missing
#  5:  0101
#
#  then first bit will be 0,1,0,1,1 (expected 0,1,0,1,0,1)

def missing_element(array):
    for i in range(len(array)+1):
        print (i,array[i][len(array[i])-1])
        if i % 2 != array[i][len(array[i])-1]: break
        i +=1
    
    return i


print (missing_element(array))

## --------------------------
#
#test function

def binarize(n):
    if n <= 1: return [n]
    bits = []
    while n >=2:
        r = n %2
        bits.insert(0,r)
        n = n // 2
        
    bits.insert(0,n)
    return bits

array = []
for i in range(0,20):
    array.append(binarize(i))
    #
print (array)

del array[12]

print (array)