# Online Python-3 Compiler (Interpreter)
print ("Hello, World!")

def binarysearch(ls, x, low, high):
    
    while (low <= high):
        mid = int((low + high)/2)
        if ls[mid] == x:
            return mid
        elif ls[mid] > x:
            high = mid -1
            binarysearch(ls, x, low, high)
        else:
            low = mid +1
            binarysearch(ls, x, low, high)
    return -1        
            
        
if __name__ == '__main__':
    ls = [10,20,30,40,50,60]
    n = len(ls)
    low = 0
    high = n-1
    x = 20
    res = binarysearch(ls, x,low,high)
    print(res)
    
    
