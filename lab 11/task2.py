class QueueList:
    def __init__(self):  
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)

    def is_empty(self):
        return len(self._items) == 0


from collections import deque

class QueueDeque:
    def __init__(self):  
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def is_empty(self):
        return len(self._items) == 0


# Testing both queues
print("Testing QueueList:")
q1 = QueueList()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print("Dequeue:", q1.dequeue())  
print("Dequeue:", q1.dequeue())  
print("Is empty?", q1.is_empty())  
print("Dequeue:", q1.dequeue())  
print("Is empty?", q1.is_empty())  

print("\nTesting QueueDeque:")
q2 = QueueDeque()
q2.enqueue("A")
q2.enqueue("B")
q2.enqueue("C")
print("Dequeue:", q2.dequeue())  
print("Dequeue:", q2.dequeue())  
print("Is empty?", q2.is_empty())  
print("Dequeue:", q2.dequeue())  
print("Is empty?", q2.is_empty())  
