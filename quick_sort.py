

def partition(ls,l,h):
    p = ls[l]
    i = l
    j = h
    print("i",i,"j",j)
    print("pivot",p)
    while (i <= j):
        while i<=j and p >= ls[i]:
            i = i + 1
            print("i",i)
        while p < ls[j]:
            j = j - 1
        print("j",j)
        print(i,j)
        if i < j:
            ls[j], ls[i] = ls[i], ls[j]
    ls[l],ls[j] = ls[j],ls[l]
    print(ls)
    return j 
def quick_sort(ls,l,h):
    if (l < h):
        j = partition(ls,l,h)
        quick_sort(ls,l,j-1)
        quick_sort(ls,j+1,h)
    return ls    
   
   

if __name__=='__main__':
    Lst = [6,10,12,1]
    n = len(Lst)
    print(Lst)
   
    res = quick_sort(Lst,0,n-1)
    print(res)
    # res = merge_sort(left,right)
    # print(res)
