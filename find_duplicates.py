

    
def find_duplicate(s):
    n = len(s)
    if s =='':
        return 0
    if len(s) == 1:
        return 0
    unique = set()
    duplicate = set()
   
    for char in s:
        if char in unique:
            duplicate.add(char)
        else:
            unique.add(char)
    return duplicate        


if __name__ == "__main__":
    # Your code goes here
    s = 'abcabcaa'
    print("string",s)
    # print(longest_substring(s))
    print(find_duplicate(s))
