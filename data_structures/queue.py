class Queue:
    def __init__(self):
        self._queue = []

    def enqueue(self, element):
        """Add element to the end of the queue"""
        self._queue.append(element)
        print(f"Added successfully {element} to the queue")

    def dequeue(self):
        """Remove element at the top of the queue"""
        if not self._queue:
            print(" Queue is empty")
            return None
        return self._queue.pop(0)
    
    def front(self):
        """Get the front element of the queue"""
        if not self._queue:
            return None
        return self._queue[0]
    
    def is_empty(self):
        """Check if queue is empty"""
        return len(self._queue) == 0
    
    def size(self):
        """Check queue length"""
        return len(self._queue)