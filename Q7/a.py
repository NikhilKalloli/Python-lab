class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if len(self.stack) == 0:
            return "Stack is empty"
        return self.stack.pop()
    
    def display(self):
        print("Stack: ")
        return self.stack

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        if len(self.queue) == 0:
            return "Queue is empty"
        return self.queue.pop(0)
    
    def display(self):
        print("Queue: ")
        return self.queue
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.display())
print(stack.pop())
print(stack.display())

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print(queue.display())
print(queue.dequeue())
print(queue.display())
