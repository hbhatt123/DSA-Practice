list1 = [2210, 700, 32, 1, 4, 1610, 2500]

def largest_ele(ls):
    max = ls[0]
    print("length", len(ls))
    for i in range(len(ls)):
        if ls[i] > max:
            max = ls[i]
    print(max)  
    return max

def second_largest_ele(ls):
    max = largest_ele(ls)
    print("length", len(ls))
    max1 = ls[0]
    for i in range(len(ls)):
        if ls[i] != max:
            if ls[i] > max1:
                max1 = ls[i]
    print(max1)            
            
if __name__ == "__main__":
    ans = second_largest_ele(list1)
    print(ans)
            
