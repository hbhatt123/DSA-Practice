list1 = [42, 7, 32, 1, 4, 20, 25]

def largest_ele(ls):
    count = 0
    print("length", len(ls))
    for i in range(len(ls)):
        count = 0
        for j in range(len(ls)):
            if i != j:
                print(i,j)
                if ls[i]>ls[j]:
                    count = count + 1
            print(count)
            if count == len(ls)-1:
                print(ls[i])
                return ls[i]
                    
            
if __name__ == "__main__":
    ans = largest_ele(list1)
    print(ans)
            
