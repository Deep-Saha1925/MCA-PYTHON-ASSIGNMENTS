class Stack:
    
    # Constructor
    def __init__(self, size):
        self.l = []
        self.max = size
        self.top = -1

    # Push operation
    def Push(self, item):
        if self.top == self.max - 1:
            print("Stack Overflow")
            return
        self.l.append(item)
        self.top += 1

    # Traverse (Display)
    def Traverse(self):
        if self.top == -1:
            print("Stack is Empty")
            return
        print("Stack elements:")
        for i in range(self.top, -1, -1):
            print(self.l[i])

    # Pop operation
    def Pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return None
        item = self.l.pop()
        print(f"{item} popped")
        self.top -= 1
        return item


# MAIN
s = Stack(5)

s.Push(1)
s.Push(2)
s.Push(3)
s.Push(4)
s.Push(5)

s.Traverse()

s.Pop()

s.Traverse()