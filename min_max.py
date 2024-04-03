
def min_max(ls):
    n = len(ls)
    min = ls[0]
    max = ls[0]
    for i in range(n):
        print(i)
        if ls[i] < min:
            min = ls[i]
        if ls[i] > max:
            max = ls[i]
            
    return min, max
    
if __name__ == '__main__':  
    ls = [2,3,5,-1,10,60]
    min, max = min_max(ls)
    print(min,max)
