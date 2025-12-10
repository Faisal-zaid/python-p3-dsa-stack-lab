class Stack:

    def __init__(self, items=None, limit=100):
        # Avoid using a mutable default value
        self.items = list(items) if items else []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.full():
            raise OverflowError("Stack is full")
        self.items.append(item)
        return self

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    # BONUS METHODS
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        """
        Return distance from the top:
           top index = last element
           if found at top → return 0
           else return distance
           else return -1
        """
        if target not in self.items:
            return -1
        
        # Position counting from the top
        return (len(self.items) - 1) - self.items.index(target)
