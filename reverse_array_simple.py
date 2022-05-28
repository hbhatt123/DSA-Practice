# list1 = [2610, 7000, 32, 1, 4, 1610, 2500]
list1 = [1, 2, 3, 4, 151, 26, 7, 95, 100, 20, 54]

def reverse(ls):
    n = len(ls)
    temp = 0
    low = 0
    high = n-1
    while (low < high):
        temp = ls[high]
        ls[high] = ls[low]
        ls[low]= temp
        low +=1
        high-=1
    return ls    

if __name__ == "__main__":
    ans = reverse(list1)
    print(ans)
            
