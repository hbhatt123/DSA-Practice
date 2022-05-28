list1 = [2210, 7000, 32, 1, 4, 1610, 25]

def largest_ele(ls):
    max = ls[0]
    print("length", len(ls))
    for i in range(len(ls)):
        if ls[i] > max:
            max = ls[i]
    return max    
            
if __name__ == "__main__":
    ans = largest_ele(list1)
    print(ans)
            
