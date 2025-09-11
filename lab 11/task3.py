class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_value(self, value):
        if self.head is None:
            print(f"Value {value} not found. List is empty.")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
        if current.next is None:
            print(f"Value {value} not found in the list.")
            return
        current.next = current.next.next

    def traverse(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

ll = LinkedList()
print("Traverse empty:", ll.traverse())
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
print("After inserts:", ll.traverse())
ll.delete_value(20)
print("After deleting 20:", ll.traverse())
ll.delete_value(10)
print("After deleting head (10):", ll.traverse())
ll.delete_value(30)
print("After deleting tail (30):", ll.traverse())
ll.delete_value(100)
ll.insert_at_end(5)
ll.insert_at_end(15)
print("Before deleting 99:", ll.traverse())
ll.delete_value(99)
print("After attempting to delete 99:", ll.traverse())
