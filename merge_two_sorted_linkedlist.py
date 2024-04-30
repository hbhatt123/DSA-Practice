# Python3 code to Check for 
# balanced parentheses in an expression

""" Python program to merge two
sorted linked lists """
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:    
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
            
    def PrintList(self):
        temp = self.head
        llstr = ''
        while temp:
            # print(temp.data)
            llstr += str(temp.data) + '-->'
            temp = temp.next
        return llstr    
            
def merge_list(h1,h2):
    if h1 is None: return h2
    if h2 is None: return h1
    
    # A dummy node to store the result

    L3 = Node(0)
    
    # prev stores the last node
    prev = L3
     # Compare the data of the lists and whichever is smaller is
        # appended to the last of the merged list and the head is changed
    while h1 and h2:
        print(h1.data,h2.data)
        if h1.data <= h2.data:
            prev.next = h1
            h1 = h1.next
        else:
            prev.next = h2
            h2 = h2.next
            
        # Advance the tail    
        prev = prev.next
        
        # If any of the list gets completely empty
        # directly join all the elements of the other list
        if h1 != None:
            prev.next = h1
        if h2 != None:
            prev.next = h2
            
    # Returns the head of the merged list
    
    return L3.next   

        
if __name__ =='__main__':
    L1 = LinkedList()
    L1.insert(3)
    L1.insert(5)
    L2 = LinkedList()
    L2.insert(1)
    L2.insert(4)
    print(L1.PrintList())
    print(L2.PrintList())
    L1.head = merge_list(L1.head,L2.head)
    print(L1.PrintList())

                


