# Maximum length of string after modifications.
MAX = 1000;

# Replaces spaces with %20 in-place and returns
# new length of modified string. It returns -1
# if modified string cannot be stored in str[]
def checkpalindrome(s, low, high):
    n = len(s)
    start = low
    end = high
	
    while start <= end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True  
    
def make_palindrome(s):
    
    n = len(s)
    start = 0
    end = n-1
    while start <= end:
 
        # If both characters are equal then
        # move both pointer towards end
        if s[start] != s[end]:
            print(s[start],s[end])
            if checkpalindrome(s, start+1, end) or checkpalindrome(s, start, end-1):
                return True
            else:
                return False
                

        start += 1
        end -= 1  
    return True  
  
  
# Driver Code
if __name__ == '__main__':
	s = "aba"
# 	s = "bdababd"
# 	s = "abba"
	ans = make_palindrome(s)
	print(ans)
