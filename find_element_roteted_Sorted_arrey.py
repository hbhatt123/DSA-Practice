# Python Program to demonstrate working of an algorithm that finds
# an element in an sorted roateted array

# Binary search algorithm implementation
def findPos(ls, x):
    n = len(ls)
    low = 0
    high = n-1
    while(low <= high):
        mid = low + (high - low)//2
        if ls[mid] == x:
            return mid
        elif ls[mid] > ls[low]:
            if x >= ls[low] and x < ls[mid]:
                high = mid-1
            else: 
                low = mid+1
        else:
            if x > ls[mid] and x <= ls[high]:
                low = mid+1
            else:
                high = mid-1
    return -1            


# Driver function
arr = [7, 9, 10, 90, 100, 130, 140, 160, 170, 3, 5]
ans = findPos(arr,2)
if ans == -1:
	print ("Element not found")
else:
	print("Element found at index",ans)
