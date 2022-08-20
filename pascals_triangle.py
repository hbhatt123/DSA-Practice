
def pascals_triangle(num):
    res = []
    for i in range(num):
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
    return res
    
if __name__=='__main__':
    pascals_triangle(5)
            
            
        
