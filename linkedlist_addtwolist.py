
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    
    def __init__(self):
        self.head = None
        
    def insert(self,data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
         
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
        
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev
        
        return
        
        
    def addlist(self,X,Y):
        head = None
        prev = None
        carry = 0
        print(carry)
        
        X = X.head
        Y = Y.head
        while X or Y:
            total = 0
            
            if X:
                total += X.data
                
            if Y:
                total += Y.data
                
            total += carry    
                
            print("sum", total)    
            
            # if the sum of a 2–digit number, reduce it and update carry
            carry = total // 10
            total = total % 10
            print("carry",carry)
            print("total",total)
            # create a new node with the calculated sum
            node = Node(total)
    
            # if the output list is empty
            if head is None:
                # update `prev` and `head` to point to the new node
                prev = node
                head = node
            else:
                # add the new node to the output list
                prev.next = node
    
                # update the previous node to point to the new node
                prev = node
                
            # advance `X` and `Y` for the next iteration of the loop
            X = X.next if X else X
            Y = Y.next if Y else Y

        if carry:
            prev.next = Node(carry)
    
        return head
        
    def sum(self, l1, l2):
        
        # l1 = l1.reverse()
        # l2 = l2.reverse()
        
        l1.reverse()
        l2.reverse()
        l1.printlist()
        
        q1 = []
        q2 = []
        
        head = l1.head
        while head:
            q1.append(head.data)
            head = head.next
        tail = l2.head 
        while tail:
            q2.append(tail.data)
            tail = tail.next
            
        print(q1)
        print(q2)
        # sum = []
        
        # for i in range(len(q1)):
        #     sum.append(q1[i] + q2[i])
        q1 = [str(i) for i in q1]
        s1 = int("".join(q1[::-1]))
        q2 = [str(i) for i in q2]
        s2 = int("".join(q2[::-1]))
        s = s1+s2
        s = [i for i in str(s)]
        s = s[::-1]
        print(s1)
        
        ll_sum = Linkedlist()
        for i in s:
            ll_sum.insert(i)
            
        # ll_sum.reverse()
        
        ll_sum.printlist()
        print()
            
     
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data,end= ' ')
            temp = temp.next
            
            
if __name__=='__main__':
    
    print("first digit", 57 // 10)
    print("second digit", 57 % 10)
    
    LL = Linkedlist()
    L = Linkedlist()
    R = Linkedlist()
    # L.insert(2)
    # L.insert(3)
    # L.insert(1)
    # L.printlist()
    # print("revers list")
   
    ls1 = [7, 1, 6]
    ls2 = [2, 9, 5]
    
    
    for i in range(len(ls1)):
        L.insert(ls1[i])
    for i in range(len(ls2)):
        R.insert(ls2[i])
    L.printlist()
    print('')
    R.printlist()
    print('')
    # L.reverse()
    # L.printlist()
    # print('')
    ans = LL.addlist(L,R)
    LL.printlist()
    print()

        
    
            
