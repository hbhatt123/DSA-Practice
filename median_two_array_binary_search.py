# Online Python-3 Compiler (Interpreter)
# Find median of two sorted array with binary search
def median(ls1,ls2,n1,n2):
    begin = 0
    end = n1-1
    while(begin <=end):
        i1 = int((begin+end)/2)
        i2 = int((n1+n2+1)/2) - i1
        print(i1,i2)
        if i1 != n1:
            min1 = ls1[i1]
        if i1 !=0:
            max1 = ls1[i1-1]
        if i2 != n2:
            min2 = ls2[i2]
        if i2 !=0:
            max2 = ls2[i2-1]
        
        if (max1 <= min2 and max2 <= min2):
            if (n1+n2) % 2 == 0:
                return (max(max1,max2) + min(min1,min2))/2
            else:
                return max(max1,max2)
        elif (max1 > min2):
            end = i1 - 1
        else:
            begin = i1+1
            
 
if __name__ =='__main__':
    ls1 = [10, 20, 30, 40, 50]
    ls2 = [5, 15, 25, 27, 28, 55, 65, 75]
    n1 = len(ls1)
    n2 = len(ls2)
    if n1 <= n2:
        ans = median(ls1,ls2,n1,n2)
    else:
        ans = median(ls2,ls1,n2,n1)
    print(ans)
