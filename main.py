from data_structures.stack import Stack
from data_structures.queue import Queue
from data_structures.hashtable import HashTable

def test_stack():
    print("\n===== Testing Stack (LIFO) =====")
    stack = Stack()

    print("\n Pushing elements onto the stack")
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("\n Current stack size:", stack.size())  # Should be 3
    print("\n Top element (peek):", stack.peek())  # Should be 3

    print("\n Popping the last pushed element")
    popped = stack.pop()
    print(" Popped element:", popped)  # Should be 3

    print("\n Stack size after pop:", stack.size())  # Should be 2
    print("\n Checking if stack is empty")
    print(" Is the stack empty?:", stack.is_empty())  # Should be False

    print("\n Popping all elements")
    stack.pop()
    stack.pop()
    stack.pop()
    print(" Popping from empty stack:", stack.pop())  # Should handle empty case
    print(" Peeking into empty stack:", stack.peek())  # Should return None


def test_queue():
    print("\n===== Testing Queue (FIFO) =====")
    queue = Queue()

    print("\n Enqueuing elements into the queue")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("\n Current queue size:", queue.size())  # Should be 3
    print("\n Front element:", queue.front())  # Should be 1

    print("\n Dequeuing the first enqueued element")
    dequeued = queue.dequeue()
    print(" Dequeued element:", dequeued)  # Should be 1

    print("\n Queue size after dequeue:", queue.size())  # Should be 2
    print(" Is the queue empty?:", queue.is_empty())  # Should be False

    print("\n Dequeuing remaining elements")
    queue.dequeue()
    queue.dequeue()
    print(" Dequeuing from empty queue:", queue.dequeue())  # Should handle empty

    print(" Front of empty queue:", queue.front())  # Should return None


def test_hashtable():
    print("\n===== Testing HashTable / Dictionary =====")
    hashtable = HashTable()

    print("\n Inserting key-value pairs...")
    hashtable.insert("a", 1)
    hashtable.insert("b", 2)
    hashtable.insert("c", 3)

    print(" Current hashtable size:", hashtable.size())  # Should be 3
    print(" Value for key 'b':", hashtable.get("b"))  # Should be 2

    print("\n Deleting key 'b'")
    hashtable.delete("b")

    print(" Hashtable size after deletion:", hashtable.size())  # Should be 2
    print(" Current keys:", hashtable.keys())  # Should be ['a', 'c']
    print(" Current values:", hashtable.values())  # Should be [1, 3]

    print("\n Trying to get a missing key:")
    print(" Value for key 'z':", hashtable.get("z"))  # Should return None

    print("\n Trying to delete a missing key:")
    hashtable.delete("z")  # Should handle gracefully


if __name__ == "__main__":
    print("\n Running data structure tests...\n")
    test_stack()
    test_queue()
    test_hashtable()
    print("\n All tests completed successfully!")