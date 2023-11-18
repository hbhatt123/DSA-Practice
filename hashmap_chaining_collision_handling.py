# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class HashTable():
    
    def __init__(self):
        self.max = 10
        self.arr = [[ ] for i in range(self.max)]
        
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max
        
    def setitem(self,key,value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][idx] = (key,value)
                found = True
        if not found:    
            self.arr[h].append((key,value))
          
        
    def getitem(self,key):
        h = self.get_hash(key)
        for k in self.arr[h]:
            if k[0] == key:
                return k[1]
            
        
    def deleteitem(self,key):
        h = self.get_hash(key)
        for i, v in enumerate(self.arr[h]) :
            if v[0] == key:
                del self.arr[h][i] 
        
        
t = HashTable()
t.setitem('march 6', 310)
t.setitem('march 8',31)
t.setitem('march 17',67)
print(t.getitem('march 6'))
print(t.getitem('march 17'))
print(t.arr)
print(t.deleteitem('march 6'))
print(t.arr)
        
