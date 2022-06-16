# Online Python-3 Compiler (Interpreter)
# Find median of two sorted array with binary search
def feasible(ls,k,mid):
    n = len(ls)
    req = 1
    sum1 = 0
    for i in range(n):
        if (sum1+ls[i]) > mid:
            sum1 = ls[i]
            req = req+1
        else:
            sum1 = sum1 + ls[i]
    print("k",req)
        
    if req <= k:
        return True
    else:
        False
    
def min_pages(ls,k):
    n = len(ls)
    sum1 = 0
    for i in range(n):
        sum1 = sum1 + ls[i]
    min1 = ls[n-1]
    max1 = sum1
    print(min1,max1)
    low = min1
    high = max1
    res = 0
    while(low<=high):
        mid = int((low+high)/2)
        print(mid)
        if feasible(ls,k,mid):
            res = mid
            high = mid -1
        else:
            low = mid + 1
    return res        
        
 
if __name__ =='__main__':
    ls1 = [10, 20, 30, 40, 50]
    ls2 = [5, 15, 25, 27, 28, 55, 65, 75]
    ls = [10,5,20]
    ls = [10,20,10,30]
    ls = [10,20,30,40]
    ans = min_pages(ls1,2)
    print(ans)
