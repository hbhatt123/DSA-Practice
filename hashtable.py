# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class HashTable():
    
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]
        
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max
        
    def setitem(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value
        
    def getitem(self,key):
        h = self.get_hash(key)
        return self.arr[h]
        
    def deleteitem(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
        
        
t = HashTable()
t.setitem('march', 31)
t.setitem('jan',31)
t.setitem('feb',28)
print(t.getitem('march'))
        
