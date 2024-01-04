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

def maxprofit(ls):
    n = len(ls)
    minv = ls[0]
    maxprofit = 0
    
    for i in range(n):
        # print(ls[i])
        cost = ls[i] - minv 
        maxprofit = max(cost, maxprofit)
        minv = min(ls[i], minv)
    
    print("max profit is", maxprofit)
    return maxprofit

    
    
    
if __name__ == '__main__':
    ls = [7,6,5,4,3,2,1]
    # ls = [7,1,5,3,6,4]
    
    print(max_profit(ls))
    
