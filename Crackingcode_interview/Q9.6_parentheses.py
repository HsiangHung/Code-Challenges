## Q9.6: generating potential combined parentheses
def generate_parenthese(n):
    import copy
    pare_sets = {1: set({"()"})}
    
    i=2
    while i <= n: 
        pare_sets[i] = set({})
        print (i)
        
        for pare in pare_sets[i-1]:
            print ('pare',pare)
            for m in range(len(pare)):
                if m ==0:
                    new_pare = pare[0]+'('+pare[1:]+')'
                else:
                    new_pare = pare[:m+1]+'('+pare[m+1:]+')'
                #new_pare.insert(m+1,"(")
                #new_pare.append(")")
                print (m, new_pare)
                pare_sets[i].add(new_pare)
        i +=1
    
    print (pare_sets)
    
    return pare_sets[n]

print (generate_parenthese(4))