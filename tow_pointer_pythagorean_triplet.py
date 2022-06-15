# Online Python-3 Compiler (Interpreter)
# Find if there is a triplet where a^2 + b^2 = c^2
# pythagorian triplet in sorted array

def ispair(ls,x,left,right):
    print(left,right)
    while(left < right):
        if ((ls[left]*ls[left]) + (ls[right]*ls[right])) == x:
            return True
        elif ((ls[left]*ls[left]) + (ls[right]*ls[right])) > x:
            right = right - 1
            print("right",right)
        else:
            left = left + 1
            print("left",left)
    return False
    
def ispythagorean(ls):
    n = len(ls)
    print(n)
    for i in range(n-1,0,-1):
        x = (ls[i]*ls[i])
        print("x = ", x)
        if ispair(ls,x,n-1-i,n-1):
            return True
    return False    
        
if __name__ =='__main__':
    ls = [2, 8, 2, 2, 3, 5, 6, 10]
    ans = ispythagorean(ls)
    print(ans)
