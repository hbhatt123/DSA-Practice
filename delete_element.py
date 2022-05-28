# Hello World program in Python
    
list1 = [3, 8, 12 ,5, 6]
x = 12

def delete_ele(ls, x):
    print(len(ls))
    for i in range(len(ls)):
        print(ls[i])
        if ls[i] == x:
            ls.pop(i)
            return ls
            
    return ls
            
if __name__ == "__main__":
    ans = delete_ele(list1, x)
    print(ans)
            
