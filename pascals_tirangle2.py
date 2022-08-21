# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")


def pascals_triangle(num):
    res = []
    for i in range(num+1):
        print("i",i)
        if i == 0:
            res.append([1])
            continue

        res.append([1])
        ls = res[i - 1]
        print(res)
        for j in range(1,len(ls)):
            res[-1].append(ls[j - 1] + ls[j])
        res[-1].append(1) 
    print(res)    
    return res[num]
    
if __name__=='__main__':
    ans = pascals_triangle(1)
    print(ans)
            
            
        
