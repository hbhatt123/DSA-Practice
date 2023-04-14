# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")


class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Linkdlist:
    
    def __init__(self):
        self.head = None
        
    def traversal(self,temp):
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
            current = self.traversal(self.head)
            current.next = new_node
            
    def print(self):
        
        if self.head == None:
            print("Linkedlist is Empty")
        else:    
            current = self.head
            while current.next:
                print(current.data)
                current = current.next
            print(current.data)  
            
    def sort(self):
        
        current = self.head
        index = None
        
        if current == None:
            print("Linkedlist is empty")
        
        while current:
            index = current.next
            while index:
                if current.data > index.data:
                    current.data, index.data = index.data, current.data
                index = index.next
            current = current.next
                
    def remove_duplicates(self):
        
        current = self.head
        index = None
        
        if current == None:
            print(Linkedlist is empty)
        if current.next == None:
            return
            
        else:
            while current:
                runner = current
                while runner.next:
                    if current.data == runner.next.data:
                        runner.next = runner.next.next
                    else:
                        runner = runner.next
                current = current.next      
                
    def kth_element(self, k):
        
        current = self.head
        index = None
        count = 0
        
        if current == None:
            print("linked list is empty")
        
        while current:
            count += 1
            current = current.next   
        print("count",count)    
        if count >= k:
            temp = self.head
            for i in range(0, count-k):
                temp = temp.next
            print(temp.data)
        return temp.data
        
    def findkthelement(self,k):
        
        current = self.head 
        first = self.head 
        
        for i in range(k):
            if current is None:
                return None
            current = current.next
        # print(current.data, self.head.data)    
        while current:
            first = first.next
            current = current.next
        return first.data    
        
        
            
    def delete_midnode(self):
        
        current = self.head
        count = 0
        if current == None:
            print("linked list is empty")
        while current:
            count += 1
            current = current.next   
        print("count",count)    
        
        if count == 2:
            return
        
        current = self.head
        
        mid = int(count/2)
        
        for i in range(mid-1):
            current = current.next
        print("prev mid data",current.data)    
        current.next = current.next.next  
      
    def del_midnode_opt(self):
        
        slow = self.head
        fast = slow.next.next
        
        if slow == None:
            return 
        if slow.next.next == None:
            return
        
        while fast != None and fast.next !=None:
            slow = slow.next
            fast = fast.next.next
        print("slow",slow.data)    
        slow.next = slow.next.next  
            
        
if __name__ == '__main__':
    
    L = Linkdlist()
    L.insert(2)
    L.insert(5)
    L.insert(1)
    L.insert(11)
    L.insert(4)
    L.insert(2)
    L.insert(7)
    L.print()
    # print("after sort")
    # L.sort()
    # L.print()
    # print("remove duplicates")
    # L.remove_duplicates()
    # L.print()
    # print("kth element")
    # ans = L.findkthelement(6)
    # print(ans)
    print("delete mid node")
    L.del_midnode_opt()
    L.print()
                
                
            
