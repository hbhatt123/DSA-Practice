# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Linkedlist:
    
    def __init__(self):
        self.head = None
        
    def traversal(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        return temp    
            
    def insert(self,data):
        
        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node
            self.next = None
        else:
            current = self.traversal()
            current.next = new_node
            
    def printlist(self):
        
        if self.head == None:
            print("linkedlist is empty")
        temp = self.head 
        while temp:
            print(temp.data)
            temp = temp.next
            
    def findkthelement(self, k):
        
        current = self.head
        first = self.head
        for i in range(k):
            if current is None:
                return None
            current = current.next
        
        while current:
            first = first.next
            current = current.next
        return first.data    
        
    def sorting(self):
        
        current = self.head
        if current == None and current.next == None:
            return current
        
        while current:
            index = current.next
            while index:
                if current.data > index.data:
                    current.data, index.data = index.data, current.data
                index = index.next
            current = current.next
                
                
    def remove_duplicates(self):
        
        current = self.head

        if current == None:
            print("linkedlist is empty")
            
        while current:
            runner = current
            while runner.next:
                if current.data == runner.next.data:
                    runner.next = runner.next.next
                else:    
                    runner = runner.next
            current = current.next  
            
    def delete_midnode(self):
        slow = self.head
        fast = slow.next.next
        
        if slow == None:
            print("linkedlist is empty")
            
        while fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next    
        
        
    def partition(self, n):
        left = Linkedlist()
        right = Linkedlist()
        current = self.head
        while current:
            print("current data", current.data)
            if current.data >= n:
                right.insert(current.data)
            else:
                left.insert(current.data)
            current = current.next
        print("first")
        print(right.printlist())
        print("Second")
        print(left.printlist())

        ls1 = left.head
        ls2 = right.head
        print(ls1.data, ls2.data)
        while ls1.next:
            ls1 = ls1.next
        ls1.next = ls2
        print("final linkedlist")
        left.printlist()
        return left
        

if __name__ =='__main__':
    L = Linkedlist()
    L.insert(2)
    L.insert(3)
    L.insert(6)
    L.insert(9)
    L.insert(1)
    L.insert(6)
    L.insert(4)
    # L.printlist()
    # ans = L.findkthelement(3)
    # print("kth element from last", ans)
    # print("sorted list")
    # L.sorting()
    # L.printlist()
    # print("remove duplicates")
    # L.remove_duplicates()
    # L.printlist()
    # print("remove mid node")
    # L.delete_midnode()
    # L.printlist()
    print("partitioning linkedlist")
    L.partition(4)
    # L.concat(left, right, tail)
    # left.printlist()
            
        
