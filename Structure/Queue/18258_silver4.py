import sys
input = sys.stdin.readline
n = int(input().strip())
class Queue:
    def __init__(self):
        self.queue = []
        self.front_idx = 0
        
    def empty(self):
        return self.front_idx == len(self.queue)
    
    def push(self, data):
        self.queue.append(data)
    
    def pop(self):
        if self.empty():
            return -1
        else:
            front_val = self.queue[self.front_idx]
            self.front_idx += 1
            return front_val
        
    def size(self):
        return len(self.queue) - self.front_idx
    
    def front(self):
        if self.empty():
            return -1
        else:
            return self.queue[self.front_idx]
            
    def back(self):
        if self.empty():
            return -1
        else:
            return self.queue[-1]
q = Queue()

for i in range(n):
    command = input().strip()
    if command == "empty":
        if q.empty():   print(1)
        else:   print(0)
    elif(command == "pop"):
        print(q.pop())
    elif(command == "back"):
        print(q.back())
    elif(command == "front"):
        print(q.front())
    elif(command == "size"):
        print(q.size())
    else:
        a, b = command.split()
        q.push(b)