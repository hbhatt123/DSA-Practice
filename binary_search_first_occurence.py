# Online Python-3 Compiler (Interpreter)
print ("Hello, World!")

def binarysearch(ls, x, low, high):
    
    while (low <= high):
        mid = int((low + high)/2)
        if ls[mid] == x and ls[mid-1] != x:
            return mid
        elif ls[mid] == x and ls[mid-1] == x:
            high = mid -1
            binarysearch(ls,x,low,high)
        elif ls[mid] > x:
            high = mid -1
            binarysearch(ls, x, low, high)    
        else:
            low = mid +1
            binarysearch(ls, x, low, high)    
    return -1        
            
        
if __name__ == '__main__':
    infi = float('inf')
    ls = [10,20,20,30,30,40,40,50,60]
    ls = [1,3,2,5,2,infi,infi,infi,infi,infi,infi]
    n = len(ls)
    low = 0
    high = n-1
    x = infi
    res = binarysearch(ls, x,low,high)
    print(res)
    
    
