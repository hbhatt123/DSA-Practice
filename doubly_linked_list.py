class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLinkedlist:
    
    def __init__(self):
        self.head = None
        
    def insert(self,data):
        if self.head == None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
         
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None
        
    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None
    
            
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            
            
if __name__=='__main__':
    
    L = DLinkedlist()
    L.insert(2)
    L.insert(3)
    L.insert(1)
    L.printlist()
    
            
