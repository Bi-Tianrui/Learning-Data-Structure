class SqQueue:
    def __init__(self, max_size=6):
        self.base = [None] * max_size
        self.front = 0  # 队头指针
        self.rear = 0   # 队尾指针，指向下一个插入位置
        self.max_size = max_size

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front

    def enqueue(self, element):
        if self.is_full():
            raise OverflowError("Queue overflow")
        self.base[self.rear] = element
        self.rear = (self.rear + 1) % self.max_size

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow")
        element = self.base[self.front]
        self.front = (self.front + 1) % self.max_size
        return element

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.base[self.front]

    def length(self):
        return (self.rear - self.front + self.max_size) % self.max_size

    def __str__(self):
        if self.is_empty():
            return "Queue: []"
        elements = []
        i = self.front
        while i != self.rear:
            elements.append(self.base[i])
            i = (i + 1) % self.max_size
        return f"Queue: {elements}"