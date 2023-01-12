def merge_rec(ls):
    n = len(ls)
    if n <= 1:
        return ls
    if (n >1):
        mid = n//2
        # print("mid",mid)
        # print("n",n)
        left = ls[:mid]
        right = ls[mid:]
        # print("left", left)
        # print("right",right)
        left_temp = merge_rec(left)
        print("left temp is")
        print(left_temp)
        right_temp = merge_rec(right)
        print("right temp is")
        print(right_temp)
        tmp = merge(left_temp,right_temp)
        print("temp is ")
        print(tmp)
        return tmp
   

def merge(ls1, ls2):
    i = j = k = 0
    temp = []
    n1 = len(ls1)
    n2 = len(ls2)
    # print(n1,n2)
    # print("in merge")
    # print(ls1,ls2)


    while i < n1 and j < n2:
        if ls1[i] > ls2[j]:
            temp.append(ls2[j])
            j = j+1
        else:
            temp.append(ls1[i])
            i = i+1
   
    while i < n1:
        temp.append(ls1[i])
        i = i +1
    while j < n2:
        temp.append(ls2[j])
        j = j + 1
    # print("i",i,"j",j)
    # print("temp",temp)
    return temp
   

if __name__=='__main__':
    Lst = [8,3,4,2,1,9]
    l = 0
    r = len(Lst)-1
    n = len(Lst)
    res = merge_rec(Lst)
    print(res)
    # res = merge_sort(left,right)
    # print(res)
