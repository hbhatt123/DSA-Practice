list1 = [2610, 7000, 32, 1, 4, 1610, 2500]

def largest_ele(ls):
    first, second = -1, -1
    print("length", len(ls))
    for i in range(len(ls)):
        if ls[i] > first:
            first , second = ls[i], first
        elif first > ls[i] > second:
            second = ls[i]
    if second!= -1:
        return second
    else:
        return  none         
            

            
if __name__ == "__main__":
    ans = largest_ele(list1)
    print(ans)
            
