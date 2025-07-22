import sys
input = sys.stdin.readline

n = int(input().strip())
stack = []
instructions = [input().strip() for _ in range(n)]

def empty():
    if size() == 0: return 1
    else: return 0
    
def top():
    if not empty():
        return stack[len(stack)-1]
    else:
        return -1

def size():
    return len(stack)

def pop():
    if empty():
        return -1
    else:
        return stack.pop()
        
def push(num):
    stack.append(num)

for i in range(n):
    instruction = instructions[i]
    
    if instruction == "top":
        print(top()) 
    elif instruction == "empty":
        print(empty()) 
    elif instruction == "size":
        print(size()) 
    elif instruction == "pop":
        print(pop()) 
    else:   # push
        a,b = instruction.split()
        push(b)
