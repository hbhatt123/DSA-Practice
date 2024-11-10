# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
# max heap 
def heapify(ls,n,i):
    largest = i
    l = 2*i 
    r = 2*i +1
    
    if l < n and ls[l] > ls[largest]:
        largest = l
    if r < n and ls[r] > ls[largest]:
        largest = r
    if largest !=i:
        ls[largest],ls[i] = ls[i], ls[largest]
        heapify(ls,n, largest)
    
def insert(ls, val): #O(log n)
    ls.append(val)
    index = len(ls) - 1
    # index = index+1
    print(index,ls)
    
    while index > 0:
        parent = (index)//2
        print(ls[parent])
        
        if ls[parent] < ls[index] :
            ls[parent],ls[index] = ls[index],ls[parent]
            index = parent
        else:
            break
    return ls    
    
def delete(ls,val): # O(log n)
    n = len(ls)
    index = 0
    if not ls:
        return
    else:
        print("hi")
        for i in range(n):
            if ls[i] == val:
                index = i
        print(index,ls[-1])
        ls[index],ls[-1] = ls[-1],ls[index] # swap with last element with to be deleted element
        print(ls)
        ls.pop() # remove the last element
        print(ls)
        while index < n-1:
            l = 2*index
            r = 2*index + 1
            print(l,r)
            if l < n and ls[index] < ls[l]:
                ls[index],ls[l] = ls[l],ls[index]
                index = l
            print(index)    
            if r < n and ls[index] < ls[r]:
                ls[index],ls[r] = ls[r],ls[index]
                index = r
            else:
                return ls
        print(ls)    
        return ls        
                    
if __name__ =='__main__':
    ls = []
    print(insert(ls,50))
    print(insert(ls,55))
    print(insert(ls,53))
    print(insert(ls,52))
    print(insert(ls,54))
    print(delete(ls,55))
    
    
    
        
        
        
