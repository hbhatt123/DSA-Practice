

def partition(ls,l,h):
    p = ls[l]
    i = l
    j = h
    print("pivot",p)
    while (i <= j):
        while p >= ls[i]:
            i = i + 1
        while p < ls[j]:
            j = j - 1
        if i < j:
            ls[j], ls[i] = ls[i], ls[j]
    ls[l],ls[j] = ls[j],ls[l]
    return j 
def quick_sort(ls,l,h):
    if (l < h):
        j = partition(ls,l,h)
        quick_sort(ls,l,j)
        quick_sort(ls,j+1,h)
    return ls    
   
   

if __name__=='__main__':
    Lst = [10,16,8,12,1,6,3,9,5,11,4,2,21]
    n = len(Lst)
   
    res = quick_sort(Lst,0,n-1)
    print(res)
    # res = merge_sort(left,right)
    # print(res)
