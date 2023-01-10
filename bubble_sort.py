
def bubble_sort(ls):
    n = len(ls)
    flag = 0
    for i in range(0,n-1):
        j = i
        for j in range(0,n-1):
            if ls[j]>ls[j+1]:
                ls[j],ls[j+1] = ls[j+1], ls[j]
                flag = 1
        if flag == 0:
           break
    print(ls)    
        
        
if __name__=='__main__':
    L = [8,5,1,3,2]
    res = bubble_sort(L)
