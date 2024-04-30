# Python3 code to Check for 
# balanced parentheses in an expression
open_list = ["[","{","("]
close_list = ["]","}",")"]
mapp = {")":"(","}":"{","]":"["}

# Function to check parentheses
def check(myStr):
	stack = []
	for i in myStr:
		if i in mapp.values():
		    stack.append(i)
		elif stack and mapp[i] == stack[-1]:
		    print(mapp[i],i)
		    stack.pop()
		else:
			return "Unbalanced"
	if len(stack) == 0:
		return "Balanced"
	else:
		return "Unbalanced"
		
def check_1(s):
    stack = []
    for c in s:
        if c == "(" or c == "{" or c == "[":
            stack.append(c)
        elif stack:
            if c == ")" or c == "}" or c == "]":
                if stack[-1] == "(" or stack[-1] == "{" or stack[-1] =="[" :
                    stack.pop()
    if len(stack) == 0:
	    return "Balanced"
    else:
        return "Unbalanced"                
                    


# Driver code
string = "{[]{()}}"
print(string,"-", check_1(string))

string = "[{}{})(]"
print(string,"-", check(string))

string = "((()"
print(string,"-",check(string))
