# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

def merge_sort(ls):
    n = len(ls)
    if n >1 :
        left_ls = ls[:n//2]
        right_ls = ls[n//2:]
        
        # recursion
        merge_sort(left_ls)
        merge_sort(right_ls)
        print("l", left_ls)
        print("r", right_ls)
        # merge
        i = 0
        j = 0
        k = 0
        while i < len(left_ls) and j < len(right_ls):
            if left_ls[i] < right_ls[j]:
                ls[k] = left_ls[i]
                i += 1
                k += 1
            else:
                ls[k] = right_ls[j]
                j += 1
                k += 1
        # print("ls",ls)        
        while i < len(left_ls):
            ls[k] = left_ls[i]
            i += 1
            k += 1
        while j < len(right_ls):
            ls[k] = right_ls[j]
            j += 1
            k += 1    
            
        return ls    
if __name__=='__main__':
    ls = [1,3,2,5,4,9,6]
    ans = merge_sort(ls)
    print(ans)
    
