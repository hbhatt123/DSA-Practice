class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    
    def in_order(self):
        elements = []
        
        if self.left:
            elements += self.left.in_order()
            
        elements.append(self.data)  
            
        if self.right:    
            elements += self.right.in_order()
            
        return elements
    
      
    def search(self,val):
        if self.data == val:
            return True
        if val <= self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False
        
def build_tree(elements):
    root = Node(elements[0])
    
    for i in range(len(elements)-1):
        root.insert(elements[i])
    
    return root
    
    
if __name__ == '__main__':
    
    elements = [17,4,1,20,9,23,18,34]
    
    tree = build_tree(elements)
    print(tree.in_order())
    print(tree.search(24))
    
    
