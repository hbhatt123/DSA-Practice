class Stack():
    
    def push(self,l):
        ls.append(l)
        n = len(ls)
        top = n-1
        return ls, top
        
    def pop(self):
        n = len(ls)
        if n > 0:
            del ls[n-1]
            return ls
        else:
            return "List is empty"
        
class Queue():
    def enqueue(self,l):
        ls.append(l)
        n = len(ls)
        rare = 0
        first = n-1
        return ls, first, rare
        
    def dequeue(self):
        n = len(ls)
        if n >= 0:
            del ls[0]
            n = len(ls)
            first = n-1
            rare = 0
            return ls, first, rare
        else:
            return "List is empty"
        
        
s = Stack()
q = Queue()
ls = []
print(q.enqueue(1))
print(q.enqueue(3))
print(q.enqueue(9))
print(q.dequeue())
# print(s.push(1))
# print(s.push(3))
# print(s.pop())
# print(s.pop())
# print(s.pop())
