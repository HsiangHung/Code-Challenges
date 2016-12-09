## Q. bonus questions: shrink a number
## On a positive integer, you can perform any one of the following 3 steps. 
##   1.) Subtract 1 from it. ( n = n - 1 )  , 
##   2.) If its divisible by 2, divide by 2. ( if n % 2 == 0 , then n = n / 2  )  , 
##   3.) If its divisible by 3, divide by 3. ( if n % 3 == 0 , then n = n / 3  ). 
##   Now the question is, given a positive integer n, find the minimum number of steps that takes n to 1

def min_step(n):
    if n <=3: return 1
    min_numberWays = {1:1, 2:1, 3:1}
    i = 4
    while i <= n:
        min_numberWays[i] = min_numberWays[i-1]+1
        if i % 2 ==0:
            min_numberWays[i] = min(min_numberWays[i], min_numberWays[int(i/2)]+1)
        if i % 3 ==0:
            min_numberWays[i] = min(min_numberWays[i], min_numberWays[int(i/3)]+1)
        i += 1
        
    return min_numberWays[n]


print (min_step(10))