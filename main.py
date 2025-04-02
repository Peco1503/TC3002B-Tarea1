from data_structures.stack import Stack

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

if __name__ == "__main__":
    test_stack()