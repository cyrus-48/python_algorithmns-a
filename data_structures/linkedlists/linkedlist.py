class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head  =None
        
    def is_empty(self):
        return self.head is None
    
    def append(self , data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def   insert_after(self , prev_node , data):
        if notprev_node:
            return
        
        new_node = Node(data)
        new_node.next = prev_node.next 
        prev_node.next = new_node
        
        
    def delete(self , data):
        if self.is_empty():
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current .next = current.next.next
                return
            current =current.next
            
    def search(self ,data):
        current = self.head
        while current:
            if current.data == data:
                return True
            
            current = current.next
            
        return False
    
    def display(self):
        elements = []
        current  = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)
        
        
        
link_list = LinkedList()
link_list.append(10)
link_list.append(20)
link_list.append(30)
link_list.append(40)
link_list.display()
link_list.delete(20)
link_list.display()
print(link_list.search(30))
print(link_list.search(15))
                
                