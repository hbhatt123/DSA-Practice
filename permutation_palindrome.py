# Maximum length of string after modifications.
MAX = 1000;

# Replaces spaces with %20 in-place and returns
# new length of modified string. It returns -1
# if modified string cannot be stored in str[]

def permutation_palindrome(s):
    n = len(s)
    s = s.lower()
    char_set = {}
    for i in s:
        if i in char_set:
            char_set[i] += 1
        else:
            char_set[i] = 1
    odd_counter = 0
    has_odd = False
    print(char_set)
    
    for k,v in char_set.items():
        print(k,v)
        print("odd_counter", odd_counter)
        if v % 2 != 0 and odd_counter == 0:
            print("hi")
            odd_counter += 1
            has_odd = True
        elif v % 2 != 0 and has_odd:
            return False
    return True        

# Driver Code
if __name__ == '__main__':
	s = "travel"
# 	s = "bdababd"
# 	s = "abba"
	ans = permutation_palindrome(s)
	print(ans)
