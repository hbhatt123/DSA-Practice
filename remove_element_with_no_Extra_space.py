# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

def remove_elements(ls,x):
    n = len(ls)
    idx = []
    length = 0
    index = 0
    for i in range(0,n):
        print("i",i)
        if ls[i] != x:
            print(ls[i])
            ls[index] = ls[i]
            index = index + 1
            length = length + 1
        print("index",index) 
        print("len",length)

    return ls[:length], length       
            
        
    
if __name__ == '__main__':
    ls = [1,3,5,5,6]
    x = 3
    ans = remove_elements(ls,x)
    print(ans)
