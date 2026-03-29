class SqStack:
    def __init__(self, max_size=8):
        self.base = [None] * max_size  # 栈底
        self.top = 0  # 栈顶指针，指向下一个插入位置
        self.stacksize = max_size

    def is_empty(self):
        return self.top == 0

    def is_full(self):
        return self.top >= self.stacksize

    def push(self, element):
        if self.is_full():
            raise OverflowError("Stack overflow")
        self.base[self.top] = element
        self.top += 1
        return True

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        self.top -= 1
        element = self.base[self.top]
        return element

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.base[self.top - 1]

    def __str__(self):
        return f"Stack: {self.base[:self.top]}"


class LinkStack:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = None  # 栈顶指针
        self.size = 0

    def is_empty(self):
        return self.top is None

    def push(self, element):
        new_node = self.Node(element)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        element = self.top.data
        self.top = self.top.next
        self.size -= 1
        return element

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.data

    def __str__(self):
        elements = []
        current = self.top
        while current:
            elements.append(current.data)
            current = current.next
        return f"Stack: {elements}"