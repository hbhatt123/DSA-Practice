# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

def max_profit(ls):
    n = len(ls)
    
    buy = ls[0]
    max_profit = 0
    i = 1
    
    while i < n:
        print(i)
        if ls[i] < buy:
            buy = ls[i]
        elif max_profit < ls[i] - buy:
            max_profit = ls[i] - buy
        i = i + 1  
    return max_profit
    
    
    
if __name__ == '__main__':
    ls = [7,6,5,4,3,2,1]
    # ls = [7,1,5,3,6,4]
    
    print(max_profit(ls))
    
