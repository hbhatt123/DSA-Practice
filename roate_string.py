def string_rotate(s1, s2):
    if s1 == s2:
        print("here")
        return True
    if len(s1) != len(s2):
        return False
    temp = []    
    k = ""
    val =""
    start = 0
    end = len(s2)
    while start < end:
        print("start",start,k)
        val = s1[start:end]
        val = val + k
        print(len(k))
        print(val,s2)
        start += 1
        k = k +"".join(s1[start-1])
        if val == s2:
            return True
    return False      
            

if __name__ == "__main__":
    list1 = [2,8,5,0,10,0,20,30,40]
    s1 = "waterbottle"
    s2 = "erbottlewat"
    
    ans = string_rotate(s1, s2)
    print(ans)
            
