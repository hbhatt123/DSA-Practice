# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
def merge(intervals):
        if(len(intervals) == 0):
            return intervals
        # print(intervals,"before")    
        # intervals.sort()
        op = []
        print(intervals)
        start = intervals[0][0]
        end = intervals[0][1 ]
        print(start,end)
        # print(intervals[0][0])
        # temp_int = intervals[0]
        for i in intervals:
            print(i[0],i[1])
            if(i[0]<=end):
                end = max(i[1],end)
                print("end",end)
            else:
                op.append([start,end])
                start = i[0]
                end = i[1]
        op.append([start,end])
        return op
        
if __name__=='__main__':
    ls = [[1,3],[2,6],[8,10],[15,18]]
    # ls = [[1,4],[4,5]]
    # ls = [[1,4],[5,6]]
    # ls = [[1,2]]
    ans = merge(ls)
    print(ans)        
