# Hello World program in Python
def search(l, element):
    for i in range(len(list1)):
        if list1[i] == n:
            return i
    else:
        return -1
            
if __name__ == '__main__':
    list1 = [2, 3, 7, 10, 19, 20]
    n = 8
    ans = search(list1, n)
    print(ans)
