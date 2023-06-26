class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]
    
    def display(self):
        return self.queue
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.peek())  # Output: 10
print(queue.dequeue())  # Output: 10
print(queue.dequeue())  # Output: 20
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)
print(queue.is_empty())  # Output: False
print(queue.display())  # Output: [30]
