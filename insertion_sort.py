def insertion_sort(ls):
    for i in range(1,len(ls)):
        x = ls[i]
        j = i-1
        while (j>-1 and ls[j] > x):
            ls[j+1] = ls[j]
            j = j-1
        ls[j+1] = x  
    return ls    
                
   

if __name__=='__main__':
    Lst = [8,3,4,2,11,9]
   
    res = insertion_sort(Lst)
    print(res)
    # res = merge_sort(left,right)
    # print(res)
