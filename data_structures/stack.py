class Stack:
    def __init__(self):
        # Inicializar lista vacia para almacenar los objetos
        # stack re
        self._stack = []

    def push(self, element):
        """Add element on the stack"""
        self._stack.append(element)
        print(f"Added successfully {element} to the stack")

    def pop(self):
        """Remove element from the stack"""
        if not self._stack:
            print("Stack is empty")
            return None
        return self._stack.pop()
    
    def peek(self):
        """Check last element without removing it"""
        if not self._stack:
            return None
        else:
            return self._stack[-1]
        
    def is_empty(self):
        """Check if stack is empty"""
        return len(self._stack) == 0
    
    def size(self):
        """Return stack lenght"""
        return len(self._stack)