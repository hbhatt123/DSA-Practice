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
        
    
    def pre_order(self):
        elements = []
        elements.append(self.data)  

        if self.left:
            elements += self.left.pre_order()
        if self.right:    
            elements += self.right.pre_order()
            
        return elements    
    
    def post_order(self):
        elements = []
        if self.left:
            elements += self.left.post_order()
        if self.right:    
            elements += self.right.post_order()
        elements.append(self.data)  
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
                
    def find_min(self):
        if self.left is None:
            return self.data
        else:
            return self.left.find_min()   
    
    def find_max(self):
        if self.right is None:
            return self.data
        else:
            return self.right.find_max()
            
    def calculate_sum(self):
        
        left_sum = 0
        right_sum = 0
        if self.left:
            left_sum =  self.left.calculate_sum()
            
        if self.right:
            right_sum = self.right.calculate_sum()
        return (self.data + left_sum + right_sum)   
        
    # def calculate_sum(self):
    #     left_sum = self.left.calculate_sum() if self.left else 0
    #     right_sum = self.right.calculate_sum() if self.right else 0
    #     return self.data + left_sum + right_sum  
    
    def delete(self, val):
        
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val> self.data:
            if self.right:
                self.right = self.right.delete(val)
                
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.left
            if self.right is None:
                return self.right
            # min_value = self.right.find_min()
            # self.data = min_value
            # self.right = self.right.delete(min_value)
            
            max_value = self.left.find_max()
            self.data = max_value
            self.left = self.left.delete(max_value)
                
        return self        
                
                
              
        
def build_tree(elements):
    root = Node(elements[0])
    
    for i in range(len(elements)):
        root.insert(elements[i])
    
    return root
    
    
if __name__ == '__main__':
    
    elements = [17,4,1,20,9,23,18,34]
    
    tree = build_tree(elements)
    print(tree.in_order())
    print(tree.search(24))
    print(tree.find_min())
    print(tree.find_max())
    print(tree.calculate_sum())
    print(tree.delete(20))
    print(tree.in_order())

    
    
