## Q9.1 Climb stairs
#
def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
        
    if n == 1: return 1  ## {1}
    if n == 2: return 2  ## {1,1}, {2}}
    if n == 3: return 4   ## {{1,1,1},{1,2},{2,1},{3}}   
        
    numberWays = {1:1, 2:2, 3:4}
        
    i = 4
    while i <= n:
        numberWays[i] = numberWays[i-1]+numberWays[i-2]+numberWays[i-3]
        i += 1
            
    return numberWays[n]

print (climbStairs(5))