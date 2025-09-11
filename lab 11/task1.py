class Stack:
    def __init__(self):
        self._items = []
    def push(self, item):
        self._items.append(item)
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._items[-1]
    def is_empty(self):
        return len(self._items) == 0
if __name__ == "__main__":
    s = Stack()
    print("Is stack empty?", s.is_empty()) 

    print("\nPushing elements: 10, 20, 30")
    s.push(10)
    s.push(20)
    s.push(30)

    print("Top element (peek):", s.peek())
    print("Is stack empty?", s.is_empty())  
    print("\nPopping elements:")
    print(s.pop()) 
    print(s.pop())  
    print("Top element after pops:", s.peek()) 
    print("Is stack empty?", s.is_empty())  
    print("Popping last element:", s.pop()) 
    print("Is stack empty now?", s.is_empty())  

