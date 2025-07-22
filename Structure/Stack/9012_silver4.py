import sys
input = sys.stdin.readline
t = int(input().strip())
for i in range(t):
    yn = True
    stack = []
    input_str = input().strip()
    for j in range(len(input_str)):
        if input_str[j] == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                yn = False
                break
            else:
                stack.pop()
    
    if len(stack) != 0:
        yn = False
    
    if yn:  print("YES")
    else:   print("NO")