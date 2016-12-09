
# Data structure: Convert an decimal integer to a binary number

```Python
def binarize(n):
    if n <= 1: return [str(n)]
    bits = []
    while n >=2:
        r = n %2
        bits.append(str(r))
        n = n // 2
        
    bits.append(str(n))
    return bits[::-1]
```
test
```Python
print (''.join(binarize(14)))
```