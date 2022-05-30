# Online Python-3 Compiler (Interpreter)
print ("Hello, World!")


def msx_diff(ls):
    n = len(ls)
    res = ls[1] - ls[0]
    minvalue = ls[2]
    for i in range(n):
       res = max(res, ls[i]-minvalue)
       minvalue = min(minvalue, ls[i])
    return res
if __name__ == "__main__":
    list1 = [10,3, 27, 10, 9, 14, 1]
    list1 = [2,3,10,6,4,8,1]
    # list1 = [2,8,5,0,10,0,20,30,40]
    # list1 = [1,200,13,44,115, 16, 27,8]
    ans = msx_diff(list1)
    print(ans)
