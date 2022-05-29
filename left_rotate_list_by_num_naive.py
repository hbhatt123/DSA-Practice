# list1 = [2610, 7000, 32, 1, 4, 1610, 2500]
#list1 = [1, 2, 3, 4, 151, 26, 7, 95, 100, 20, 54]
list1 = [2,8,5,0,10,0,20,30,40]

def left_rotate(ls, n):
    num = len(ls)
    temp = []
    for k in range(n):
        # print("k", k)
        temp.append(ls[0])
        for i in range(num-1):
            # print(i,k)
            # print(temp[k])
            # print(ls[num-1])
            ls[i] = ls[i+1]
        ls[num-1] = temp[k]
    return ls
            
    
    

if __name__ == "__main__":
    ans = left_rotate(list1, 4)
    print(ans)
            
