# list1 = [2610, 7000, 32, 1, 4, 1610, 2500]
#list1 = [1, 2, 3, 4, 151, 26, 7, 95, 100, 20, 54]

def reverse(ls, start, end):
    while (start < end):
        temp = ls[start]
        ls[start] = ls[end]
        ls[end] = temp
        start += 1
        end = end-1 
    return ls       
    

def leftRotate(arr, d):
    n = len(arr)
    reverse(arr, 0, d-1)
    reverse(arr, d, n-1)
    reverse(arr, 0, n-1)
    return arr


if __name__ == "__main__":
    # list1 = [2,8,5,0,10,0,20,30,40]
    list1 = [1,2,3,4,5, 6, 7,8]
    ans = leftRotate(list1, 3)
    print(ans)
