# Online Python-3 Compiler (Interpreter)
# Find median of two sorted array with binary search
def repeat_element(ls):
    n = len(ls)
    res = set()
    for i in range(n):
        if ls[i] in res:
            print("value already in list = ",ls[i])
            break
        res.add(ls[i])
     
 
if __name__ =='__main__':
    ls1 = [10, 20, 30, 40, 50]
    ls2 = [5, 15, 25, 27, 28, 55, 65, 75]
    ls = [0,2,3,2,3,4,5,7]
    ans = repeat_element(ls)
    print(ans)
