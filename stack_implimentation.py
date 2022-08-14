# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# print("Hello world")
class Stack(object):
    def __init__(self):
        self.items = []
    def push(self,item):
        return self.items.append(item)
    def IsEmpty(self):
        return self.items==[]
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
        
if __name__ == '__main__':
    
    s = Stack()
    print(s.IsEmpty())
    print(s.push(1))
    print(s.push(2))
    print(s.peek())
    print(s.size())
    print(s.pop())
    ls = [1,3,5,5,6]
    x = 3
    # ans = remove_elements(ls,x)
    # print(ans)
