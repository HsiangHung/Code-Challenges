# Q11.1: merge two sroted arrays 
#
#
def merge_sorted_array(a,b):
    #print (a)
    if b[0] >= a[len(a)-1]: return a+b
    
    jj =0
    for num in b:
        for j in range(jj,len(a)):
            if a[j] > num: 
                jj = j
                a.insert(j,num)
                break
        print (len(a),j, jj, num)
        
        if num > a[len(a)-1]: a.append(num)
        
        
    print (a)
            
    
    
a = [1,2,3,5,15,70]
b = [0, 2.4, 4, 10,20,25,60]
    
merge_sorted_array(a,b)