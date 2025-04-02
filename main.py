from data_structures.stack import Stack
from data_structures.queue import Queue

def test_stack():
    print("Testing Stack...")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack size:", stack.size())  # Should print 3
    print("Top element:", stack.peek())  # Should print 3
    print("Popped element:", stack.pop())  # Should print 3
    print("Stack size after pop:", stack.size())  # Should print 2
    print("Is stack empty?", stack.is_empty())  # Should print False


def test_queue():
    print("Testing Queue...")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Queue size:", queue.size())  # Should print 3
    print("Front element:", queue.front())  # Should print 1
    print("Dequeued element:", queue.dequeue())  # Should print 1
    print("Queue size after dequeue:", queue.size())  # Should print 2
    print("Is queue empty?", queue.is_empty())  # Should print False

if __name__ == "__main__":
    test_stack()
    test_queue()
    print("All tests passed!")