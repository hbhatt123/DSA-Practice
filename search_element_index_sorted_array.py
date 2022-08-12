# Online Python-3 Compiler (Interpreter)
print ("Hello, World!")

def binarysearch(ls, x):
    n = len(ls)
    low = 0
    high = n-1
    while (low <= high):
        mid = int((low + high)/2)
        if ls[mid] == x:
            return mid
        elif ls[mid] > x:
            high = mid -1
        else:
            low = mid +1
   return low   
        
if __name__ == '__main__':
    ls = [10,20,30,40,50,60]
    x = 10
    res = binarysearch(ls, x)
    print(res)
    
    
