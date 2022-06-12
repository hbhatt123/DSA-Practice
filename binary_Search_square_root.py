# Python 3 program to find the ones in
# a given sorted array

# if x is present in arr[] then
# returns the index of FIRST
# occurrence of x in arr[0..n-1],
# otherwise returns -1
def squareroot(x):
    low = 1
    high = x
    while(low <= high):
        mid = int((low+high)/2)
        print("mid", mid)
        print("low", low)
        print("high", high)
        msq = mid*mid
        if msq == x:
            return mid
        if msq > x:
            high = mid -1
            print(low, high, mid)
        elif msq < x:   
            low = mid + 1
            ans = mid
            print(low, high, mid)
    return ans

    
if __name__ =='__main__':    
    # Driver program
    x = 25
    res = squareroot(x)
    print("ans", res)
    

