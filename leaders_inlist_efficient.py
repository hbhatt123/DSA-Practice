# Online Python-3 Compiler (Interpreter)
print ("Hello, World!")


def leaders(ls):
    res = []
    n = len(ls)
    lead = ls[n-1]
    res.append(lead)
    for i in range (n-1, 0, -1):
        print(ls[i], ls[i-1])
        if lead < ls[i-1]:
            lead = ls[i-1]
            res.append(lead)
    return res
 
if __name__ == "__main__":
    list1 = [0,3, 27, 10, 9, 14, 1]
    # list1 = [2,8,5,0,10,0,20,30,40]
    # list1 = [1,200,13,44,115, 16, 27,8]
    ans = leaders(list1)
    print(ans)
