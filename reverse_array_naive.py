# list1 = [2610, 7000, 32, 1, 4, 1610, 2500]
list1 = [1, 2, 3, 4, 151, 26, 7, 95, 100, 20, 54]

def reverse(ls):
    n = len(ls)
    # print(n)
    for i in range(n-1):
        temp = 0
        print(n-1-i)
        if n-1-i >= n/2:
            print(ls[i], ls[n-1-i])
            temp = ls[n-1-i]
            ls[n-1-i] = ls[i]
            ls[i]= temp
    return ls        
            
    
if __name__ == "__main__":
    ans = reverse(list1)
    print(ans)
            
