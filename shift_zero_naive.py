# list1 = [2610, 7000, 32, 1, 4, 1610, 2500]
#list1 = [1, 2, 3, 4, 151, 26, 7, 95, 100, 20, 54]
list1 = [0,8,5,0,10,0,20,0,0]

def shift_zeros(ls):
    n = len(ls)
    for i in range(n-1):
        temp = -1
        if ls[i] == 0:
            for j in range(n-1):
                if ls[j] == 0:
                    temp = ls[j+1]
                    ls[j+1] = ls[j]
                    ls[j] = temp
    return ls        

if __name__ == "__main__":
    ans = shift_zeros(list1)
    print(ans)
            
