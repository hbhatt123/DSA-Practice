# Online Python-3 Compiler (Interpreter)

def ispair(ls,x):
    n = len(ls)
    left = 0
    right = n-1
    while(left < right):
        if (ls[left] + ls[right]) == x:
            return ls[left], ls[right]
        elif (ls[left] + ls[right]) > x:
            right = right - 1
        else:
            left = left + 1
    return -1

def twosum(ls,target):
    map_val = {}
    
    for i,n in enumerate(ls):
        more = target - n
        if more in map_val:
            return (map_val[more],i)
            print(map_val)
        else:
            map_val[n] = i
if __name__ =='__main__':
    ls = [2,4,6,7,9,10,12,14]
    x = 24
    ans = ispair(ls,x)
    print(ans)
