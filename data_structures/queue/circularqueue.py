###A circular queue, also known as a circular buffer, is a data structure that operates as a queue but utilizes a fixed-size array in a circular manner. It allows efficient insertion and deletion of elements at both ends of the queue.


class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = 0  # Index of the front element
        self.tail = 0  # Index of the next available position at the rear
        self.size = 0  # Current size of the queue

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full. Unable to enqueue.")
            return
        self.queue[self.tail] = data
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Unable to dequeue.")
            return None
        data = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return data

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[self.head]

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        idx = self.head
        elements = []
        while idx != self.tail:
            elements.append(self.queue[idx])
            idx = (idx + 1) % self.capacity
        print(elements)
queue = CircularQueue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()  # Output: [10, 20, 30]
print(queue.dequeue())  # Output: 10
queue.enqueue(40)
queue.enqueue(50)
queue.display()  # Output: [20, 30, 40, 50]
print(queue.is_full())  # Output: True
