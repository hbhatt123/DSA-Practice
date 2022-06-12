# Python 3 program to find the ones in
# a given sorted array

# if x is present in arr[] then
# returns the index of FIRST
# occurrence of x in arr[0..n-1],
# otherwise returns -1
def numones(ls, low, high, x, n):
    while(high >= low):
        mid = int((low + high)/2)
        if ls[mid] != x:
            low = mid + 1
        elif ls[mid] == x and ls[mid-1] != x:
            return n - mid
        else:
            high = mid - 1
    return -1

    
if __name__ =='__main__':    
    # Driver program
    arr = [1, 1, 1, 1, 2, 2, 2, 2, 3, 4, 7, 7, 7, 8, 8]
    arr = [0,0,0,0,0,1,1,1,1,1,1,1]
    n = len(arr)
    x = 1
    res = numones(arr, 0, n-1, x, n)
    print(res)
    

# This code is contributed by Nikita Tiwari.
