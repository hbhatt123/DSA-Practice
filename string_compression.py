# Maximum length of string after modifications.
MAX = 1000;
from collections import Counter

# Replaces spaces with %20 in-place and returns
# new length of modified string. It returns -1
# if modified string cannot be stored in str[]

def string_compression(s):
    result = ""
    count = 0
    ch = s[0]
    s = s + " "
    for i in s:
        print("ch", i,ch)
        if i == ch:
            count += 1
            print("count of ",ch, count)
        else:
            result = result + str(count) + str(ch)
            ch = i
            count = 1
            print(result)
        print("ch after", ch)   
        # result = result + str(count) + str(ch)
    return result     
    

    
# Driver Code
if __name__ == '__main__':
	s = "aaabbbcccdddd"
# 	s = "bdababd"
# 	s = "abba"
	ans = string_compression(s)
	print(ans)
