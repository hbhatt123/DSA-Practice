# Online Python-3 Compiler (Interpreter)
print ("Hello, World!")


def leaders(ls):
    res = []
    n = len(ls)
    for i in range(n):
        for j in range(i+1, n):
            if ls[i] <= ls[j]:
                break
            if j == n-1:
                res.append(ls[i])
                print(ls[i])
    res.append(ls[n-1])
    return res        
 
if __name__ == "__main__":
    # list1 = [2,8,5,0,10,0,20,30,40]
    list1 = [1,200,13,44,115, 16, 27,8]
    ans = leaders(list1)
    print(ans)
