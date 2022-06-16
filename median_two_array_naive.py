# Online Python-3 Compiler (Interpreter)
# Find median of two sorted array
def median(ls1,ls2):
    n1 = len(ls1)
    n2 = len(ls2)
    ls1.extend(ls2)
    n = len(ls1)
    for i in range(n):
        for j in range(n):
            if ls1[i] < ls1[j]:
                ls1[i], ls1[j] = ls1[j], ls1[i]
    print(n) 
    print(ls1)
    mid = int((0 + n-1)/2)
    if(n % 2 != 0):
        return ls1[mid]
    else:
        return (ls1[mid] +ls1[mid+1])/2
        
   
 
if __name__ =='__main__':
    ls1 = [2, 8, 2, 2, 3, 5, 6]
    ls2 = [3,5,7,9,10,12,14]
    ans = median(ls1,ls2)
    print(ans)
