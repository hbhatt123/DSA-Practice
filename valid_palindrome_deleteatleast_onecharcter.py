# Python3 code to Check for 
# balanced parentheses in an expression

def isPalindrome(s,l,r):
    
    while l<r:
        if s[l] == s[r]:
           l = l+1
           r = r-1
        else:
            return False
    print(s)        
    return True        
           
            
def isPalindrome2(s):
    #Given a string s, return true if the s can be palindrome after deleting at most one character from it.
    
    n = len(s)
    l = 0
    r = n-1

    while l<r:
        if s[l] == s[r]:
            l = l+1
            r = r-1
        else:
            return isPalindrome(s,l+1,r) or isPalindrome(s,l,r-1)
    return True
 
if __name__ =='__main__':
    s = 'abca'
    ans = isPalindrome2(s)
    print(ans)
