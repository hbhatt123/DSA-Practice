# list1 = [2610, 7000, 32, 1, 4, 1610, 2500]
#list1 = [1, 2, 3, 4, 151, 26, 7, 95, 100, 20, 54]
list1 = [20, 10, 20, 10, 30, 10, 20, 40, 60, 30]

def remove_duplicates(ls):
    res = []
    
    for i in ls:
        if i not in res:
            res.append(i)
                    
    return res        

if __name__ == "__main__":
    ans = remove_duplicates(list1)
    print(ans)
            
