# Maximum length of string after modifications.
MAX = 1000;

# Replaces spaces with %20 in-place and returns
# new length of modified string. It returns -1
# if modified string cannot be stored in str[]
def checkpalindrome(s, low, high):
    n = len(s)
    start = low
    end = high
	
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True  
    
def make_palindrome(s):
    
    n = len(s)
    start = 0
    end = n-1
    while start < end:
 
        # If both characters are equal then
        # move both pointer towards end
        if s[start] != s[end]:
            if checkpalindrome(s, start+1, end):
                return start
            if checkpalindrome(s, start, end-1):
                print(s[start],s[end-1])
                return end
            return -1
        start += 1
        end -= 1    
        print(start, end)    
    return -2        
                
  
# Driver Code
if __name__ == '__main__':
	s = "abcckba"
# 	s = "bdababd"
# 	s = "abba"
	ans = make_palindrome(s)
	if ans == -1:
	    print("not possibel with one character")
	elif ans == -2:
	    print("alearady palindrome")
	else:
	    print("possible by removing index", ans)

