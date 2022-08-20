# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

def insertion_sort(ls):
    n = len(ls)
    for i in range(1,n):
        j = i
        while ls[j-1] > ls[j]:
            ls[j-1], ls[j] = ls[j], ls[j-1]
            j -= 1
    return ls        
if __name__=='__main__':
    ls = [1,3,2,5,4,9,6]
    ans = insertion_sort(ls)
    print(ans)
    
