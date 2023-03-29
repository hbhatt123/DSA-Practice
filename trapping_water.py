# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

def dp_sol(ls):
    n = len(ls)
    left = n*[0]
    right = n*[0]
    left[0] = ls[0]
    right[n-1] = ls[n-1]
    sum = 0
    
    for i in range(n):
        left[i] = max(left[i-1],ls[i])
    for i in range(n-2,-1,-1):
        print(i)
        right[i] = max(right[i+1],ls[i])
    for i in range(n):
        sum += min(left[i],right[i]) - ls[i]
    print(left)
    print(right)
    return sum     
    
def trap_water(ls):
    n = len(ls)
    left = n*[0]
    right = n*[0]
    left[0] = ls[0]
    l = ls[0]
    r = ls[n-1]
    for i in range(n):
        if ls[i] > l:
            left[i] = ls[i]
            l = ls[i]
        else:
            left[i] = l
    for i in range(n-1,-1,-1):
        #print("i",i)
        if ls[i] > r:
            right[i] = ls[i]
            r = ls[i]
        else:
            right[i] = r
            
    sum = 0
    print(ls)
    print(left)
    print(right)
    for i in range(n):
        sum = sum + min(left[i],right[i]) - ls[i]
        # print(sum)
    return sum
    
if __name__ == '__main__':
    ls = [1,0,2,0,1,0,3,1,0,2]
   # ans = trap_water(ls)
    ans = dp_sol(ls)
    print(ans)
            
