# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world") 
# Node class
class Node:
    # Function to initialize the node object
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linkedlist:
    #Function to initialize the linkedlist objects
    def __init__(self):
        self.head = None
        
    def traversal(self,temp):
        while temp.next:
            temp = temp.next   
        return temp    
        
    def insert(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.traversal(self.head)
            temp.next = new_node
     
    def insert_after(self, prev_node, data):
        new_node = Node(data)
        print(new_node)
        if prev_node == None:
            print("Previous Node is not present in LinkedList")
        else:
            temp = prev_node.next
            prev_node.next = new_node
            new_node.next = temp
            
        
    def search(self,data):
        if self.head.data == data:
            return True
        else:
            temp = self.head.next
            while temp is not None:
                if temp.data == data:
                    return True
                else:
                    temp = temp.next
        return False
        
     # Print the linked list
    def printList(self):
        temp = self.head
        while temp.next:
            print(temp.data)
            #print(temp.next)
            temp = temp.next
        print(temp.data)    
    
    def delete(self,data):
        if self.head==None:
            return "LinkedList is Empty"
        if self.head.data == data:
            self.head = self.head.next
        current =  self.head   
        while current:
            print("current loop",current.data,current.next)
            if current.data == data:
                break
            prev = current
            current = current.next
        if current is None:
            print("Data not found")
        else:
            prev.next = current.next
            

    def sorting1(self):
        if self.head == None:
            return "LinkedList is Empty"
            
        current=self.head
        while(current!=None):
            index=current.next
            while(index!=None):
                if(current.data>index.data):
                    n=index.data
                    index.data=current.data
                    current.data=n
                index=index.next
            current=current.next
        
    def sorting(self):
        
        if self.head == None:
            return "LinkedList is Empty"
            
        current = self.head 
        index = None
        
        while current:
            index = current.next
            while index != None:
                if current.data > index.data:
                    current.data, index.data = index.data, current.data
                else:
                    index = index.next
            current = current.next  
  

    def remove_duplicates(self):
        # o(n)
        if self.head == None:
            return "LinkedList is Empty"
            
        if self.head.next == None:
            return
        
        current = self.head
        prev = None
        d ={} # check in d -> o(1)
        
        while current:
            if current.data in d:
                prev.next = current.next
                current = current.next
            else:
                d[current.data] = 1
                prev = current
            current = current.next  
            
    def remove_duplicates_woextraspace(self):
        
        # o(n^2)
        
        if self.head == None:
            return "LinkedList is Empty"
        if self.head.next == None:
            return
        
        current = self.head

        while current:
            runner = current
            # Check until runner.next is not None.
            while runner.next:
                if current.data == runner.next.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next   
        
if __name__ == "__main__":
    L = Linkedlist()
    L.insert(2)
    L.insert(3)
    L.insert(4)
    L.insert(2)
    L.insert_after(L.head.next,12)
    L.printList()
    # L.delete(2)
    print("final linkedlist")
    L.printList()
    # ans = L.search(13)
    # print(ans)
    print("sorting the linkelist")
    L.sorting()
    
    L.printList()
    print("remove duplicates")
    L.remove_duplicates_woextraspace()
    L.printList()


    
