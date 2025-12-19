'''Solution: Design Circular Queue (Challenge 4)
Implement circular queue with fixed size.'''

class MyCircularQueue:
    def __init__(self, k):
        self.queue = [0] * k
        self.head = self.tail = -1
        self.size = k
    
    def enQueue(self, value):
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = value
        return True
    
    def deQueue(self):
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.size
        return True
    
    def isFull(self):
        return (self.tail + 1) % self.size == self.head
    
    def isEmpty(self):
        return self.head == -1
