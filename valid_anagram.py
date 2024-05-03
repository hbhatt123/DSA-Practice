# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
# from collection import counter
def valid_anagram1(s,t): #time-O(n) space-O(1)
    
    if len(s) != len(t):
        return True
    else:    
        s_dict = counter(s)
        t_dict = counter(t)
        
        
        return s_dict == t_dict

def check(s,t):
    if len(s) != len(t):
        return False
    else:
        return sorted(s) == sorted(t)
        
def valid_anagram(s1,s2): # O(n)
    
    dict_val = {}
    dict_val2 = {}
    if len(s1) != len(s2):
        return False
    else:
        for c in s1:
            if c not in dict_val:
                dict_val[c] = 1
            else:
                dict_val[c] += 1
    print(dict_val)        
    for c in s2:
        if c in dict_val:
            dict_val[c] -= 1
        else:
            return False
        
    print(dict_val)        
    for val in dict_val.values():
        if val ==0:
            return True
        else:
            return False
        
    
    
    
if __name__ == '__main__':
    s1 = "anagram"
    s2 = "nagaram"
    
    print(check(s1,s2))
    
    
    
   
   

    
    
