# list1 = [2610, 7000, 32, 1, 4, 1610, 2500]
list1 = [1, 2, 3, 4, 151, 26]

def is_sorted(ls):
    flag = True
    for i in range(len(ls)-1):
        if ls[i] > ls[i+1]:
            print(i)
            flag = False
    if flag ==True:
        print("sorted array")
    else:
        print("unsorted")

if __name__ == "__main__":
    ans = is_sorted(list1)
    print(ans)
            
