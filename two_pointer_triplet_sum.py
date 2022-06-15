# Online Python-3 Compiler (Interpreter)

def ispair(ls,x,left,right):
    while(left < right):
        if (ls[left] + ls[right]) == x:
            return True
        elif (ls[left] + ls[right]) > x:
            right = right - 1
        else:
            left = left + 1
    return False
    
def istriplet(ls,x):
    n = len(ls)
    for i in range(len(ls)):
        if ispair(ls,x-ls[i],i+1,n-1):
            return True
        else:
            return False
        
if __name__ =='__main__':
    ls = [2,4,6,7,9,10,12,14]
    x = 29
    n = len(ls)
    ans = istriplet(ls,x)
    print(ans)
