# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

def permutation_string(s1,s2):
    #big(o) = n^2 log n
    n1 = len(s1)
    n2 = len(s2)
    if n1 > n2 or n2 >= 10000:
        return False
    if n1 == 1:
        if s1[0] in s2:
            return True
    for i in range(0,n2-1): # n
        print(s2[i:i+n1])
        s3 = s2[i:i+n1]
        x = sorted((s1)) # nlogn
        y = sorted((s3))
        print("x",x)
        print("y",y)
        if x == y:
            print("True")
            return True
    return False  
    
def permutation_string_2(s1,s2):
    # Big(0) = n
    n1 = len(s1)
    n2 = len(s2)
    lookup1 = [ord(i) - ord('a') for i in s1]
    lookup2 = [ord(i) - ord('a') for i in s2]
    print(lookup1)
    
    target = [0] * 26
    window = [0] * 26
    
    for i in lookup1:
        print(i)
        target[i] += 1
    print("target",target)  
    for i, s in enumerate(lookup2):
        print("s",s, n1, i)
        window[s] += 1
        print(window)
        if i >= n1: # window size exceeded
            rem = i - n1
            print("rem", rem)
            window[lookup2[rem]] -= 1
            print("window")
            print(window)
        if window == target:
            return True
    return False        
        
    
    
    
    
    
if __name__ =='__main__':
    s1 = 'ab'
    s2 = "eiabooo"
    ans = permutation_string_2(s1,s2)
    print(ans)
    
    
