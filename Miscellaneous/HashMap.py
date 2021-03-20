'''
https://www.geeksforgeeks.org/hash-map-in-python/
'''
class HashMap(object):

    def __init__(self, size):
        self.size = size
        self.data = [-1]*size

    def put(self, key, val):
        hashed_key = hash(key) % self.size 
        if self.data[hashed_key] == -1:
            self.data[hashed_key] = [(key, val)]
        else:
            key_found = False
            for i, record in enumerate(self.data[hashed_key]):
                if record[0] == key:
                    key_found = True
                    break
            
            if key_found:
                self.data[hashed_key][i] = (key, val) # update value
            else:
                self.data[hashed_key].append((key, val))

    def get(self, key):
        hashed_key = hash(key) % self.size
        if self.data[hashed_key] == -1:
            return -1
        else:
            print (self.data[hashed_key])
            key_found, i = False, 0
            for i, record in enumerate(self.data[hashed_key]):
                if record[0] == key:
                    key_found = True
                    break
            
            if key_found:
                return self.data[hashed_key][i][0]
            else:
                return -1

    
            

hashmap = HashMap(100000)

print (hashmap.put(100, "sos"))
print (hashmap.put("val", "python"))
print (hashmap.get(100))
print (hashmap.get("val"))
print (hashmap.get("sos"))
print (hashmap.get(124))