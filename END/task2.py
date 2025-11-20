class PatientQueue:
    """
    A simple Queue implementation for managing patients in a hospital.
    Supports enqueue, dequeue, and peek operations.
    """

    def __init__(self):
        # List used to store patient names
        self.queue = []

    def enqueue(self, patient):
        """Add a new patient to the end of the queue"""
        self.queue.append(patient)

    def dequeue(self):
        """Remove and return the first patient in the queue"""
        if not self.queue:
            return "No patients in queue"
        return self.queue.pop(0)

    def peek(self):
        """Return the patient at the front of the queue without removing"""
        if not self.queue:
            return "Queue is empty"
        return self.queue[0]


# ----------------------------
# Test Cases
# ----------------------------

hospital = PatientQueue()

print("Enqueuing patients...")
hospital.enqueue("John")
hospital.enqueue("Alice")
hospital.enqueue("Michael")
print("Current Queue:", hospital.queue)

print("\nPeeking front patient:")
print("Front:", hospital.peek())

print("\nDequeuing patients...")
print("Dequeued:", hospital.dequeue())
print("Dequeued:", hospital.dequeue())

print("\nQueue after two removals:", hospital.queue)

print("\nPeeking again:")
print("Front:", hospital.peek())

print("\nDequeuing remaining patient...")
print("Dequeued:", hospital.dequeue())

print("\nDequeuing from empty queue:")
print("Dequeued:", hospital.dequeue())
