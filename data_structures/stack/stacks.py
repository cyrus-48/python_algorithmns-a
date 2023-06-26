class Stack:
    def __init__(self):
        self.items = [] 
    
    # Returns the size of the stack    
    def is_empty(self):
        return len(self.items) == 0
    
    # adds an item to the stack
    def push(self, item):
        self.items.append(item)
    
    # removes an item from the stack    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        self.items.remove(self.items[-1])
        return self.items[-1]
    # returns the top item in the stack
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]
    
    # returns the size of the stack
    def size(self):
        return len(self.items)
    
    # all the items in the stack
    
    def all_items(self):
        return self.items
    
stack = Stack()
print(stack.is_empty())
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
print(stack.peek())
print(stack.pop())
print(stack.peek())
print(stack.is_empty())
print(stack.size())
print(stack.all_items())