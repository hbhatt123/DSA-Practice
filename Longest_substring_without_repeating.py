
def longest_substring(s):
    ans = 0
    dic = {}
    st = ''
    for i in range(len(s)):
        if s[i] not in st:
            st += s[i]
            dic[s[i]] = i
            # print(st)
            print("dic",dic)
        else:
            ans = max(len(st), ans)
            j = dic[s[i]]
            print("ans",ans,"j",j)
            st = s[j+1:i+1]
            dic[s[i]] = i
            print("i",i)
        print("s",s[i])
        print("st", st)    
    ans = max(len(st), ans)
    return ans
    
def hash_map_sol(s):
    n = len(s)
    if s =='':
        return 0
    if len(s) == 1:
        return 1
    hashmap = set()
    start = 0
    max_len = 0
    i = 0
    while (i < n):
        if s[i] not in hashmap:
            hashmap.add(s[i])
            max_len = max(max_len,len(hashmap))
            i += 1
        else:
            hashmap.remove(s[start])
            start += 1
    return max_len        
            



if __name__ == "__main__":
    # Your code goes here
    s = 'abcabcaa'
    print("string",s)
    # print(longest_substring(s))
    print(hash_map_sol(s))
