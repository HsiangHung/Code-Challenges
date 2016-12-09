## Q1.6 rotate a matrix at 90 degree in place

def rotate_matrix(A):
    n = len(A)
    ll = n-1
    for  j in range(int(n/2)):
        for i in range(ll):
            a = A[0+i+j][0+j]
            b = A[0+j][(n-1)-i-j]
            c = A[(n-1)-j][i+j]
            d = A[(n-1)-i-j][(n-1)-j]
    
            A[0+i+j][0+j]         =c
            A[0+j][(n-1)-i-j]     =a
            A[(n-1)-j][i+j]       =d
            A[(n-1)-i-j][(n-1)-j] =b
        
        ll -= 2  
        '''Note: here it is -= 2, not -= 1'''
        
    return A
    


        
A = [[1,2,3,4,0,0],[3,4,5,6,1,1],[9,10,11,12,5,5],[7,8,9,0,1,-1],[0,0,0,0,0,0],[2,2,2,2,2,2]]
print (rotate_matrix(A))