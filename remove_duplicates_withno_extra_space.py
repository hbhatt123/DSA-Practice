def remove_duplicates(ls):
    n = len(ls)
    idx = []
    print👎
    length = 1
    index = 1
    prev = ls[0]
    for i in range(1,n):
        if ls[i] != prev:
            length = length + 1
            prev = ls[i]
            ls[index] = ls[i]
            index = index + 1
            
    return length
  
  if __name__ == '__main__':
    ls = [1,1,2,2,3,4,5,5]
    
    ans = remove_duplicates(ls)
    print(ans)
